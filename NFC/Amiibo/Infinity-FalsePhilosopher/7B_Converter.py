import argparse
import os
import pathlib
from typing import Tuple
import time
import binascii
import hashlib
import re
import sys

# mifare classic mini DI 7b uid binary to flipper .nfc converter.
# Created by Equipter with code portions borrowed from Lucaslhm/AmiiboFlipperConverter
# V1.09
# Modified by FalsePhilospher to work with DI toys

# Function from infsha.py
uidre = re.compile('^04[0-9a-f]{12}$', re.IGNORECASE)
magic_nums = [3, 5, 7, 23, 9985861487287759675192201655940647, 38844225342798321268237511320137937]

def calc_keya(uid, sector):
    if uidre.match(uid) is None:
        raise ValueError('invalid UID (seven hex bytes)')

    if sector < 0 or sector > 4:
        raise ValueError('invalid sector (0-4)')

    PRE = format(magic_nums[0] * magic_nums[1] * magic_nums[3] * magic_nums[5], '032x')
    POST = format(magic_nums[0] * magic_nums[2] * magic_nums[4], '030x')

    sha1 = hashlib.sha1()
    sha1.update(binascii.unhexlify(PRE + uid + POST))
    key = sha1.digest()

    return binascii.hexlify(key[3::-1] + key[7:5:-1]).decode()

# Functions from 7B_Converter.py
def write_output(name: str, assemble: str, out_dir: str):
    with open(os.path.join(out_dir, f"{name}.nfc"), "wt") as f:
        f.write(assemble)

def convert(contents: bytes) -> Tuple[str, int, int]:
    buffer = []
    Block_count = 0
    Mf_size = 0

    Block = []
    key_a = None
    uid = get_uid(contents).replace(' ', '')
    key_a = calc_keya(uid, 0).upper()
    formatted_key_a = ' '.join([key_a[i:i+2] for i in range(0, len(key_a), 2)])

    for i in range(len(contents)):
        byte = contents[i : i + 1].hex()
        Block.append(byte)

        if len(Block) == 16:
            if Block_count in [2, 3, 7, 11, 15, 19]:  # Insert Key A in these blocks
                Block[0:6] = formatted_key_a.split()  # Insert Key A
                Block[10:16] = formatted_key_a.split()  # Insert Key B
            buffer.append(f"Block {Block_count}: {' '.join(Block).upper()}")
            Block = []
            Block_count += 1

        if Block_count == 64:
            Mf_size = 1
        elif Block_count == 128:
            Mf_size = 2
        elif Block_count == 256:
            Mf_size = 4
    return "\n".join(buffer), Block_count, Mf_size

def get_uid(contents: bytes) -> str:
    Block = []
    for i in range(7):
        byte = contents[i : i + 1].hex()
        Block.append(byte)
    return " ".join(Block).upper()

def get_sak(contents: bytes) -> str:
    Block = []
    for i in range (7,8):
        sak = contents[i : i + 1].hex()
        Block.append(sak)
    return " ".join(Block).upper()

def get_atqa(contents: bytes) -> str:
    Block = []
    for i in range (8,10):
        atqa = contents[i : i + 1].hex()
        Block.append(atqa)
    return " ".join(Block).upper()

def assemble_code(contents: bytes) -> str:
    conversion, Block_count, Mf_size = convert(contents)
    uid = get_uid(contents)
    key_a = calc_keya(uid.replace(' ', ''), 0)  # Calculate key A

    return f"""Filetype: Flipper NFC device
Version: 4
# Nfc device type can be UID, Mifare Ultralight, Mifare Classic, Bank card
Device type: Mifare Classic
# UID, ATQA and SAK are common for all formats
UID: {uid}
ATQA: 00 44
SAK: 09
# Mifare Classic specific data
Mifare Classic type: MINI
Data format version: 2
# Mifare Classic Blocks, '??' means unknown data
# Key A: {key_a}
{conversion}
"""

def convert_file(input_path: str, output_path: str):
    input_extension = os.path.splitext(input_path)[1]
    if input_extension == ".bin":
        with open(input_path, "rb") as file:
            contents = file.read()
            name = os.path.split(input_path)[1]
            write_output(name.split(".bin")[0], assemble_code(contents), output_path)

def process(path: str, output_path: str):
    if os.path.isfile(path):
        convert_file(path, output_path)
    else:
        for filename in os.listdir(path):
            new_path = os.path.join(path, filename)
            if os.path.isfile(new_path):
                convert_file(new_path, output_path)
            else:
                process(new_path, output_path)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input-path",
        required=True,
        type=pathlib.Path,
        help="Single file or directory path to convert",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        required=False,
        type=pathlib.Path,
        help="Output path, if not specified, the output .nfc file will be created in the same directory the .bin file exists within.",
    )

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    if os.path.isfile(args.input_path):
        if not args.output_path:
            args.output_path = os.path.split(args.input_path)[0]

    os.makedirs(args.output_path, exist_ok=True)
    process(args.input_path, args.output_path)

if __name__ == "__main__":
    main()
    print("Converting...")
    time.sleep(0.3)
    print("Completed Conversion")
