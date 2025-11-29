variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "insert-aws-region-here"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "insert-instance-type-here"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "insert-ami-id-here"
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
  default     = "insert-ssh-key-name-here"
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "insert-pypi-server-name-here"
}