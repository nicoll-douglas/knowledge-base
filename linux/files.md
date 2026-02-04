# Files

## File Permissions

- Read (r) - Allows you to view the contents of a file
- Write (w) - Allows you to modify the contents of the file
- Execute (x) - Allows you to execute the file as a program/script

### Directories

- Read (r) - Allows you to view the contens of a directory (i.e `ls -ld`)
- Write (w) - Allows you to create, delete, or rename files in the directory (you also need execute permissions on the directory to write)
- Execute (x) - Allows you enter the directory and access files essentially acting as a lock to anything inside (i.e `cd` or `cat dir/file` if you know the filename)

### SetUID Bit

- Used on files
- Set using `chmod u+s <filename>`
- When the file is executed, the EUID is set to the file's owner
- Allows user to execute the file with owner permissions
- As long as the current user has execute permissions and the setUID bit is set, they can execute as the owner

Display:

```
-rwSrw-r-- # uppercase s means owner can't execute but setuid bit is set
-rwsrw-r-- # lowercase s means owner can execute and setuid bit is set
```

### SetGID Bit

- Used on files and directories
- Set using `chmod g+s <file_or_dir>`
- For files:
    - When the file is executed, the EGID is set to the file owner's GID
    - Allows user to execute with owner's group permissions
    - As long as the current user has execute permissions and the setGID bit is set, they can execute as the owner's group
- For directories:
    - Any new files or directories created **only** in that directory (1 level) will inherit the owner group of the directory
    - As long as the user has write permissions for that directory (and execute) they can create a file as such

Display:

```
-rw-rwS-r-- # uppercase s means group user can't execute but setgid bit is set
-rw-rws-r-- # lowercase s means group user can execute and setuid bit is set
```

### Sticky Bit

- Used on directories
- Set using `chmod +t <directory>`
- You need write and execute on a directory to delete or rename a file in that directory
- Sticky bit adds an extra restriction: allows **only** the owner of the file or the directory owner to delete a file (so group users and other users can't delete/rename even if they have permissions)

Display:

```
-rw-rw-r-T # uppercase t means other users can't execute but sticky bit is set
-rw-rw-r-t # lowercase t means other users can execute and sticky bit is set
```

### Umask

- The umask is a per-shell configuration that dictates what permissions new files will have
- New files are *usually never* created with executable permissions
- New directories are *usually* created with executable permissions
- The umask is subtractive and set with the umask command where each digit removes those permission bits from the respective permission set (ugo)
- Example: `umask 022`, files don't start with execute (1 bits) so start with 666, then umask creates 644 by removing the 2 bits from group and other
- 022 is a common umask, for Debian 13 it is 002
- Umask is per-shell so when a shell starts it takes on the default umask (either system default or parent shell umask)
- Child process inherit the current umask
- When a shell exits, the umask is lost (doesn't persist)

## Archiving and Compressing

### `tar`

- Used to create and extract tar archives (tarballs)

#### Usage

- `tar -cvf <tar_filename> <target>` - Create a tar archive
- `tar -cvzf <targz_filename> <target>` - Create a compressed tar archive using gzip
- `tar -xvf <tar_filename> -C <target>` - Extract a tar archive
- `tar -xvzf <targz_filename> -C <target>` - Extract a gzip-compressed tar archive

### `gzip` and `zip`

- Use the `zip` command to zip files and folders
- Use the `unzip` command to unzip .zip files
- Use the `gzip` command to compress files with gzip compression
- Use the `gunzip` command to extract gzip compressed files

## Hard and Soft (Symbolic) Links

### Hard Links

- Each file on a file system has an inode that stores metadata and pointers to the file's data blocks
- A hard link is just another filename that points to the same inode
- The number after a file's permissions is the number of hard links in `ls -l` output
- You can check the inode a file with `ls -i`
- Hard links cannot cross filesystems (including mounted filesystems)
- Deleting a hard link does not delete a file
- A file is only deleted when the link count reaches 0
- Hard links share the same metadata and file content, the only thing that differs is the filename

### Soft Links

- A soft link is a separate file that points to another file (its file path)
- If the original file is deleted, the link becomes a "dangling link"
- Directories can also be symlinked
- Soft links don't recieve their source's file content directly, rather the path is followed
- Soft links follow the path they point to so if the source path is relative, moving the symlink file may break it
- Soft links that point to absolute paths are more stable

### `ln`

- Use for creating hard and soft links

#### Usage

- `ln <source_path> <destination_path>` - Create a hard link to the inode at `<source_path>` at `<destination_path>`
- `ln -s <source_path> <destination_path>` - Create a soft link to `<source_path>` at `<destination_path>`

