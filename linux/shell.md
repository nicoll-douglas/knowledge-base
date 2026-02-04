# Shell

## Shell Types

### Login Shell

- A shell that starts a user session, typically when you:
  - Log in to a virtual console (tty)
  - SSH into a machine
  - Log in via a display manager
- Reads and executes the system-wide login initilization file /etc/profile and the per-user login initialization ~/.profile (or ~/.bash_login or ~/.bash_profile)

### Interactive Shell

- A shell where you can type in commands
- Can be a login or non-login shell
- Reads and executes the system-wide initialization file /etc/bash.bashrc (Debian/Ubuntu) and the per-user initialization ~/.bashrc
- Non-interactive shells don't have interactive features

## Text Quirks

- Editors like vim and nano add a new-line character to the end of file to keep it POSIX compliant (text files defined as zero or more lines ending with a new-line character)

## Shell Behaviour

### Environment Variables

- Shell variables only exist in the shell
- Environment variables are part of the environment (exported variables)
- When you start a child process from a shell it receives all environment variables
- When you run a command in a shell, the shell process forks itself and then loads a new program into the process memory
  - This way the child process inherits things like environment variables, open file descriptors, cwd, etc.
  - The child process will get a new process ID
  - The child process will run in the foreground (shell waits for it to finish)
  - The child process can also be run in the background (shell doesn't wait for it to finish, child runs async)
- When you run a script with `source`, no child process is created, it runs in the context of the current shell (things like cd and changes to environment variables affect the current shell)
  - When the script exits, control is handed back to the origin shell/script and it will keep running

### `exec`

- If you use `exec` to run a command, no new processes are forked, instead the shell gets replaced with another command
- When the command exits, the origin shell will no longer exist (in a script any commands after will never run)
- Can be used in things like containers in order to replace the shell with the native container process
- Much like when a new process is ran in a shell, a command ran under `exec` inherits the environment of the origin shell
- The process ID stays the same

#### Usage

- `exec <command>` - Runs a command with exec
- `exec > <file_path>` - Permanently redirect stdout to a file for the current shell
- `exec 0< <file_path>` - Permanently redirect stdin to a file for the current shell

## Redirects & Streams

- stdin = file descriptor 0
- stdout = file descriptor 1
- stderr = file descriptor 2

| Operator | Description                                              |
| -------- | -------------------------------------------------------- |
| `>`      | Redirect stdout to a file, overwriting it                |
| `>>`     | Redirect stdout to a file, appending to it               |
| `<`      | Redirect stdin from a file                               |
| `2>`     | Redirect stderr to a file, overwriting it                |
| `2>>`    | Redirect stderr to a file, appending to it               |
| `&>`     | Redirect stderr and stdout to a file                     |
| `<<`     | Here-document: redirect stdin from a block of text       |
| `<<<`    | Here-string: redirect stdin from a string                |
| `\|`     | Pipe: redirect stdout of one command to stdin of another |
| `>&`     | Redirect output file descriptors                         |
| `<&`     | Redirect input file descriptors                          |

### Manipulating File Descriptors

- `exec 3>&1 4>&2 5<&0` - Points file descriptor 3 to stdout and file descriptor 4 to stderr (duplicates them)
- `exec 1>&3 2>&4 0<&5` - Points file descriptor 1 to stdout (which was saved) and file descriptor 4 to stderr (also saved); restores the standard output streams
- `exec 3>&- 4>&- 5<&-` - Closes temporary file desciptors that we were using before

## Here-documents & Here-strings

### Here-documents

- Allows you to feed a block of text into stdin of a command
- Requires an opening and closing delimiter (which must be on its own line)
- Variable expansion is allowed unless you quote the delimiter (e.g "DELIMITER", 'DELIMITER' - both allowed)

Syntax:

```
command << DELIMITER
line 1
line 2
DELIMITER
```

### Here-strings

- Allows you to feed a string into stdin of a command
- Quotes are needed if the string has spaces
- Single quotes prevent variable expansion whereas double quotes allow it
- You can embed new lines into it with \\n

Syntax:

```
command <<< "string"
```

## Help

- `which` - locates a binary
- `whatis` - display one line page description of a binary
- `whereis` - locates the file, source and manual for a binary
- `man <binary>` - shows the manual page for a binary
- `help <builtin>` - shows help information for a shell builtin
- `type -a <command>` - shows all locations of an executable command and what it is (i.e binary, builtin)

## Command History

### `history`

- Use the `history` command to view command history
- Bash has command history persisted in ~/.bash_history
- The max number of entries in the file is according to the $HISTFILESIZE environment variable
- An in-memory history list is also kept for each shell
- The max number of entries in the in-memory history is according to the $HISTSIZE environment variables
- When a shell starts, the last $HISTSIZE (e.g 1000) commands are loaded from the history file
- Each time a command is ran in the shell session it is appended to the in-memory history list
- When the shell closes, any new items in the history are appended to the history file

#### Usage

- Ctrl + R can be used in the terminal to perform a reverse search for a command, finding the first match
- Ctrl + R can be pressed again to find the next match
- `history <n>` - Show the last n commands
- `history !n` - Repeat command number n
