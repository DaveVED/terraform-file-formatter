from enum import Enum


class BlockType(Enum):
    """Enum class representing the types of blocks in a Terraform file."""

    output = "OUTPUT"
    variable = "VARIABLE"
