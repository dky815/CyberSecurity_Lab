data "aws_ami" "ubuntu" {
#   executable_users = ["self"]
  most_recent      = true
#   name_regex       = "^myami-\\d{3}"
  owners           = ["amazon"]
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20220901"]
  }

#   filter {
#     name   = "root-device-type"
#     values = ["ebs"]
#   }

#   filter {
#     name   = "virtualization-type"
#     values = ["hvm"]
#   }
}

resource "aws_ami_copy" "Ubuntu1804" {
  name              = "Ubuntu1804"
  description       = "A copy of Ubuntu server 18.04 AMD 64"
  source_ami_id     = data.aws_ami.ubuntu.id
  source_ami_region = "us-east-1"

  tags = {
    Name = "Ubuntu1804"
  }
}