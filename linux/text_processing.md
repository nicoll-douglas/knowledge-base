# Text Processing

## `cut`

### Cutting by character (`-c`)

- `cut -c 5 file.txt` - Extracts and evaluates to characters 5 of each line in file.txt
- `cut -c 1-5,10-15 file.txt` - Extracts and evaluates characters 5 + characters 10 to 15 for each line

### Cutting by field (`-f`) and delimiter (`-d`)

- `cut` uses the tab character as the default delimiter
- If your data uses something else (like commas) to separate columns you must specify it
- `cut -f` accepts field numbers in the same way character numbers are accepted
- The delimiter must be a single quoted character

### Other Options and Behaviour

- `--complement` extracts everything except the fields you specified
- `--output-delimiter` allows you to change the separator in the result to a given string
- You can pass multiple filenames for `cut` to process them in sequence as part of one data stream

## `paste`

- Merges lines from multiple files horizontally using tab as a delimiter

Example:

```
> cat names.txt
Alice
Bob
> cat scores.txt
95
82
> paste names.txt scores.txt
Alice   95
Bob     82
```

### Options

- `-s` - Pastes one file at a time instead of in parallel
- `-d` - Specify the output delimiter
