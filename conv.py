#!/usr/bin/env python
"""
 Date: 11/23/2012
 Author: Sam Chapler
 Name: conv.py
"""

import argparse
from prettytable import PrettyTable


def getargs():
    """Converts bytes to other shit."""
    parser = argparse.ArgumentParser(
        description='Converts bytes to other shit.')
    parser.add_argument(
        'integer', metavar='INT', type=float,
        help='Integer value to convert')
    parser.add_argument(
        'unit', metavar='b|k|m|g|t', type=str, help='unit of the integer',
        choices='bkmgt')

    args = parser.parse_args()
    num = args.integer + 0.0

    vals = []
    units = [
            'Bytes',
            'Kilobytes',
            'Megabytes',
            'Gigabytes',
            'Terabytes']

    if args.unit == 'b':
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024 / 1024)
    elif args.unit == 'k':
        vals.append(num * 1024)
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
        vals.append(num / 1024 / 1024 / 1024)
    elif args.unit == 'm':
        vals.append(num * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num)
        vals.append(num / 1024)
        vals.append(num / 1024 / 1024)
    elif args.unit == 'g':
        vals.append(num * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num * 1024)
        vals.append(num)
        vals.append(num / 1024)
    elif args.unit == 't':
        vals.append(num * 1024 * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024 * 1024)
        vals.append(num * 1024 * 1024)
        vals.append(num * 1024)
        vals.append(num)

    results = zip(units, vals)
    return results

def conv(results):
    """Build the conversion table"""
    table = PrettyTable()
    table.field_names = ['Units', 'Size']
    table.align = 'l'
    table.padding_width = 1

    for unit, size in results:
        table.add_row([unit, size])
    print table

if __name__ == '__main__':
    RESULT_LIST = getargs()
    conv(RESULT_LIST)
