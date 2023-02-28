# Hack The Box

In this task, you will perform penetration testing as a group on a vulnerable machine of your choice hosted on the [Hack The Box **Links to an external site.**](https://www.hackthebox.eu/)(HTB) platform. HTB is a massive, online cybersecurity training platform, allowing individuals, companies, universities, and all kinds of organizations around the world to level up their hacking skills. The provided services vary from but are not restricted to:

* Challenges: CTF targeted challenges to level up and learn useful skills for a variety of topics such as web, crypto, hardware, OSINT and so on
* Fortresses: CTF challenges designed by companies
* Endgames: Advanced labs simulating real-world infrastructure and exploit scenarios, with multiple hosts and various attack paths
* Machines: Single machines to be exploited and hacked. There is no need to perform lateral movement with multiple hosts.
* Starting Point: Free Machines that are marked as "Very Easy" to start and evaluate your hacking skills.
* Academy: Tutorials and guides on various tools and techniques to learn by example

#### Machine Selection

The main focus of this task is  *Machines* . To complete this task you need to pick one of the lab machines in HTB to perform penetration testing, or in the HTB terminology, to pawn it.

* You work in a group of three students.
* Let the teaching team know your HBT account ID to add you to the *SFU dedicated labs*: [https://piazza.com/class/l6u4fqaaq5z5ot/post/61**Links to an external site.**](https://piazza.com/class/l6u4fqaaq5z5ot/post/61)
* [Here](https://canvas.sfu.ca/courses/71722/pages/machines) you can find the list of available machines in the SFU dedicated labs along with the corresponding difficulty and the operating system.
* Two groups cannot select the same Machine.
* When you select one of these machines for the HBT task we make it available for your group, which is a different environment than the provided links and you can find it on HTB > Lab > Dedicated Lab.
* Note that the links provided in the machines [list](https://canvas.sfu.ca/courses/71722/pages/machines) will not let you spawn a machine if it is retired unless you are a VIP, but will give you an overview of the machine.
* If a link in the machines list is not working just search the name of the machine on Google or search it in Hack The Box and you will find it.
* You will have free access to *SFU dedicated labs *for six months.
* Groups that pawn a medium machine will have up to 2% extra credit.

#### Report

You are expected to write a report of up to five pages and present your findings to the class. You need to document each step you take in the procedure of getting the user flag as well as the root flag. This means that you need to report the tools you used, the commands and their outputs as well as relevant screenshots as proof.

* If the output of using a tool is too big you do not report the whole output but only the relevant part that has the essential information.
* You need to explain how the exploits you used work, regardless if you created them or found them on the internet.
* If you use an exploit you found on the internet, provide a link to the used source.
* If you make a modification to an exploit, provide its source code and highlight the modifications you made.
* When you obtain the user flag use the following commands and take a screenshot of their output (you can split it into multiple commands if necessary)

```
*nix: cat user.txt && whoami && hostname && ifconfig
 Windows: type user.txt && whoami && hostname && ipconfig
```

* When you obtain the root flag use the following commands and take a screenshot of their output (you can split it in multiple commands if necessary)

```
*nix: cat root.txt && whoami && hostname && ifconfig
 Windows: type user.txt && whoami && hostname && ipconfig
```

You can check section 3 and below of a sample report from PWK's (Offensive Security ) report to get an idea how a penetration testing report looks like:

[https://www.offensive-security.com/pwk-online/PWK-Example-Report-v1.pdf**Links to an external site.**](https://www.offensive-security.com/pwk-online/PWK-Example-Report-v1.pdf)

It is basically a set of instructions along with an explanation (where needed) on how somebody else can get access to the machine by following your report.

Signing up in Hack The Box

The normal sign up procedure in HTB requires you to provide credentials but also solve a simple challenge. Although the solution to the challenge can be found on the Internet, it is recommended that you solve it on your own. After signing up you will have access to the aforementioned features and more.

#### Pawning a Machine

The procedure of pawning a machine requires you to get user access and root/administrator access in the machine of your choice. To prove that you got access you have to capture a flag located in a file inside a regular user and the root/administrator. That is:

* Windows
  * user: C:\Users\SomeUsername\Desktop\user.txt
  * root: C:\Users\Administrator\Desktop\root.txt
* Linux, Unix etc
  * user: /home/someusername/user.txt
  * root: /root/root.txt

The username of the regular user is different for each machine, the username of the root/administrator is standard. After obtaining each flag you need to input it in the appropriate Submit Flag section in HBT to obtain points.

#### Hacking Procedure

To start the hacking process you need to either join or spawn the machine of your choice. This will give you the IP of the machine. Also you will have to download the VPN configuration for the lab and establish a VPN connection to the HTB servers. If you don't do it, you will not have access to the machine. You can try pinging the machine's IP to test if you can reach it or not.

The provided machines are usually web servers that host a vulnerable web service which you can exploit.

The procedure in order to fully own root access to a machine usually but not necessarily consists of the following steps:

1. Reconnaissance/Target identification: In this step you need to identify what type of services are running on the machine you chose. If the machine runs a web server on some port you should explore the website for vulnerabilities. Useful tools and actions for this step
   * Nmap: To detect open ports, services and their version
   * Nikto: Web scanner that performs automated tests
   * Burp Suite: For monitoring and altering requests made to the server
   * smbwalk: For samba services
   * snmpwalk & snmp (perl) to perform scans for the snmp protocol
   * sqlmap: For sql injection vulnerabilities
   * ffuf & gobuster: For fuzzing and scanning directories
   * View Source Code & Developer tools of your browser: Sometimes there is useful information hidden in there
2. Foothold: In this step you might have already gained access to a login page or an admin panel. But have not yet gained access to the server. You need to identify the vulnerability that will allow you remote code execution in order to get some kind of a shell. That shell might be a non-interactive/persistent shell, or a normal reverse shell (don't try bind shell they won't work). Useful tools for this step might be:
   * metasploit: exploits
   * searchsploit (exploitdb): exploits
   * google
   * nc (netcat) & socat: reverse shells
   * [Payloads All The things **Links to an external site.**](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md): Cheatsheet with reverse shells and payloads of various kinds (they need slight modification with your IP etc)
3. Enumeration: After you get a foothold the process of enumeration begins (the first step can also be called enumeration). In this step, you may already have user access and read the user flag, so you can skip to the next step. However, this is rarely the case. In this step, you need to perform enumeration steps in order to find vulnerabilities and misconfigurations in the server. For that purpose you can search for
   * Any hidden services running that are not reachable from outside. You can use tools such as [chisel **Links to an external site.**](https://github.com/jpillora/chisel)to create a tunnel to your machine to try and exploit it locally.
   * Readable configurations and passwords for databases and users
   * Using john (the ripper) locally to potentially crack any password hash found in any database, MySql for example
4. Privilege Escalation: Assuming you have the user flag, the next step is to get the root flag. You will need to find a method to escalate your privileges to a root/administrator. If you have full user access and ssh is running on the server you may want to establish an SSH connection to the server for easier navigation. Useful tools for privilege escalation are:
   * [PEASS-ng **Links to an external site.**](https://github.com/carlospolop/PEASS-ng): A privilege escalation automated script that scans for common vulnerabilities
     * (Note you probably want to avoid very common vulnerabilities such as the sudo vulnerability)
   * WinEnum and LinEnum scripts are also all over github and can be used to gather extra information in the case that PEASS-ng was not enough
   * pspy (Linux only): To enumerate and snoop on running processes
   * [gtfobins **Links to an external site.**](https://gtfobins.github.io/): A list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.
   * internet: Gather knowledge and search your findings

#### Notes

* When using HTB it is strongly recommended that you use a Virtual Machine without any shared folders with the host machine to connect and perform any task. Connecting through VPN on a non-virtual machine to the HTB servers is not recommended. Although it is strictly prohibited and protected by HTB you need to remember that the place is full of hackers. Better to be safe than sorry!
* You can use your Virtual Machine/OS of your choice. It is strongly recommended that you use Linux. Here are some recommendations:
* * Kali Linux: Comes preinstalled with a variety of tools
  * Parrot Linux: Comes preinstalled with a variety of tools
  * Debian Linux: You need to install the tools on your own
  * BlackArch Linux: An Arch Linux based distribution like Kali and Parrot. Not recommended, unless you know your way around Arch and its configurations.
* If the machine you chose is an active machine and not a retired one, you can join it or create a new instance, depending on your account status. In the case you join, there will be other people trying to hack the same machine as you. Please do not try to disrupt other users, patch vulnerabilities or just remove crucial files (rm -rf /). Occasionally users do that and people vote on server reset in which case the server resets to its original state, you lose any reverse shell you may have and any change you may have made in the server and you may have to retake some steps if you lose access.
* In the case you require help, you may ask the TAs. There is also the [Hack the Box Forum **Links to an external site.**](https://forum.hackthebox.eu/)with official discussions for each machine and you can use the hints provided in the corresponding thread, however, you have to mention this point and how these hints helped you. You should not solve the entire machine using hints from other users.
* Furthermore, there are writeups/tutorials online on how to solve machines. It is strongly recommended not to use them. However if you find yourself at a dead end after spending a considerable amount of time, you may use them to proceed to the next step from which you will have to start searching on your own. You have to mention if you used a tutorial and which one. Do not use the whole tutorial to solve the machine.
* You can warm up by
* * Solving some challenges
  * Trying the Starting Point track which provides a series of "Very Easy" machines to train on: Note that the machines in this track are sequential and you need to solve one to proceed. You may have to use some flags/passwords/credentials from a previous machine to a next one
* If a command you found on the internet does not work you may have to adapt it, change it a bit or even try it on your machine if possible, before trying it as a payload or an exploit.
* Finally, the most important note is to use the internet to research anything that you do not understand fully. In most cases, you may not know what to do. The best advice in such cases is to use the internet. For example, you can google about
* * How to exploit a vulnerability of a specific service version
  * How does a protocol work
  * How does a web framework work
  * What commands to run to find what you are looking for
  * Privilege Escalation common commands and techniques
  * Anything that you do not fully understand: If you partially understand something you may get your way to the root flag, but it is preferable to understand how something works.
