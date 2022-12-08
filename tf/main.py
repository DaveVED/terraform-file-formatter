#!/usr/bin/env python3
import argparse
import validators

from terraform.file import TerraformFile
from exceptions import (
    NotATerraformFileException,
    InvalidBlockTypeException,
    NoValidBlockTypeException,
)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sort", help="Sort a terraform file in alphabetical (or reverse) order."
    )
    parser.add_argument("-file", nargs="+", help="One or more terraform file to sort.")

    args = parser.parse_args()

    sort_value = args.sort
    file_values = args.file

    if sort_value:
        if file_values:
            try:
                if validators.are_terraform_files(file_values):
                    file_content = TerraformFile(file_values).file_content
                    # if validators.has_valid_block_type(file_content):
                    print("HELLO WORLD")
            except NotATerraformFileException as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    cli()
