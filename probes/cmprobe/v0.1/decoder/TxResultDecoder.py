#!/usr/bin/python3
# --*-- coding: utf-8 --*--


def batch_decode(octal_strings):
    for tmp in octal_strings.split("\\"):
        print(decode(tmp), end=" ")


def decode(octal_string: str) -> str:
    bytes_data = bytes([int(c, 8) for c in octal_string])

    # 解码为UTF-8
    utf8_string = bytes_data.decode('utf-8')

    return utf8_string


if __name__ == '__main__':
    batch_decode(r'\020\001\032')

