# terraform-file-writter
Custom python CLI that allows you to create, manipulate, and format terrafrom `*.tf` files.

This sovles the issue, of no hasicorp python library to work with hcl files.

## Features

Following features exists.

- [ ] A CLI to read in a potential *three* flags.
    - [ ] `-f` flag to pass in *N* file paths, for `*.tf`.
    - [ ] `-a` flag to have us serach for all `*tf` in the working directory.
    - [ ]`-r` flag to sort the file content in reverse order.
- [ ] Ability format the provided `*.tf` file(s) content blocks in sorted alphabetical or reverse order. 
- [ ] Write the formated `*.tf` files to the original file destiation. Providng a sorted/formatted file.

* Right only `*tf` files with *all* `variable` or *all* `output` blocks are supported. Will add in other resource support later. *



## Usage.
Inovke cli with one of the following options.

```
    # Pass in a single file. 
    ./tfw/main.py -f test/files/input_easy.tf

    # Pass in multi files.
    ./tfw/main.py -f test/files/input_easy.tf test/files/input_medium.tf
```

Then you should see your provided files (or all files if using the `-a` flag.) formatted.

### Before Example

Before runnging ```./tfw/main.py -f test/files/input_easy.tf```

```hcl
    variable "carl" {
        type = string
        description = "Hellow Carl...."
    }

    variable "david" {
        type = number
        description = "Hellow David"
    }

    variable "adam" {
        type = bool
        description = "Hellow Adam"
    }

    variable "vincient" {
        type = list(string)
        description = ["Hellow", "World"]
    }
```

### After Example
Before runnging ```./tfw/main.py -f test/files/input_easy.tf```

```hcl
    variable "adam" {
        type = bool
        description = "Hellow Adam"
    }

    variable "carl" {
        type = string
        description = "Hellow Carl...."
    }

    variable "david" {
        type = number
        description = "Hellow David"
    }

    variable "vincient" {
        type = list(string)
        description = "['Hellow', 'World']"
    }
```
