# Process

## Process Permissions

- Each process when started has certain user IDs attached to it, being the following:
  - User ID (UID)
  - Effective user ID (EUID)
  - Saved user ID (SUID)
  - Group ID (GUID)
  - Effective group ID (EGID)
  - Saved group ID (SUID)
- The UID is set to the user that started the process
- The EUID is set to whoever is given effective control (usually UID but with the setUID bit, this will be the owner of the executable)
- The SUID will be set to EUID, this allows the process to memorise the initial EUID so that it can change the EUID as suited to regulate privileges
- The above also apply to the group ID equivalents and the setGID bit

## Creating Processes

- When a process needs to start a new task, it uses a system call called fork()
- This creates a near-exact copy of the parent process
- When the copy is made, the child process usually runs the exec() system call to replace its memory space with the new program it is intended to run
- The very first process created after your system boots is called init (systemd in modern distros)
- init is the ancestor of all other processes

## Process States

- **Running (R)**: The process is actively executing or waiting in the run queue
- **Sleeping (S)**: The process is waiting for an event (e.g user input, file read)
- **Stopped (T)**: The process has been paused (usually by a signal like Ctrl+Z)
- **Zombie (Z)**: The process has finished but its parent hasn't acknowledged it yet

## Process Signals
