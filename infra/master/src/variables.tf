variable "application" {
  type = string
}

variable "environment" {
  type = string
}

variable "create_iam_user" {
  type = bool
}

variable "bucket_username" {
  type = string
}

variable "create_public_folder" {
  type = bool
}

variable "public_folder_key" {
  type = string

}

variable "enable_tagged_deletion" {
  type = bool
}

variable "deletion_tag" {
  type = string
}

variable "exipiry_days_for_tagged_deletion" {
  type = number
}

variable "tagged_deletion_path_key" {
  type = string
}

variable "ec2_vpc_id" {
  type = string
}

variable "ec2_subnet_id" {
  type = string
}

variable "ec2_iam_instance_profile" {
  type    = string
  default = "NAXA-EC2-SSM-Role"
}

variable "create_ssh_key_pair" {
  type    = bool
  default = false
}

variable "ec2_root_vol_size" {
  type = string
}

variable "ec2_ebs_volumes" {
  type = list(object({
    size     = number
    type     = string
    device   = string
    vol_name = string
  }))
}

variable "ec2_sec_grp_ingress" {
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
    description = optional(string)
  }))
}

variable "ec2_sec_grp_egress" {
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
}
