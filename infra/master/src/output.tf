output "ec2_instance_id" {
  value = module.ec2.ec2_instance_id
}

output "ec2_instance_ip" {
  value = module.ec2.ec2_instance_ip
}

output "help" {
  value = "You can access VM via `aws ssm start-session --target ${module.ec2.ec2_instance_id}` "
}

output "ecr_name" {
  value = module.ecr.ecr_repository_name
}
