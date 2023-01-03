variable "adam" {
  type        = string
  default     = "Adam"
  description = "Hello Adam."
}

variable "bob" {
  type        = number
  default     = 35
  description = "Hello David."
}

variable "david" {
  type        = bool
  default     = false
  description = "Hello David."
}

variable "taylor" {
  type        = list(string)
  default     = ["T", "A", "Y", "L", "O", "R"]
  description = "Hellow Taylor"
}