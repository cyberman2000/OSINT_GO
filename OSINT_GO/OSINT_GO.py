import pyfiglet as pyfig
import os
import googlesearch as GS
import datetime
from colorama import *
print(Fore.BLUE + pyfig.figlet_format("""   =======>>>   OSINT GO   <<<=======   """))
print(Fore.YELLOW + """                          Created by CyberMan                      """)
print("""                                 Welcome                              """)
Data_input1=print(Fore.WHITE +"1. |-> Enter for Find info on Google : ")
Data_input2=print("2. |-> Create ID through full name for social networks : ")
Data_input3=print("3. |-> Enter for Find people on Web sites : ")
input_user=int(input("====-> Please choose one of the options according to your needs >>> "))
_Date_Time=datetime.datetime.now()
DT=str(_Date_Time)
if input_user==1:
    print(Fore.RED + pyfig.figlet_format ("Google Power"))
    Name_info=input(Fore.GREEN + "Please enter the name of the information you want >>> ")
    Last_search=Name_info+" *"
    for Last_search in GS.search(Last_search):
        print(Last_search)
        files=open("save_History.txt","a")
        files.write("your Results"+"\n\t")
        files.write(DT+" =====>> ")
        files.write(Last_search +"\n")
        files.close()
    print(Fore.RED + "Warning: "+ Fore.BLUE +"Your Results have been successfully created in this folder")
elif input_user==2:
    print(Fore.BLUE + pyfig.figlet_format("Goole Wild"))
    FName_Target=input(Fore.GREEN + "Please enter the Fname of the target to generate the ID >>> ")
    LName_Target=input(Fore.RED +"Please enter the Lname of the target to generate the ID >>>")
    HBD_Target=input(Fore.BLUE + "Please enter the date of birth of the target >>> ")
    files=open("ID for Social Networks.txt","a")
    files.write("your Results"+"\n\t")
    files.write(DT+" =====>> ")
    files.write(FName_Target + "\n")
    files.write(FName_Target + HBD_Target +"\n")
    files.write(FName_Target+"_"+LName_Target+"\n")
    files.write(FName_Target[0]+LName_Target+"\n")
    files.write(FName_Target[0]+"._."+LName_Target+"\n")
    files.write(FName_Target+"_"+ LName_Target[0]+"\n")
    files.write(FName_Target +"._"+LName_Target[0]+"\n")
    files.write(FName_Target[0]+"_"+FName_Target[1]+"_"+FName_Target[2]+"_"+FName_Target[3]+"_"+FName_Target[4]+"_"+FName_Target[5:]+"\n")
    files.write(LName_Target+HBD_Target+"\n")
    files.write(FName_Target+"._"+HBD_Target[2:]+"\n")
    print(Fore.RED + "Warning: "+ Fore.BLUE +"Your IDs have been successfully created in this folder")

elif input_user==3:
    print(Fore.GREEN + pyfig.figlet_format("Google Dark"))
    Name_people=input(Fore.WHITE + "Please enter your desired name or username >>> ")
    result_on_site="inurl:" + Name_people +"*.*"
    for result_on_site in GS.search(result_on_site):
        print(result_on_site)
        files=open("google_result.txt","a")
        files.write("your Results"+"\n\t")
        files.write(DT+" =====>> ")
        files.write(result_on_site +"\n")
        files.close()
    print(Fore.RED + "Warning: "+ Fore.BLUE +"Your Results have been successfully created in this folder")
else:
    print("Please try again")
