import re


class TerraformFileWritter:
    def __init__(self, blocks: dict, fp: str):
        self._write_blocks(blocks, fp)

    def _format_block(self, name: str, attrs: dict) -> str:
        rex = attrs["type"][2:-1]
        output = 'variable "{}" {{\n    type = {}\n    description = "{}"\n}}'.format(
            name, rex, attrs["description"]
        )

        return output

    def _write_blocks(self, blocks: str, fp: str):
        with open("test/files/junk/temp.tf", "w") as f:
            f.truncate()

            count = 0
            for block in blocks:
                for name, attrs in block.items():
                    # format file and setup write command.
                    fmt = self._format_block(name, attrs)
                    cmd = f"{fmt}" if count == len(blocks) - 1 else f"{fmt}\n\n"
                    f.write(cmd)
                count = count + 1
