"""
This week I'd like you to write a function for formatting numbers into human-readable byte sizes (kilobytes, megabytes, gigabytes, etc.).

Your format_bytes function should accept a number of bytes as an integer and should return a string with 1-3 digits and a suffix which represent that number of bytes.

>>> format_bytes(0)
'0B'
>>> format_bytes(500)
'500B'
>>> format_bytes(56374)
'56KB'
>>> format_bytes(87238722)
'87MB'
>>> format_bytes(9876543210)
'10GB'
>>> format_bytes(591627861221937)
'592TB'
Note that the output is rounded to the nearest whole number and the greatest prefix (e.g. GB instead of MB) is used which will still allow for a non-zero number.

The suffixes you should support are:

B for Bytes
KB for Kilobytes (1KB = 1000B)
MB for Megabytes (1MB = 1000KB)
GB for Gigabytes (1GB = 1000MB)
TB for Terabytes (1TB = 1000GB)
One more thing: your format_size function should return a ValueError for negative bytes.

Bonus 1

For the first bonus, your format_bytes function should accept an optional bits argument which, when True, will use a lowercase b instead of an uppercase B and will return the number of bits instead of the number of bytes (8 bits in 1 byte).

>>> format_bytes(0, bits=True)
'0b'
>>> format_bytes(500, bits=True)
'4Kb'
>>> format_bytes(500, bits=False)
'500KB'
>>> format_bytes(56374, bits=True)
'451Kb'
>>> format_bytes(9876543210, bits=True)
'79Gb'
"""
byte_set = [1000**i for i in range(4, -1, -1)]
byte_prefixes = ['TB', 'GB', 'MB', 'KB', 'B']

def format_bytes(bytes, bits=False):
    if bytes < 0:
        raise ValueError('bytes cannot be negative')
    elif bytes == 0:
        return '0B'
    unit = 'B'
    value = 0
    i = 0
    while i < len(byte_set):
        if bytes % byte_set[i] != bytes:
            unit = byte_prefixes[i]
            value = bytes / byte_set[i]
            break
        i += 1
    value = round(value) if bits == False else round(value * 8)
    if bits is True:
        unit = unit[:-1] + 'b'

    return f"{value}{unit}"
