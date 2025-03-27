# Description
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz

# Solution
```bash
$ srch_strings dds1-alpine.flag.img | grep 'pico'