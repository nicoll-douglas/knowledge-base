# Vim

## netrw

- `%` - Create a new file
- `d` - Create a new directory
- `-` - Go up one directory go
- `u` - Return to the previous directory
- `r` - Refresh the directory listing
- `R` - Rename a file
- `D` - Delete a file
- `Leader + E` - Open netrw (E for explorer)
- `Leader + Q` - Close netrw (Q for quit)

## Editor

- `Leader + R` - Toggle relative line numbers

### Switching Modes

- `jj` - Insert -> normal
- `v` - Insert -> visual
- `Leader + Leader` - Visual -> normal
- `Shift + V` - Select a line in visual mode
- `Ctrl + V` - Enter visual mode, select a rectangular block of text
- `a` - Enter insert mode and start inserting _after_ the caret
- `i` - Enter insert mode and start inserting _before_ the caret
- `Shift + a` - Enter insert mode and start inserting at the _end_ of the line
- `Shift + i` - Enter insert mode and start inserting at the _start_ of the line
- `o` - Open a new line _below_ the current and enter insert mode
- `Shift + O` - Open a new line _above_ the current and enter insert mode

### Navigation

#### Normal/Visual Mode

- `h` - Move left
- `j` - Move down
- `k` - Move up
- `l` - Move right
- `0` - Go to the _first_ character of the line
- `$` - Go to the _last_ character of the line
- `^` - Go to the first _non-blank_ character of the line
- `gg` - Go the _first_ line of the file
- `Shift + G` - Go the _last_ line of the file
- `w` - Go to the start of the _next_ word
- `b` - Go to the start of the _last_ word
- `e` - Go to the end of the _next_ word
- `<number>w` - Jump to the start of the \<number\>th next word
- `<number>b` - Jump to the start of the \<number\>th last word
- `<number>e` - Jump to the end of the \<number\>th next word
- `f<char>` - Find the next occurence of \<char\> in the line and jump to it
- `F<char>` - Find the previous occurence of \<char\> in the line and jump to it
- `;` - Repeat the the last `f` command
- `,` - Repeat the last `f` in the opposite direction
- `%` - Go to the matching bracket

#### Commands

- `:<number>` - Move to the line \<number\> number
- `:$` - Move to the last line
- `:-<number>` - Move \<number\> lines up
- `:+<number>` - Move \<number\> lines down

### Insertion & Deletion

- `dw` - Cut a word starting at the caret
- `dd` - Delete a line
- `u` - Undo the last action
- `Ctrl + R` - Redo the last action
- `p` - Paste the last item after the caret or after the current line
- `Shift + P` - Paste the last time before the caret or before the current line
- `yw` - Copy a word
- `yy` - Copy a line
- `diw` - Cut the current word
- `yiw` - Copy the current word

### Searching

- `/` - Open a search query
- `n` - Go to the next match
- `Shift + n` Go to the previous match
- `?` - Open a search query in the reverse direction

### Useful Shortcuts / Motions

- `Shift + M` - Go to the line in the middle of the screen
- `Shift + H` - Go to the line at the top of the screen
- `Shift + L` - Go to the line at the bottom of the screen
- `zz` - Scroll the current line to the middle of the screen
- `.` - Repeat the last change made in normal mode
- `Shift + zz` - Save and quit vim
