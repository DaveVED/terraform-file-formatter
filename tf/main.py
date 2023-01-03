#!/usr/bin/env python3
import argparse
import validators
import terraform.writter as writter

from logger import logger
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
    parser.add_argument("--debug", "-d", action="store_true", help="Print debug messages.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose output.")
    
    args = parser.parse_args()

    sort_value = args.sort
    file_values = args.file
    debug = args.debug
    verbose = args.verbose

    if debug:
        logger.debug("This is a debug message")

    
    if verbose:
        logger.info("Starting in verbose mode...")
    
    # Handle `sort` arg.
    if sort_value:
        # Sort if any files exist.
        if file_values and len(file_values) > 0:
            try:
                
                # Validate file extension.
                if validators.are_terraform_files(file_values):
                    
                    # Build each file object.
                    for file in file_values:
                        if debug:
                            logger.debug(f"Formating file {file}")
                        terraform_file = TerraformFile(file)
                        
                        # Verify it's a valid terraform file.
                        status, block_type = validators.has_valid_block_type(
                            terraform_file.file_content
                        )
                        
                        # If valid file.
                        if status:
                            content = terraform_file.file_content

                            # Sort content.
                            sorted_content = terraform_file.sort(
                                content, block_type, None
                            )

                            if sorted_content:
                                # Write Content.
                                if debug:
                                    file_name = file.split("/")[3]
                                    file = f"test/files/output-files/{file_name}"
                                    logger.debug(f"Writing output file to {file}")
                                terraform_writter.write(sorted_content, file)
                            else:
                                #TODO: Throw error.
                                pass
                        else:
                            raise NoValidBlockTypeException(None)
            except NotATerraformFileException as e:
                logger.error(f"Error: {e}")
            except InvalidBlockTypeException as e:
                logger.error(f"Error: {e}")
            except NoValidBlockTypeException as e:
                logger.error(f"Error: {e}")
        else:
            raise NoProvidedTerraformfileException([])


if __name__ == "__main__":
    cli()
