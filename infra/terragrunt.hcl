// export TERRAGRUNT_GIT_REPO_NAME=$(git remote -v | grep -m1 "" | awk {'print $2'} | xargs basename | sed -e s/.git//)

remote_state {
  backend = "s3"
  config = {
    region                   = "ap-south-1"
    key                      = "${local.application}/${get_path_from_repo_root()}/terraform.tfstate"
    bucket                   = "naxa-terraform-statefiles"
    dynamodb_table           = "naxa-terraform-locks"
    // shared_credentials_files = ["/Users/nischal/NAXA/naxa-terraform/.aws/credentials"]
    profile                  = "default"
    disable_bucket_update    = true
  }

  generate = {
    path        = "backend.tf"
    if_exists   = "overwrite_terragrunt"
  }
}

locals {
    application  = "naxa-backend-boilerplate"
    client       = "naxa-developers"
    cost         = "NAXA"
    team         = "DevOps"
    created_with = "NAXA-Terragrunt-CI"
    owner        = "NAXA"
    aws_region   = "ap-south-1"
    account_name = ""
}
