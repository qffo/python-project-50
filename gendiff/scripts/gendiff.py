#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def parsing_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_path_1')
    parser.add_argument('file_path_2')
    parser.add_argument(
        "-f",
        "--format",
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help="set format of output (default: 'stylish')")
    return parser.parse_args()


def main():
    args = parsing_arguments()
    diff = generate_diff(args.file_path_1, args.file_path_2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
