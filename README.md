# terraform-formatter
Python CLI provding terraform file manipulation (formating) functionality. Allowing you to format and write valid terraform files using `python`. Something that is typically only achievable in `go`. 

If you just just want to use the code to format and write a terraform file without the cli, you can check out the `./tf/terraform/writter.tf` file the `_format_block` handles the magic. 

* currently only supports, `*.tf` files with variable blocks.

## Functionality
This CLI allows your to.
- [x] Pass in a argument defining what type of file manipulation you would like. 
    - [x] `./tfw/main.py sort` - Sort a file in alphabetical (or reverse) order.
- [x] Read in one ore more files and store them in a python readable `TerraformFile` object.
    - [x] `./tfw/main.py sort -file file1 file2` - User provided files
- [x] Validates all files passed in for formatting are valid `*.tf` files.
- [x] Validaets that the `*.tf` file are valid in regards to our supported blocks. 
    - [x] variable blocks
    - [ ] output blocks
- [x] Sorts the files in alphabetical (or reverse).
- [x] Writes (overwrites) the file in the originial destination.
- [x] Support for `variable.tf` files that have our supported blocksblocks. And support for `all` variable block types. 

## Usage.

```
    # Sort user provided files.
    ./tf/main.py sort -file test/files/input-files/medium1.tf
    ./tf/main.py sort -file test/files/easy-files/medium1.tf test/files/input-files/easy3.tf
```

Validate your files with this usage, but checking the same file you passed in, and ensuring it's formating correctly.

Here is an example. Using the following command.
```
./tf/main.py sort -file test/files/input-files/medium1.tf
```
### Before File.
```hcl
    variable "bob" {
    type = number
    default = 35
    description = "Hello David."
    }

    variable "adam" {
    type = string
    default = "Adam"
    description = "Hello Adam."
    }

    variable "david" {
    type = bool
    default = false
    description = "Hello David."
    }

    variable "taylor" {
    type = list(string)
    default = ["T", "A", "Y", "L", "O", "R"]
    description = "Hellow Taylor"
    }
```

### After File.
```hcl
    variable "adam" {
    type = string
    default = "Adam"
    description = "Hello Adam."
    }

    variable "bob" {
    type = number
    default = 35
    description = "Hello David."
    }

    variable "david" {
    type = bool
    default = false
    description = "Hello David."
    }

    variable "taylor" {
    type = list(string)
    default = ["T", "A", "Y", "L", "O", "R"]
    description = "Hellow Taylor"
    }
```

## Testing
You can run a bulk test on a vast range of files, by running the test shell script. Which will run the program in debug mode. Once the test script is done you can validate all filles, in ```test/files/output-files```. But the script it's self validates the files, agasint the correct file formats found in ```test/files/correct-outut-files```. If no error arsie, program is behaving as expected.

```
% ./test/test.sh
Testing sorting easy files...
2023-01-02 21:49:11,127 - logger - DEBUG - This is a debug message
2023-01-02 21:49:11,127 - logger - DEBUG - Formating file test/files/input-files/easy1.tf
2023-01-02 21:49:11,129 - logger - DEBUG - Writing output file to test/files/output-files/easy1.tf
2023-01-02 21:49:11,188 - logger - DEBUG - This is a debug message
2023-01-02 21:49:11,188 - logger - DEBUG - Formating file test/files/input-files/easy2.tf
2023-01-02 21:49:11,190 - logger - DEBUG - Writing output file to test/files/output-files/easy2.tf
2023-01-02 21:49:11,247 - logger - DEBUG - This is a debug message
2023-01-02 21:49:11,247 - logger - DEBUG - Formating file test/files/input-files/easy3.tf
2023-01-02 21:49:11,249 - logger - DEBUG - Writing output file to test/files/output-files/easy3.tf

Testing sorting medium files...
2023-01-02 21:49:11,306 - logger - DEBUG - This is a debug message
2023-01-02 21:49:11,306 - logger - DEBUG - Formating file test/files/input-files/medium1.tf
2023-01-02 21:49:11,308 - logger - DEBUG - Writing output file to test/files/output-files/medium1.tf
2023-01-02 21:49:11,364 - logger - DEBUG - This is a debug message
2023-01-02 21:49:11,364 - logger - DEBUG - Formating file test/files/input-files/medium2.tf
2023-01-02 21:49:11,366 - logger - DEBUG - Writing output file to test/files/output-files/medium2.tf

```