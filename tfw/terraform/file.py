import hcl2


class TerraformFile:
    def __init__(self, file_path: str):
        self._blocks = self._parse_terrafrom_file(file_path)
        self._file_path = file_path

    def _parse_terrafrom_file(self, file_path: str) -> dict:
        """Parse a Terraform file and return its contents as a dictionary.

        Args:
            fp (str): The path to the Terraform file.

        Returns:
            dict: A dictionary containing the parsed contents of the Terraform file.
        """
        with open(file_path, "r") as file:
            return hcl2.load(file)

    def sort(self, blocks: dict, resource_type: str) -> dict:
        if resource_type == "variable":
            variables = blocks["variable"]
            sorted_ = sorted(variables, key=lambda d: list(d.keys())[0])
            return sorted_

        return {}

    @property
    def blocks(self) -> dict:
        return self._blocks

    @property
    def file_path(self) -> str:
        """Return the path to the Terraform file.

        Returns:
            str: The path to the Terraform file.
        """
        return self._file_path

    @property
    def file_name(self) -> str:
        return self._file_path.split("/")[-1]
