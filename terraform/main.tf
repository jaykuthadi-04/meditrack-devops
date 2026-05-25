terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "meditrack_rg" {
  name     = "meditrack-rg"
  location = "West US"
}

resource "azurerm_container_registry" "meditrack_acr" {
  name                = "mediatrackacr"
  resource_group_name = azurerm_resource_group.meditrack_rg.name
  location            = azurerm_resource_group.meditrack_rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_kubernetes_cluster" "meditrack_aks" {
  name                = "meditrack-aks"
  location            = azurerm_resource_group.meditrack_rg.location
  resource_group_name = azurerm_resource_group.meditrack_rg.name
  dns_prefix          = "meditrack"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2s_v3"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Learning"
    Project     = "MediTrack"
  }
}