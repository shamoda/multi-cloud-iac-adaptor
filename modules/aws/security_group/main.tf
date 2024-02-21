resource "aws_security_group" "security_group" {
  name        = var.name
  tags        = var.tags
}