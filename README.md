# terraform-file-writter
Python CLI provding terraform file manipulation (formating) functionality. 

## Functionality
This CLI allows your to.
- [x] Pass in a argument defining what type of file manipulation you would like. 
    - [x] `./tfw/main.py sort` - Sort a file in alphabetical (or reverse) order
- [x] Read in one ore more files and store them in a python readable `TerraformFile` object.
    - [x] `./tfw/main.py sort -file file1 file2` - User provided files
    - [x] `./tfw/main.py sort` - Serach for all `*.tf` files in the current working directory.

## Usage.

```
    # Sort user provided files.
    ./tfw/main.py sort -file test/files/easy-files/easy1.tf test/files/easy-files/easy2.tf

    # Sort all files in working directory.
    ./tfw/main.py sort
```
