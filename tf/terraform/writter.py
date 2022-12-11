class TerraformFileWritter:
    def __init__(self):
        pass

    def _format_block(self, block_name: str, block_attributes: dict) -> str:
        # enhcnae for all var inputs.
        formatted_type = rex = block_attributes["type"][2:-1]
        output = 'variable "{}" {{\n    type = {}\n    description = "{}"\n}}'.format(
            block_name, formatted_type, block_attributes["description"]
        )

        return output

    def write(self, blocks: str, file_path: str):
        with open(file_path, "w") as f:
            f.truncate()

            count = 0
            for block in blocks:
                for name, attrs in block.items():
                    fmt = self._format_block(name, attrs)
                    cmd = f"{fmt}" if count == len(blocks) - 1 else f"{fmt}\n\n"
                    f.write(cmd)
                count = count + 1
