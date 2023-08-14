resource "azurerm_network_security_rule" "example" {
  name                        = var.name
  priority                    = var.priority
  direction                   = var.direction
  access                      = var.access
  protocol                    = var.protocol
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}