module "s3" {
  #just local path for development/testing
  # source = "/Users/nischal/NAXA/naxa-terraform/modules//s3"

  source                           = "git::https://github.com/naxa-developers/naxa-terraform-infra-modules.git//s3?ref=v0.4.3"
  application                      = var.application
  environment                      = var.environment
  create_iam_user                  = var.create_iam_user
  bucket_username                  = var.bucket_username
  create_public_folder             = var.create_public_folder
  public_folder_key                = var.public_folder_key
  enable_tagged_deletion           = var.enable_tagged_deletion
  deletion_tag                     = var.deletion_tag
  exipiry_days_for_tagged_deletion = var.exipiry_days_for_tagged_deletion
  tagged_deletion_path_key         = var.tagged_deletion_path_key
}

module "ec2" {
  # source = "/Users/nischal/NAXA/naxa-terraform/modules//ec2"

  source                   = "git::https://github.com/naxa-developers/naxa-terraform-infra-modules.git//ec2?ref=v0.4.3"
  application              = var.application
  environment              = var.environment
  vpc_id                   = var.ec2_vpc_id
  ec2_subnet_id            = var.ec2_subnet_id
  create_ssh_key_pair      = var.create_ssh_key_pair
  ec2_iam_instance_profile = var.ec2_iam_instance_profile
  ec2_root_vol_size        = var.ec2_root_vol_size
  ec2_ebs_volumes          = var.ec2_ebs_volumes
  ec2_sec_grp_ingress      = var.ec2_sec_grp_ingress
  ec2_sec_grp_egress       = var.ec2_sec_grp_egress
}

module "ecr" {
  source                   = "git::https://github.com/naxa-developers/naxa-terraform-infra-modules.git//ecr?ref=v0.4.5"
  application              = var.application
  environment              = var.environment
}
