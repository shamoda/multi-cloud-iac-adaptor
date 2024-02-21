variable "name" {
  description = "Name of security group"
  type        = string
}

variable "tags" {
  description = "Resouce tags"
  type        = map
  default     = {}
}
