import pyfiglet
from colorama import init,Fore
import scapy.all as scapy
import sys
import os
import os.path
from os.path import join as pjoin
import time
import zipfile
from tqdm import tqdm
import socket
import threading
from queue import Queue
from PIL import Image
from PIL.ExifTags import TAGS
import time
init()
GREEN=Fore.GREEN
RED=Fore.RED
YELLOW=Fore.YELLOW
WHITE=Fore.WHITE
#Text format
print(f"{YELLOW}")
banner=pyfiglet.figlet_format("Noobs Network")
print(banner)
print("©Gone Lastvirus")
#for public ip of sites
def Public_ip(name_site):
    try:
        ip=socket.gethostbyname(name_site)
        print(f"\n{GREEN}Ip of site:\t{ip}")
    except:
        print(f"{YELLOW}\n[!]Something error...\n")
#for cmd prompt control and home
def syss():
    if sys.argv[1]=="start":
        sys.stderr.write(f"{GREEN}\n[1]public address of sites \n[2]port Scanner \n[3]Scan Ip's on your Wi-Fi\n[4]Zip-File Cracker\n")
        sys.stderr.write(f"{GREEN}[5]Image_meta Data Extract")
        print(f"{RED}[+]whats your choice")
def port_scanner(target):
    # a print_lock is what is used to prevent "double" modification of shared variables.
    # this is used so while one thread is using a variable, others cannot access
    # it. Once done, the thread releases the print_lock.
    # to use it, you want to specify a print_lock per thing you wish to print_lock.
    print_lock = threading.Lock()
    ip=socket.gethostbyname(target)
    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect_ex((target,port))
            with print_lock:
                if con==0:
                 print(f"{GREEN}\n[.]{ip}:{port} is Open")
            s.close()
        except  EOFError:
            sys.exit()
    # The threader thread pulls an worker from the queue and processes it
    def threader():
        while True:
        # gets an worker from the queue
            worker = q.get()
        # Run the example job with the avail worker in queue (thread)
            portscan(worker)
        # completed with the job
            q.task_done()
    # Create the queue and threader 
    q = Queue()
    # how many threads are we going to allow for
    for x in range(30):
        t = threading.Thread(target=threader)
     # classifying as a daemon, so they will die when the main dies
        t.daemon = True
     # begins, must come after daemon definition
        t.start()
    #start = time.time()
    # 100 jobs assigned.
    for worker in range(1,6353):
        q.put(worker)
    # wait until the thread terminates.
    q.join()
def zip_file_crack(zip_file,wordlist):
    zip_file=zipfile.ZipFile(zip_file)
    n_word=len(list(open(wordlist,"rb")))
    with open(wordlist,"rb") as wordlist:
        for word in tqdm(wordlist,total=n_word,unit="files"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print(f"{YELLOW}\n [.] password found",word.decode().strip())
            exit(0)
            print(f"{YELLOW}\n [!] password Not found")
            exit(0)
def image_data(image_path):
    
    # path to the image or video
    imagename= image_path

    # read the image data using PIL
    image = Image.open(imagename)

    # extract EXIF data
    exifdata = image.getexif()

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{GREEN}\t{tag:40}: {data}")
def file_search(zip_file):
    try:
        for root,dirs,files in os.walk("c:\\"):
            for files in files:
                if files ==zip_file:
                    File_path=os.path.join(root,files)
                    return File_path
    except:
        try:
            for root,dirs,files in os.walk("d:\\"):
                for files in files:
                    if files ==zip_file:
                        File_path=os.path.join(root,files)
                        return File_path
        except:
            try:
                for root,dirs,files in os.walk("e:\\"):
                    for files in files:
                        if files ==zip_file:
                            File_path=os.path.join(root,files)
                            return File_path
            except:
                for root,dirs,files in os.walk("f:\\"):
                    for files in files:
                        if files ==zip_file:
                            File_path=os.path.join(root,files)
                            return File_path
def ip_scanner():
    request = scapy.ARP()
    print(f"{WHITE}Enter the ip range in CIDR  form(192.168.1.1/24): ")
    request.pdst = input()
    print(f"{WHITE}<<<<<<<Scanning your network please wait>>>>>>")
    broadcast =scapy.Ether() 
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request 
    clients = scapy.srp(request_broadcast, timeout =10, verbose=0)[0]
    print(f"{RED}") 
    print(" "*5+"Ip"+" "*30+"Mac")
    print(f"{WHITE}")
    for element in clients: 
        print(element[1].psrc+" "*18+element[1].hwsrc)
    print(f"{YELLOW}>>>[?]Do you want to continue scanning>>>[y/n]")
    cond=input()
    if(cond=='y'):
        ip_scanner()
    else:
        main()

#All the function call here
def main():
    syss()
    try:
        choose_1=input()
    except EOFError:
        sys.exit()
    if choose_1=="1":
        sys.stderr.write(f"{WHITE}Enter the name of site: ")
        name_site=input()
        Public_ip(name_site)
    elif choose_1=="2":
        sys.stderr.write(f"{WHITE}\n[+]Enter the target: ")
        target=input()
        try:
            port_scanner(target)
        except EOFError:
            sys.exit()
    elif choose_1=="3":
        ip_scanner()

    elif choose_1=="4":
        sys.stderr.write(f"{WHITE}\n[+]Enter the target Zip File: ")
        zip_file=input()
        try:
            zip_path=file_search(zip_file)
        except EOFError:
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
        sys.stderr.write(f"{WHITE}\n[+]Enter the target  Word File: ")
        print(f"{RED}[!]Word File name is rockyou.txt")
        wordlist=input()
        try:
            word_path=file_search(wordlist)
        except EOFError:
            sys.exit()
        print(f"{WHITE}[->]Decryption Start:")
        zip_file_crack(zip_path,word_path)
    elif choose_1=="5":
        sys.stderr.write(f"{WHITE}\n[+]Enter the target image File: ")
        image_file=input()
        try:
            image_path=file_search(image_file)
        except EOFError:
            sys.exit()
        else:
            image_data(image_path)

    else:
        main()

main()
print(f"{WHITE}DO you want to continue[y/n]: ")
cmd=input()
if cmd=='y':
    main()
else:
    sys.exit()




   

    