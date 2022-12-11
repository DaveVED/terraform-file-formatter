from enum import Enum


class BlockType(Enum):
    """Enum class representing the types of blocks in a Terraform file."""

    output = "OUTPUT"
    variable = "VARIABLE"


class Block:
    def __init__(self, block_name, block_attrs):
        self._block_name = block_name
        self._block_attributes = block_attrs

    @property
    def name(self) -> str:
        return self._block_name

    @property
    def attrs(self) -> str:
        return self._block_attributes
