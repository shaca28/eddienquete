# escolhendo a plataforma de serviço
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

# Escolhendo local do provedor
provider "aws" {
  profile = "default"
  region  = var.regiao_aws
}

# Criando maquina virtual
resource "aws_instance" "app_server" {
  ami           = "ami-04505e74c0741db8d"
  instance_type = var.instancia
  key_name = var.chave

  tags = {
    Name = "eddienquete-python"
  }
}

resource "aws_key_pair" "chaveSSH" {
  key_name = var.chave
  public_key = file("${var.chave}.pub")  
}

output "IP_publico" {
  value = aws_instance.app_server.public_ip  
}