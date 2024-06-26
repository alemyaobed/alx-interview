#!/usr/bin/python3
'''
Write a method that determines if a given data set represents a valid UTF-8
encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the
8 least significant bits of each integer
'''
def validUTF8(data) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0

    for byte in data:
        # Mask to get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character (0xxxxxxx), valid if MSB is set to 1.
                return False
        else:
            # Continuation byte must be of the form 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
