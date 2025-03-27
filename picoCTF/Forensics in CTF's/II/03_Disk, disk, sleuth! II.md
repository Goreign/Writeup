# Description
All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: dds2-alpine.flag.img.gz

# Solution
```bash
$ mmls dds2-alpine.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)

$ fls -r -o 2048 dds2-alpine.flag.img | grep 'down-at-the-bottom.txt'
+ r/r 18291:    down-at-the-bottom.txt

$ icat -o 2048 dds2-alpine.flag.img 18291 > flag
$ cat flag
```