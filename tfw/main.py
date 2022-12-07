#!/usr/bin/env python3
import argparse

from terraform_file import TerraformFile
from terraform_file_writter import TerraformFileWritter


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f", nargs=1, type=str, help="flag for doing something with a file"
    )
    parser.add_argument("-r", action="store_true", help="flag for doing something else")
    parser.add_argument("-a", action="store_true", help="flag for doing another thing")

    args = parser.parse_args()

    # add in error handle and help... Cant have f and a..
    # error check for > 1 file.. We should loop over each one.
    # for now one file to test.
    # why am i not using click.
    if args.f:
        fp = args.f[0]

        tf = TerraformFile(fp)
        tfs = tf.get_sorted_terraform_blocks()
        tfw = TerraformFileWritter(tfs)
    if args.r:
        print("r")
    if args.a:
        print("a")


if __name__ == "__main__":
    cli()
