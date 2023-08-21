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

variable "source_port_range" {
  description = "Source port range of network security rule"
  type        = string
}

variable "destination_port_range" {
  description = "Destination port range of network security rule"
  type        = string
}

variable "source_address_prefix" {
  description = "Source address prefix of network security rule"
  type        = string
}

variable "destination_address_prefix" {
  description = "Destination address prefix of network security rule"
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
