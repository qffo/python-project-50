#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_path_1')
    parser.add_argument('file_path_2')
    parser.add_argument(
        "-f", "--format", help="set format of output (default: 'stylish')")
    args = parser.parse_args()
    diff = generate_diff(args.file_path_1, args.file_path_2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
