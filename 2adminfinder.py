import pyfiglet
import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def Adminfinder():
    url=input("Enter the URL to find a Admin panel : ")
    path=input("Enter the path of a wordlist : ")
    print("-"*50)
    print("Scanning Target : ",url)
    print("wordlist        : ",path)    
    print("-"*50)        
    print("[+] parsing the wordlist.....")
    try:
        with open(path) as file:
            check=file.read().strip().split("\n")
            print(G+"[+] PARSING DONE ")
            print(G+"[+] TOTAL PATHS TO BE CHECK : ",str(len(check)))
    except IOError:
        print(R+'[+] FAILED')
        print(R+'[+] Failed to read the wordlist specified')
        sys.exit(1)
    def checkpath(cp):
        u='http://'+url+'/'+cp
        #print (u)
        try:
            r = requests.head(u)
            code=r.status_code
        except requests.ConnectionError:
            print(R+"failed to connect")
            
        if(code == 200 ):
            print(G+"[Found]",u)
        else:
            print(R+'[-]',u)
    print(G+"[+] Begin scanning....")
    for i in range(len(check)):
        #print(check[i])
        checkpath(check[i])
    print(G+'\n Scan complete....')    


ban=pyfiglet.figlet_format("ADMIN FIND3R",font="slant")
print(ban)
print( '                             created by - Ramalingasamy M K')
print()

Adminfinder()
