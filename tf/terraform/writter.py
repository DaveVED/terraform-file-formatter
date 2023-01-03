class TerraformFileWritter:
    def __init__(self):
        pass

    def _format_block(self, block_name: str, block_attributes: dict) -> str:
        output = 'variable "{}" {{\n'.format(block_name)
        output += self._format_type(block_attributes)
        output += self._format_default(block_attributes)
        output += self._format_description(block_attributes)
        if "sensitive" in block_attributes:
            if isinstance(block_attributes["sensitive"], bool):
                output += '    sensitive = {}\n'.format(str(block_attributes["sensitive"]).lower())
            else:
                output += '    sensitive = {}\n'.format(block_attributes["sensitive"])
        output += "}"
        if "validation" in block_attributes:
            validation_block = 'validation {{\n    condition     = "{}"\n    error_message = "{}"\n}}'.format(
                block_attributes["validation"]["condition"], block_attributes["validation"]["error_message"]
            )
            output += "\n" + validation_block
        return output


    def _format_type(self, block_attributes: dict) -> str:
        if "type" in block_attributes and block_attributes["type"]:
            type_string = block_attributes["type"][2:-1]
            if type_string.startswith("object("):
                type_string = type_string[8:-1]
                type_string = type_string.replace("'", "")
                type_string = type_string.replace("${", "")
                type_string = type_string.replace("}", "")
                type_string = type_string.replace(": ", " = ")
                type_string = type_string.replace(",", "\n    ")
                type_string = "object({\n     " + type_string + "\n    })"
            elif type_string.startswith("list(object("):
                type_string = type_string[13:-1]
                type_string = type_string.replace("'", "")
                type_string = type_string.replace("${", "")
                type_string = type_string.replace("}", "")
                type_string = type_string.replace(": ", " = ")
                type_string = type_string.replace(",", "\n    ")
                type_string = type_string[:-1]
                type_string = "list(object({\n     " + type_string + "\n    }))"
            return '  type = {}\n'.format(type_string)
        return ""

    def _format_description(self, block_attributes: dict) -> str:
        if "description" in block_attributes and block_attributes["description"]:
            return '  description = "{}"\n'.format(block_attributes["description"])
        return ""

    def _format_default(self, block_attributes: dict) -> str:
        if "default" in block_attributes:
            if isinstance(block_attributes["default"], str):
                return '  default = "{}"\n'.format(block_attributes["default"])
            elif isinstance(block_attributes["default"], list) and all(isinstance(i, str) for i in block_attributes["default"]):
                return '  default = [{}]\n'.format(", ".join([f'"{i}"' for i in block_attributes["default"]]))
            elif isinstance(block_attributes["default"], bool):
                temp = "false"
                if block_attributes["default"]:
                    temp = "true"
                return '  default = {}\n'.format(temp)
            elif isinstance(block_attributes["default"], list) and all(isinstance(i, dict) for i in block_attributes["default"]):
                default_string = ""
                for obj in block_attributes["default"]:
                    obj_string = ""
                    for key, value in obj.items():
                        if isinstance(value, str):
                            obj_string += f"    {key} = \"{value}\"\n"
                        elif isinstance(value, bool):
                            obj_string += f"    {key} = {value}\n"
                        else:
                            obj_string += f"    {key} = {value}\n"
                    default_string += f"  {{\n{obj_string}      }},\n"
                return f"  default = [\n    {default_string}    ]\n"
            else:
                return '  default = {}\n'.format(repr(block_attributes["default"]))
        return ""


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
