#!/usr/bin/env python3
import argparse
import validators
import terraform.writter as writter

from terraform.file import TerraformFile
from exceptions import (
    NotATerraformFileException,
    InvalidBlockTypeException,
    NoValidBlockTypeException,
    NoProvidedTerraformfileException,
)
from terraform.writter import TerraformFileWritter

terraform_writter = TerraformFileWritter()


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sort", help="Sort a terraform file in alphabetical (or reverse) order."
    )
    parser.add_argument("-file", nargs="+", help="One or more terraform file to sort.")

    args = parser.parse_args()

    sort_value = args.sort
    file_values = args.file

    # Handle `sort` arg.
    if sort_value:
        if file_values and len(file_values) > 0:
            try:
                if validators.are_terraform_files(file_values):
                    for file in file_values:
                        terraform_file = TerraformFile(file)
                        status, block_type = validators.has_valid_block_type(
                            terraform_file.file_content
                        )

                        if status:
                            blocks = terraform_file.file_content

                            sorted_blocks = terraform_file.sort(
                                blocks, block_type, None
                            )

                            # if sort is not none. TODO. Should never happen.
                            # else write.
                            # change the writer to catch error on false to write. TODO.
                            terraform_writter.write(sorted_blocks, file)
                        else:
                            # shold never happen, am I crazy?...
                            raise NoValidBlockTypeException(None)
            except NotATerraformFileException as e:
                print(f"Error: {e}")
            except InvalidBlockTypeException as e:
                print(f"Error: {e}")
            except NoValidBlockTypeException as e:
                print(f"Error: {e}")
        else:
            raise NoProvidedTerraformfileException([])


if __name__ == "__main__":
    cli()
