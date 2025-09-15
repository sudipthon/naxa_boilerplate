# CREATE S3 Bucket
# resource "aws_s3_bucket" "s3_bucket" {
#   bucket = "demo-extra-resource-s3-bucket"
#   tags = {
#     Name = "demo-extra-resource-s3-bucket"
#   }
# }


# resource "aws_db_subnet_group" "db_subnet_grp" {
#   name        = "TEST-test-db-subnetgrp"
#   description = "Subnet group for databases upgrade test"
#   subnet_ids  = ["subnet-0e97be876038d55fe", "subnet-0d9f500e761ed89d5"]
#   tags = {
#     Name = "TEST-test-db-subnetgrp"
#   }
# }


# # PostgreSQL
# resource "aws_db_instance" "postgresql_cluster" {
#   identifier                 = "TEST-update-testing-db-postgresql"
#   allocated_storage          = 10
#   max_allocated_storage      = 30
#   engine                     = "postgres"
#   engine_version             = "13.13" # The new version is 14.6-R1 - Please Mahesh double check
#   auto_minor_version_upgrade = false
#   instance_class             = "db.t3.2xlarge"
#   db_name                    = "dbadmin"
#   username                   = "dbadmin"
#   password                   = "abvschfjajksdlnabsjhkd"
#   skip_final_snapshot        = true
#   apply_immediately          = true
#   deletion_protection        = false
#   publicly_accessible        = true
#   delete_automated_backups   = false
#   backup_retention_period    = 3
#   backup_window              = "20:30-21:30"
#   db_subnet_group_name       = aws_db_subnet_group.db_subnet_grp.name
#   vpc_security_group_ids     = ["sg-0abcf5519fa2e9de1"]
#   enabled_cloudwatch_logs_exports = [
#     "postgresql",
#   ]
#   tags = {
#     Name = "TEST-update-testing-db-postgresql"
#   }
#   allow_major_version_upgrade = true
# }
