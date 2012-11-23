#/usr/bin/env python
#Date: 11/23/2012
#Author: Sam Chapler
#Name: conv.py


import argparse
import string


def main():

    parser = argparse.ArgumentParser(
        description='Usage: %prog [value] [size]',
        epilog='Converts file size into equivilents.')
    parser.add_argument(
        'integer', metavar='INT', type=float,
        help='value in b, kb, mb, gb or tb')
    parser.add_argument(
        'size', metavar='SIZE', type=str, help='indicate the size',
        choices='b, k, m, g, t')

    args = parser.parse_args()
    num = args.integer + 0.0

    vals = []
    sizes = ['Bytes:', 'Kilobytes:', 'Megabytes:', 'Gigabytes:', 'Terabytes:']
    if args.size == 'b':
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024 / 1024)
    elif args.size == 'k':
        vals.append(num * 1024)
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024)
    elif args.size == 'm':
        vals.append(num * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
    elif args.size == 'g':
        vals.append(num * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num * 1024)
        vals.append(num)
        vals.append(num / 1024)
    elif args.size == 't':
        vals.append(num * 1024 * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num * 1024)
        vals.append(num)

    for s, n in zip(sizes, vals):
        print string.rjust(s, 10), string.rjust(str(n), 2)


if __name__ == '__main__':
    main()
