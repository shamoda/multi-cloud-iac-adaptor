variable "name" {
  description = "Name of network security rule"
  type        = string
}

variable "priority" {
  description = "Priority of network security rule"
  type        = number
}

variable "direction" {
  description = "Direction of network security rule"
  type        = string
}

variable "access" {
  description = "Access rule of network security rule"
  type        = string
}

variable "protocol" {
  description = "Protocol of network security rule"
  type        = string
}

variable "resource_group_name" {
  description = "Resource Group Name for network security rule"
  type        = string
}

variable "network_security_group_name" {
  description = "Network security group of network security rule"
  type        = string
}
