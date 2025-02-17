# Description
> Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

# Solution
**strings**
It's a utility that is used to search for printable strings in binary files.
```bash
$ strings strings
// too massive to read?
$ strings strings | grep "picoCTF"
```
`|` is used to pipe the output of one command as the input to another command. 
`grep` is a search-find-like command.