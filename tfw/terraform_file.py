import hcl2


class TerraformFile:
    def __init__(self, fp: str):
        self._fc = self._parse_terrafrom_file(fp)
        self._sorted = self._sort_terraform_blocks(self._fc, "variable")

    def _parse_terrafrom_file(self, fp: str) -> dict:
        dict = None
        with open(fp, "r") as file:
            dict = hcl2.load(file)
        return dict

    def _sort_terraform_blocks(self, fc: dict, ft: str) -> dict:
        if ft == "variable":
            variables = fc["variable"]
            sorted_ = sorted(variables, key=lambda d: list(d.keys())[0])
            return sorted_

        return {}

    def get_sorted_terraform_blocks(self) -> dict:
        return self._sorted
