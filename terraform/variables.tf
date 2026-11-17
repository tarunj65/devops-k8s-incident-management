variable "aws_region" {
  description = "AWS region for Kubernetes Infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "devops-k8s-incident-management"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}


variable "admin_cidr" {
  description = "Public IPv4 CIDR allowed to SSH into Kubernetes nodes"
  type        = string

  validation {
    condition     = can(cidrhost(var.admin_cidr, 0)) && endswith(var.admin_cidr, "/32")
    error_message = "admin_cidr must be a valid single-host IPv4 CIDR ending in /32"
  }
}


variable "control_plane_instance_type" {
  description = "EC2 instance type for Kubernetes control plane"
  type        = string
  default     = "t3.medium"
}


variable "worker_instance_type" {
  description = "EC2 instance type for Kubernetes worker"
  type        = string
  default     = "t3.medium"
}


variable "root_volume_size" {
  description = "Root EBS volume size in GiB"
  type        = number
  default     = 20
}


variable "ssh_public_key_path" {
  description = "Path to SSH public key"
  type        = string
  default     = "~/.ssh/devops-k8s-lab.pub"
}
