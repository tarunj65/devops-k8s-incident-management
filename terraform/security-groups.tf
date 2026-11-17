resource "aws_security_group" "k8s_nodes" {
  name_prefix = "${var.project_name}-nodes-"
  description = "Security group for self-managed Kubernetes nodes"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-nodes-sg"
  }
}


# SSH access from your workstation only

resource "aws_vpc_security_group_ingress_rule" "ssh" {
  security_group_id = aws_security_group.k8s_nodes.id

  description = "SSH from admin workstation"
  cidr_ipv4   = var.admin_cidr
  from_port   = 22
  to_port     = 22
  ip_protocol = "tcp"
}


# Allow Kubernetes nodes to communicate with one another

resource "aws_vpc_security_group_ingress_rule" "internal" {
  security_group_id            = aws_security_group.k8s_nodes.id
  description                  = "Internal communication between Kubernetes nodes"
  referenced_security_group_id = aws_security_group.k8s_nodes.id
  ip_protocol                  = "-1"
}


# Permit outbound connections for package installation, container image pulls, and Kubernetes setup

resource "aws_vpc_security_group_egress_rule" "outbound" {
  security_group_id = aws_security_group.k8s_nodes.id
  description       = "Outbound IPv4 traffic"
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}
