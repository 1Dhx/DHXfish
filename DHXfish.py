import os
os.system("clear")
#colors
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#GUI
os.system("toilet -f mono12 -F gay DHXfish")

print ("\033[0;31m telegram: https://t.me/DHXfollowers\n \n \n \n ")


print ("\033[0;32m[1] PyPhisher  \n")
print ("\033[0;34m[2] Clifty \n")
print ("\033[0;35m[00] exit \n")
y = input(">>>")

#back end
if y == "1":
    os.system("pkg install git python3 python-pip php openssh -y")
    os.system("git clone https://github.com/KasRoudra/PyPhisher")
    os.system("cd PyPhisher")
    os.system("pip3 install -r files/requirements.txt --break-system-packages")
    os.system("python3 pyphisher.py")
elif y == "2" :
    os.system("pkg update && pkg upgrade -y && pkg install cloudflared git -y && git clone https://github.com/Alygnt/Clifty && cd Clifty && bash clifty.sh")
elif y == "00":
    print ("thanks for use")
    os.system("exit")	
else :
    print ("\033[0;34m error reuse the tool")
    os.system("python DHXfish.py")

