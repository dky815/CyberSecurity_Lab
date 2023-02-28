resource "aws_route_table" "routetable" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "routetable"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.routetable.id
}

# resource "aws_route_table_association" "b" {
#   gateway_id     = aws_internet_gateway.gw.id
#   route_table_id = aws_route_table.routetable.id
# }

# route table with target as NAT gateway
resource "aws_route_table" "NAT_route_table" {
  depends_on = [
    aws_vpc.main,
    aws_nat_gateway.nat_gateway,
  ]

  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.nat_gateway.id
  }

  tags = {
    Name = "NAT-route-table"
  }
}

# associate route table to private subnet
resource "aws_route_table_association" "associate_routetable_to_private_subnet" {
  depends_on = [
    aws_subnet.private,
    aws_route_table.NAT_route_table,
  ]
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.NAT_route_table.id
}