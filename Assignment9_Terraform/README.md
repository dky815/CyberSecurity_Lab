## Terraform

In this assignment you will be introduced to Terraform, a tool for building, changing, and versioning infrastructure safely and efficiently. You are going to create the same infrastructure as in the previous assignment, but this time using Terraform.

### Setup

You need to have installed the AWS CLI from [https://aws.amazon.com/cli/![]()Links to an external site.](https://aws.amazon.com/cli/). After installing it you need to edit or create the credentials and config files. The files are located at ~/.aws/ on Linux, macOS, or Unix, or at C:\Users\USERNAME\.aws\ on Windows.

If you are using the AWS Educate Starter Account option you should find credentials by visiting [https://labs.vocareum.com/main/main.php![]()Links to an external site.](https://labs.vocareum.com/main/main.php) and clicking on Account Details > AWS CLI and copy the credentials. Your credentials file should be in the following format

```
[default]
aws_access_key_id=ASIAX6FEVCKT6CQX7
aws_secret_access_key=UoB20G4jw/He5/oG773qp94oJXtPk2cr
aws_session_token=FQoGZXIvYXdzEGQaDMz/k6QeUDbPOxlEFSL6AoRZzonaoRzncHjCT5V3Ktl9kufJ+Z116q+xf2Hzh4Xmy0Q72eHGaWiMps1BW4dqKAulvTX/yL7RwGioC0neEP8TehbQyR6XY3z0yB/UT+p7XVXDC4J7SsPZyG7Xpv+trF+QK7Rhghc/9BDpLSF5y1a3NqVlBcCsA8Aerxbvb8LOOPqWAsavfQEOWWu6xZ8bBmaRadE+jWMs3eXqizrdJq/Zs2u6pJeSDRD3x8DDE8Emxmxk8mUjIm14PohegRZeWD+JS2TfAk0Pq1Zb1hufTBXAISVOp9E8M1vG1YBXIivDArZVGZVkzVd0tQUUpHIaxs4obOBAkkBkp119Y8S8QhfoM0ap2SduJ7sdN04pHqMOTt4C3M2I9jxapTFmr5ow/xMoS15/Gz5+OStHfWDhR+gbchnlYfxUWb2wqXgsLTSDyJiL6IbNvGshL4aYZDiCdlHEwNVMctTCakOjPg+7evFxaxZG2MbXoHi3Dw/qxDNTcCiAzI7qBQ==
```

If you have created a separate account and linked it to the AWS Educate Starter account then you should have downloaded the credentials.csv upon the user creation. If not then go to the IAM console and generate a new pair of keys. You should create the credentials file using the following content

```
[default]
aws_access_key_id = "your key"
aws_secret_access_key= "your key"
```

Next, you should create the config file in the same directory using the following contents:

```
[default]
region=us-east-1
```

After successfully setting up the AWS CLI you should install Terraform from [https://www.terraform.io![]()Links to an external site.](https://www.terraform.io/).

Next, create a folder for your Terraform files and put the files provided [here ](https://canvas.sfu.ca/courses/71722/files/20321953?wrap=1 "terraform.zip")[ **Download here **](https://canvas.sfu.ca/courses/71722/files/20321953/download?download_frd=1)in the folder. Navigate to the folder and run the commands:

```
terraform init
terraform apply (use this command to “upload” any changes to your “code”)
```

This will create a simple VPC with a subnet.

**Task 1 (11%)** : Modify the file `subnets.tf` inside the provided .zip file to create a private subnet along with the existing public subnet.

Hint: The command `terraform apply` "uploads" new changes to AWS. Use this command to check if your "code" works properly.

**Task 2 (11%)** : Create a file named `gateways.tf` and place the “code” needed to create an internet gateway that is associated with the VPC terraform creates.

**Task 3 (11%)** : Create a file named route-tables.tf and write the “code” needed to create the proper route-table for the internet-gateway as well as the subnet association for the public subnet.

For the remaining tasks the following links may be helpful ([gateway![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway), [route table![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table), [route table association![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association)).

**Task 4 (11%)** : Create a file called `security-groups.tf` and write the “code” required to create security group(s) that allows inbound traffic for SSH and for TCP for port 8081 and all outgoing traffic.

**HINT:** You should probably consider not putting all of the rules inside one resource. It is a better idea to separate the groups so you can assign a subset of the groups to a public EC2 and another subset to a private EC2 without having groups with repeating rules. This means that instead of creating one group with all the rules, you can create one group for each rule.

**Task 5 (11%)** : Create a file called `ami.tf` and place the required “code” in order to create an image based on Ubuntu server 18.04 AMD 64. Your code should create an AMI from ubuntu's AMI.

**HINT** : These links may be helpful [[Link, ![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ami "Link")[Link![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ami_copy "Link")]. Also avoid using the following because it is pretty complicated and not what you need [Link![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ami "Link")

**Task 6 (11%)** : Create a file called `ec2.tf` and write the “code” to create an EC2 instance based on the AMI from **Task 5** inside the **public subnet** the provided code creates. The new public instance adopts all the rules that are mentioned in  **Task 4** . You should also assign a key to this instance so that in later tasks you can access it via SSH. Also set the option `associate_public_ip_address = true`.

**HINT 1:** If you find yourself creating and destroying your setup many times, consider using the Ubuntu's AMI directly instead and comment out the code from  **Task 5** . This will save you time for your debugging purposes.

**HINT 2:** Before applying the changes you should probably create SSH keys for your machine so that you can connect to it later. You can choose to do it in either of the following ways (follow one way not both).

**Way 1** : In order to create key pairs go to the EC2 Menu > Key Pairs (Under Network & Security) [Link![]()Links to an external site.](https://console.aws.amazon.com/ec2/#KeyPairs: "Link"). Create a new key pair, give it the name CYBERSECURITY_EC2_PUB and download the private key to your computer. In order to inform AWS that you are going to use this key pair to SSH to the instance add this to your resource:

```
key_name = "CYBERSECURITY_EC2_PUB"
```

More info about this in the following link [Link![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#key_name "Link")

**Way 2:** If you want to create the keys locally in your machine create a key pair with the following command

```
ssh-keygen
....
```

Use the following terraform resource to create the keys in AWS [Link![]()Links to an external site.](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/key_pair "Link")

Specify the name as "CYBERSECURITY_EC2_PUB" and the public_key field to be the contents of your public key (.pub file)

Associate the key to your instance by setting a key_name field inside your "aws_instance" resource like this:

```
key_name = "CYBERSECURITY_EC2_PUB"
```

**Task 7 (11%)** : In the `ec2.tf` file you created in **Task 6** write the “code” to create an EC2 instance based on the AMI you created in  **Task 5** . This new instance should be inside the **private subnet** you created in  **Task 1** . It also should have outgoing traffic to everywhere and be accessible through SSH . Again you have to specify a key so that you can SSH to that machine later (follow the same steps as in the  **Task 6's HINT** ). Also set the `associate_public_ip_address = fase.`

**HINT:** You can use **some** of the security groups you created in **Task 4** for that, just keep in mind not to allow any inbound traffic other than SSH. In the case you created one security group in  **Task 4** , you will probably need to create and attach another security group for this EC2 instance.

**Task 8 (11%)** : If you have created the EC2 instances properly you should be able to SSH into the **EC2 private instance** created in **Task 7** through the **EC2 public instance** created in  **Task 6** . After you SSH into the private instance try to ping [www.google.com![]()Links to an external site.](http://www.google.com/). It should not work. If you try the same from the **EC2 public instance** you will see that you can actually ping [www.google.com![]()Links to an external site.](http://www.google.com/). Explain briefly why on the **EC2 private instance** you cannot ping google whereas on the  **EC2 public instance you can** .

**HINT: **You can follow the following steps if you don't know how to SSH to the private instance

**Way 1 (Not the best practive but it will not affect your grade):**

Copy the ssh **private** key you provided for the EC2 private instance in the EC2 public instance's home directory. To do that type the command:

```
scp -o 'IdentitiesOnly yes' -i CYBERSECURITY_EC2_PUB CYBERSECURITY_EC2_PRIV ubuntu@<PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE>:~/
```

* <PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE> is the **public** ip the **EC2 public instance** gets assigned
* CYBERSECURITY_EC2_PUB is the path to the file of the **private key** of the **EC2 public instance**
* CYBERSECURITY_EC2_PRIV is the path to the file of the **private key** of the **EC2 private instance**

Then ssh to the public instance by typing:

```
ssh -o 'IdentitiesOnly yes' -i CYBERSECURITY_EC2_PUB ubuntu@<PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE>
```

* <PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE> is the **public ip** the **EC2 public instance** gets assigned.
* CYBERSECURITY_EC2_PUB is the path to the file of the **private key** of the **EC2 public instance**

Now you should be SSHed into the  **EC2 public instance** . Check that the **private key** of the **EC2 private instance** is inside the home folder by typing

```
ls -l  ~
```

Assuming the key is there you need to SSH to the  **EC2 private instance** . Type:

```
ssh -o 'IdentitiesOnly yes' -i CYBERSECURITY_EC2_PRIV ubuntu@10.0.2.50
```

* CYBERSECURITY_EC2_PRIV is the path to the file of the **private key** of the **EC2 private instance** **inside the EC2 public instance's directory** (this should be the home directory)
* 10.0.2.50 is the IP of the **EC2 private instance**

**Way 2 (Best practice):**

Use the following command to directly ssh to the **EC2 private instance** from your computer by going through the  **EC2 public instance** .

```
ssh -o ProxyCommand="ssh -o 'IdentitiesOnly yes' -i CYBERSECURITY_EC2_PUB -W %h:%p ubuntu@<PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE>" -o 'IdentitiesOnly yes' -i CYBERSECURITY_EC2_PRIV ubuntu@10.0.2.50
```

* <PUBLIC_IP_OF_EC2_PUBLIC_INSTANCE> is the **public ip** the **EC2 public instance** gets assigned.
* CYBERSECURITY_EC2_PUB is the file path of the **private key** of the **EC2 public instance**
* CYBERSECURITY_EC2_PRIV is the file path of the **private key** of the **EC2 private instance**

If you used the same key in both instances, just specify the same file for both arguments in the command.

**Task 9 (12%)** : What would you change in your “code” in order to let the **EC2 private instance** to connect to the Internet (please consider using the best practices since this is an instance in a private subnet)?
