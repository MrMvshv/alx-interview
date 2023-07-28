#!/usr/bin/python3
"""
method that determines if data set
represents  valid UTF-8 encoding.
"""


def isByteStart(num):
    """ function to check if a number is a valid utf-8 start byte"""
    return (num & 0b10000000) == 0b00000000


def isByteContinue(num):
    """ function to check if a number is a valid utf-8 continuation byte"""
    return (num & 0b11000000) == 0b10000000


def validUTF8(data):
    """checks if is valid utf-8"""
    i = 0

    while i < len(data):
        numOfBytes = 0

        if isByteStart(data[i]):
            if (data[i] & 0b11110000) == 0b11110000:
                numOfBytes = 4
            elif (data[i] & 0b11100000) == 0b11000000:
                numOfBytes = 3
            elif (data[i] & 0b11000000) == 0b10000000:
                numOfBytes = 2
            else:
                numOfBytes = 1
        else:
            return False

        for j in range(1, numOfBytes):
            if i + j >= len(data) or not isByteContinue(data[i + j]):
                return False

        i += numOfBytes
    return True
