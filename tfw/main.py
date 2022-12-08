#!/usr/bin/env python3
import argparse

from terraform.file import TerraformFile


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sort", help="Sort a terraform file in alphabetical (or reverse) order."
    )
    parser.add_argument("-file", nargs="+", help="One or more terraform file to sort.")

    args = parser.parse_args()

    sort_value = args.sort
    file_values = args.file

    files = []
    if sort_value:
        if file_values:
            for file in file_values:
                files.append(TerraformFile(file))

    for file in files:
        temp = file.sort(file.blocks, "variable")
        print(temp)


if __name__ == "__main__":
    cli()
