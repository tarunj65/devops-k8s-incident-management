# --------------------------------
# Ubuntu 24.04 LTS AMI
# --------------------------------


data "aws_ssm_parameter" "ubuntu_ami" {
  name = "/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id"
}


# --------------------------------
# SSH Key Pair
# --------------------------------


resource "aws_key_pair" "k8s" {
  key_name_prefix = "devops-k8s-labs-"
  public_key      = file(pathexpand(var.ssh_public_key_path))

  tags = {
    Name = "${var.project_name}-ssh-key"
  }
}


# -------------------------------
# Kubernetes Control Plane
# -------------------------------


resource "aws_instance" "control_plane" {
  ami                    = data.aws_ssm_parameter.ubuntu_ami.value
  instance_type          = var.control_plane_instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.k8s_nodes.id]
  key_name               = aws_key_pair.k8s.key_name

  associate_public_ip_address = true

  root_block_device {
    volume_type           = "gp3"
    volume_size           = var.root_volume_size
    encrypted             = true
    delete_on_termination = true
  }

  metadata_options {
    http_tokens = "required"
  }

  tags = {
    Name = "${var.project_name}-control-plane"
    Role = "control-plane"
  }
}


# -------------------------------
# Kubernetes Worker Node
# -------------------------------


resource "aws_instance" "worker" {
  ami                    = data.aws_ssm_parameter.ubuntu_ami.value
  instance_type          = var.worker_instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.k8s_nodes.id]
  key_name               = aws_key_pair.k8s.key_name

  associate_public_ip_address = true

  root_block_device {
    volume_type           = "gp3"
    volume_size           = var.root_volume_size
    encrypted             = true
    delete_on_termination = true
  }

  metadata_options {
    http_tokens = "required"
  }

  tags = {
    Name = "${var.project_name}-worker"
    Role = "worker"
  }
}
