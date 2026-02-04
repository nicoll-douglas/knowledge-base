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
