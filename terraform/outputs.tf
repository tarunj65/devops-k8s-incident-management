output "vpc_id" {
  description = "ID of the Kubernetes VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = aws_internet_gateway.main.id
}

output "availability_zone" {
  description = "Availability zone of the public subnet"
  value       = aws_subnet.public.availability_zone
}

output "k8s_security_group_id" {
  description = "Security group ID for Kubernetes EC2 nodes"
  value       = aws_security_group.k8s_nodes.id
}

output "control_plane_public_ip" {
  description = "Public IP of Kubernetes control plane"
  value       = aws_instance.control_plane.public_ip
}

output "control_plane_private_ip" {
  description = "Private IP of Kubernetes control plane"
  value       = aws_instance.control_plane.private_ip
}

output "worker_public_ip" {
  description = "Public IP of Kubernetes worker"
  value       = aws_instance.worker.public_ip
}

output "worker_private_ip" {
  description = "Private IP of Kubernetes worker"
  value       = aws_instance.worker.private_ip
}

output "ssh_key_name" {
  description = "AWS EC2 SSH key pair name"
  value       = aws_key_pair.k8s.key_name
}
