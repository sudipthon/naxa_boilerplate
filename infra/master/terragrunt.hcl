include "root" {
  path = find_in_parent_folders()
}

terraform {
  # Sourcing from here rn, updating to a release from https://github.com/hotosm/TM-Extractor/ later.
  // source = "${local.base_source_url}?ref=v1.0.0"
  source = ".//src"
}


locals {
  # Automatically load environment-level variables
  environment_vars  = read_terragrunt_config(find_in_parent_folders("terragrunt.hcl"))
  inputs  = read_terragrunt_config("inputs.hcl")

  # Extract the variables we need for easy access
  account_name      = local.environment_vars.locals.account_name
  aws_region        = local.environment_vars.locals.aws_region
  application       = local.environment_vars.locals.application
  team              = local.environment_vars.locals.team
  created_with      = local.environment_vars.locals.created_with
  owner             = local.environment_vars.locals.owner
  client            = local.environment_vars.locals.client
  cost              = local.environment_vars.locals.cost

  #custom
  environment       = "master"
}

generate "provider" {
  path = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
# Terraform provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.67.0"
    }
  }
}

provider "aws" {
  # region and profile is for the architecture
  region                   = "${local.aws_region}"
  profile                  = "default"

  default_tags {
    tags = {
      Environment  = "${local.environment}"
      Application  = "${local.application}"
      Team         = "${local.team}"
      Owner        = "${local.owner}"
      Created_with = "${local.created_with}"
      Cost         = "${local.cost}"
      Client       = "${local.client}"
    }
  }
}
EOF
}

inputs = merge(
  local.inputs.locals, local
  )
