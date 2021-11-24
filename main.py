#!/usr/bin/python3

"""
This is program is intended to to handle .save files from html games, 
that are encode as lz-string. 

For more information on lz-string visit: 
https://pieroxy.net/blog/pages/lz-string/index.html


Example on how to use the lzstring module.

>>> import lzstring
>>> x = lzstring.LZString()
>>> compressed = x.compressToBase64(u'你好') # 'gbyl9NI='
>>> x.decompressFromBase64(compressed) # '你好'
"""

import sys
import lzstring
import json


def get_file_contents(fname: str) -> str:
    with open(file=fname, mode="r") as f:
        contents = [line.strip() for line in f]
    return "".join(contents)


def write_json_to_file(json_data: dict, fname="default.json"):
    with open(file=fname, mode="w") as f:
        json.dump(obj=json_data, fp=f, indent=4)


def decode_lzs(encoded_string: str) -> str:
    x = lzstring.LZString()
    return x.decompressFromBase64(encoded_string)


def main(arglist: list):
    command = arglist[1]
    fname = arglist[2]
    if command == "-r":
        cont = get_file_contents(fname=fname)
        dec_cont = decode_lzs(cont)
        json_data = json.loads(dec_cont)
        write_json_to_file(json_data=json_data)


if __name__ == "__main__":
    main(sys.argv)

