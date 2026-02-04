# Users

## Switching to a User

### `su`

- Used to give a full login shell as another user
- Requires the user's password
- You can run individual commands with

#### Usage

- `su - <user>` - Run an interactive login shell for \<user\> (root if left blank)

## Superusers

### `sudo`

- Used to run commands as another user
- A login shell can be granted with `sudo` as with `su`
- On a Linux system, the root user has the highest privileges
- Users can be added to the sudo group to mark them as a superuser (lets you run commands with elevated privileges)

#### Usage

- `sudo -u <user> <command>` - Run \<command\> as \<user\> (root if user option not specified)
- `sudo -u <user> -i` - Run an interactive login shell for \<user\> (root if left blank)

### Delegating a Superuser

Creating:

```
sudo usermod -aG sudo <username> # creates a superuser by adding them to the sudo group
```

Removing:

```
sudo deluser <username> sudo # removes a superuser by removing them from the sudo group
```
