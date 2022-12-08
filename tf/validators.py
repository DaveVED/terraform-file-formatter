from exceptions import (
    NotATerraformFileException,
    InvalidBlockTypeException,
    NoValidBlockTypeException,
)
from terraform.block import BlockType


def are_terraform_files(file_paths: list) -> bool:
    """Check if a list of files are Terraform files.

    If the list is empty, return False. If any of the files are not Terraform files, raise a NotATerraformFileException with the file path as the argument. If all of the files are Terraform files, return True.

    Args:
        file_paths (list): The paths to the files.

    Returns:
        bool: True if the files are Terraform files, False otherwise.

    Raises:
        NotATerraformFileException: If any of the files are not Terraform files.
    """
    if not file_paths:
        return False

    for path in file_paths:
        if not path.endswith(".tf"):
            raise NotATerraformFileException(path)

    return True


def has_valid_block_type(file_content: dict) -> tuple[bool, BlockType]:
    """Check if the input dictionary has a valid block type.

    If the dictionary contains both a 'variable' and 'output' block, raise an InvalidBlockTypeException.
    If the dictionary contains neither a 'variable' nor 'output' block, raise a NoValidBlockTypeException.
    If the dictionary contains a 'variable' block, return (True, BlockType.variable).
    If the dictionary contains an 'output' block, return (True, BlockType.output).

    Args:
        file_content (Dict): The input dictionary.

    Returns:
        tuple[bool, BlockType]: A tuple containing a boolean value indicating if the dictionary has a valid block type, and the block type if it is valid.

    Raises:
        InvalidBlockTypeException: If the dictionary contains both a 'variable' and 'output' block.
        NoValidBlockTypeException: If the dictionary does not contain a 'variable' or 'output' block.
    """
    has_variable = "variable" in file_content
    has_output = "output" in file_content

    if has_variable and has_output:
        raise InvalidBlockTypeException(file_content)
    elif has_variable:
        return (True, BlockType.variable)
    elif has_output:
        return (True, BlockType.output)
    else:
        raise NoValidBlockTypeException(file_content)
