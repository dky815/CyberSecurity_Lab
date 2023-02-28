resource "aws_instance" "ubuntu_public" {
  ami                           = aws_ami_copy.Ubuntu1804.id
  instance_type                 = "t2.micro"
  subnet_id                     = aws_subnet.public.id
  vpc_security_group_ids        = [aws_security_group.allow_ssh.id, aws_security_group.allow_tcp_8081.id, aws_security_group.allow_all_outgoing.id]
  associate_public_ip_address   = true
  key_name                      = "CYBERSECURITY_EC2_PUB"

  tags = {
    Name = "ubuntu_public"
  }
}

resource "aws_instance" "ubuntu_private" {
  ami                           = aws_ami_copy.Ubuntu1804.id
  instance_type                 = "t2.micro"
  subnet_id                     = aws_subnet.private.id
  vpc_security_group_ids        = [aws_security_group.allow_ssh.id, aws_security_group.allow_all_outgoing.id]
  associate_public_ip_address   = false
  key_name                      = "CYBERSECURITY_EC2_PUB"   

  tags = {
    Name = "ubuntu_private"
  }
}