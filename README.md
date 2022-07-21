# Python Hexdump
Simple function to dump an array of bytes into a bytewise hex dump.

## Example

```python
from os import urandom
from hexdump import dump_to_console

def main():
    data = bytearray(os.urandom(128))
    dump_to_console(data)

if __name__ == '__main__':
    main()
```

Prints the following output to the console:
```plaintext
     | 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 
-----+-------------------------------------------------
0000 | 04 a8 e0 6a c7 3a 6a d8 a1 33 d0 f9 2a 2f 37 a6 |    j :j  3  */7  |
0010 | 19 5a 02 93 09 19 b6 1a 71 00 73 5b 28 14 f9 6e |  Z      q s[(  n |
0020 | e6 5d 16 78 37 52 70 da 58 bf 5c b6 00 e7 e7 4d |  ] x7Rp X \    M |
0030 | 95 ae 3f 0a db fc 42 78 ca 65 a4 ed 1e d5 6c 15 |   ?   Bx e    l  |
0040 | db 7c ca 63 25 a5 9c e4 6f 6f 0d 8f 73 ec da 8f |  | c%   oo  s    |
0050 | 40 fe b8 32 16 32 39 68 0b cf 4c 76 bd 4b 0f e2 | @  2 29h  Lv K   |
0060 | 91 cd 27 ae 09 54 06 28 77 28 0f 01 e4 3b 7e 79 |   '  T (w(   ;~y |
0070 | 2b 5d 9d 63 28 06 47 1f 98 0b 54 2d 85 99 d2 dd | +] c( G   T-     |
0080 | 9f 9b e8 80 89 e4 34                            |       4          |
Dumped 135 bytes
```