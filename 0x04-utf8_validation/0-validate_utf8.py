#!/usr/bin/python3
"""
UTF-8 Validation Module

This module provides a function to check if a given dataset represents UTF-8.
"""

def validUTF8(data):
    num_bytes = 0  # Number of bytes in the current UTF-8 character
    
    for byte in data:
        byte = byte & 0xFF  # Mask to ensure only the last 8 bits are used
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character based on leading bits
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character should start with 0
                return False
        else:
            # Check that the byte is a continuation byte (starts with '10')
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    
    # If num_bytes is not zero, it means there are incomplete characters
    return num_bytes == 0
