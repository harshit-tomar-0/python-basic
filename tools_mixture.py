import subprocess,sys,threading,time,argparse
#tools used
#Dmitry
#nmap
#dnsenum
tool = ['dmitry -w -n -s -e {}','nmap -A {}','lbd {}','dnsrecon --tcp -d {}','enum4linux -U -M -S -P -G -D -o -i -n -r -a {}','dig -x {}','amass enum -src -brute -min-for-recursive 2 -d {}']
class tools():
    def __init__(self,ip=None,port=None,dns=None):
        self.ip = ip
        self.port = port
        self.dns = dns
    def dmitry(self): #dmitry --> both ip/dns --> find useful info
        if self.ip != None or self.dns == None: 
            for i in str(subprocess.getoutput(tool[0].format(self.ip))).split('\n'):
                print(i)
        if self.ip == None or self.dns != None:
            for i in str(subprocess.getoutput(tool[0].format(self.dns))).split('\n'):
                print(i)
    def nmap(self): #dmitry --> both ip/dns --> find useful info
        if self.ip != None or self.dns == None: 
            for i in str(subprocess.getoutput(tool[1].format(self.ip))).split('\n'):
                print(i)
        if self.ip == None or self.dns != None:
            for i in str(subprocess.getoutput(tool[1].format(self.dns))).split('\n'):
                print(i)
    def lbd(self): #lbd --> dns --> find load balancing on dns
        for i in str(subprocess.getoutput(tool[2].format(self.dns))).split('\n'):
            print(i)
    def dnsrecon(self): #dnsrecon --> dns --> info
        for i in str(subprocess.getoutput(tool[3].format(self.dns))).split('\n'):
            print(i)
    def enum4linux(self): #enum4linux --> ip --> ?
        for i in str(subprocess.getoutput(tool[4].format(self.ip))).split('\n'):
            print(i)
    def dig(self): #dig --> dns --> info
        for i in str(subprocess.getoutput(tool[5].format(self.dns))).split('\n'):
            print(i)
    def amass(self): #amass --> dns --> info
        for i in str(subprocess.getoutput(tool[6].format(self.dns))).split('\n'):
            print(i)

new = tools('ip','port','dns')
def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", help="Target IP", type=str)
    parser.add_argument("-p", "--port", help="port ", type=str)
    parser.add_argument("-d", "--dns", help="dns (example:https://google.com/)", type=str)
    args = parser.parse_args()
    ip = str(args.ip)
    port = str(args.port)
    dns = str(args.dns)
    if ip == None and dns != None:
        t = tools(None,port,dns)
        t.dmitry()
        t.nmap()
        t.lbd()
        t.dnsrecon()
        t.dig()
        t.amass()
    elif ip != None and dns ==None:
        t=tools(ip,port)
        t.dmitry()
        t.nmap()
        t.enum4linux()
    else:
        for i in range(10):
            print('eXit')
            time.sleep(1)
            os.system('clear')
