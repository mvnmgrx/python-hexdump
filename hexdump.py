"""Hexdump in Python

Author:
    (C) Marvin Mager - @mvnmgrx - 2022

License identifier:
    MIT

Major changes:
    21.07.2022 - created
"""


def dump_to_console(data: bytearray, start_addr: int = 0x0):
    """Dump an array of bytes to the standard output

    Args:
        data (bytearray): Array of bytes to be dumped
        start_addr (int, optional): Starting address to be displayed in the dump. Defaults to 0x0.

    Raises:
        See exceptions of dump() function
    """
    print(dump(data, start_addr))

def dump(data: bytearray, start_addr: int = 0x0) -> str:
    """Dump an array of bytes into a string

    Args:
        data (bytearray): Array of bytse to be dumped
        start_addr (int, optional): Starting address to be displayed in the dump. Defaults to 0x0.

    Raises:
        Exception: When the length of the byte array is zero
        Exception: When the length of the byte array is bigger than 2^16
        Exception: When the starting address is negative

    Returns:
        str: Hex dump as string
    """
    if len(data) == 0:
        raise Exception("Cannot dump 0 bytes")

    if len(data) > 2**16:
        raise Exception("Byte array is too large")

    if start_addr < 0:
        raise Exception("Start address cannot be negative")

    dump_str = ""

    # Start to print the dump table
    dump_str = '     | '
    for i in range(min(len(data), 16)):
        if i < 10:
            dump_str += f'0{i} '
        else:
            dump_str += f'{i} '
    dump_str += f'\n-----+-{"---" * min(len(data), 16)}'

    chars_last_row = ""
    counter = 0

    # Iterate over each datum
    for datum in data:

        # Line end is handled here
        if counter %16 == 0:
            if counter > 0:
                dump_str += f' | {chars_last_row} |'
                chars_last_row = ""
            dump_str += '\n{:04x} |'.format(counter + start_addr)

        # Print datum and add it to the character row of the current line
        dump_str += ' {:02x}'.format(datum)
        chars_last_row = chars_last_row + (chr(datum) if (datum >= 0x20 and datum <= 0x7E) else ' ')
        counter += 1

    # The last character line will be printed after the loop
    if counter % 16 != 0:
        dump_str += ' '*((16 - (counter % 16)) * 3)
        dump_str += f' | {chars_last_row}{" "*((16 - (counter % 16)) * 1)} |'
    else:
        dump_str += f' | {chars_last_row} |'

    dump_str += f'\nDumped {counter} bytes'
    return dump_str
