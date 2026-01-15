variable "location" {
  description = "Région Azure pour le déploiement"
  default     = "francecentral" 
}

variable "prefix" {
  description = "Préfixe pour le nommage des ressources"
  default     = "td-devops"
}

variable "admin_username" {
  description = "Nom d'utilisateur pour la VM"
  default     = "azureuser"
}