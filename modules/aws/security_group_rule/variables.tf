variable "type" {
  description = "Type of security group rule"
  type        = string
}

variable "from_port" {
  description = "From port of security group rule"
  type        = number
}

variable "to_port" {
  description = "To port of security group rule"
  type        = number
}

variable "protocol" {
  description = "Protocol of security group rule"
  type        = string
}

variable "security_group_id" {
  description = "Security Group ID for security group rule"
  type        = string
}