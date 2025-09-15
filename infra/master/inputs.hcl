locals {
  // Custom variables below

  // S3
  // bucket_name = "naxa-backend-boilerplate-tg-variables-example-bucket"  # this overrides default bucket name
  create_iam_user = true
  bucket_username = null
  create_public_folder = true
  public_folder_key = "public/"
  enable_tagged_deletion = true
  deletion_tag = "deleted"
  exipiry_days_for_tagged_deletion = 7
  tagged_deletion_path_key = "/"


  // EC2
  ec2_vpc_id               = "vpc-0c6185319b9dca8d1" # naxa internal vpc
  ec2_subnet_id            = "subnet-0ba037da13090c1e7"  # naxa internal vpc public subnet 0
  ec2_iam_instance_profile = "NAXA-EC2-SSM-Role"  # SSM Role for SSM login. Better dont change if on NAXA account
  create_ssh_key_pair      = false # keep if false. use ssm login for security. change to true if you want to generate key pair. Adjust actions or run locally
  ec2_root_vol_size        = "15"

  // EBS Volume
  ec2_ebs_volumes = [
    {
      size                   = 20      # Size
      type                   = "gp3"   # Type
      device                 = "/dev/sdb" # Device Name
      vol_name               = "docker-volume" # Volume name
    }
  ]

  // Security Group Rules
  ec2_sec_grp_ingress = [
    {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "allow for ssh"
    },
    {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "allow for http"
    },
    {
      from_port   = 443
      to_port     = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "allow for https"
    },
  ]

  ec2_sec_grp_egress = [
    {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}
