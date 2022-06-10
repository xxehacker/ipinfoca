#!/usr/bin/python3
import requests
import json
import sys
import argparse
from colorama import Fore



parser = argparse.ArgumentParser(description="A tool that collects information about IP address" , usage='./ipinformation.py -h/-t  Ip/Domain',epilog=f'Example: ./ipinformation.py -t 8.8.8.8')

parser.add_argument ("-t", help= "Target/Host Ip Address", type=str, dest='ip' , required=True)
args = parser.parse_args()



print ('''\033[96m

 ____  ____  ____  _  _  ____  _____  ___    __
(_  _)(  _ \(_  _)( \( )( ___)(  _  )/ __)  /__\ 
 _)(_  )___/ _)(_  )  (  )__)  )(_)(( (_-. /(__)\ 
(____)(__)  (____)(_)\_)(__)  (_____)\___/(__)(__)

''')

#ip = input("Enter your target ip: ")

ip = args.ip

try:
	response = requests.get(f"http://ip-api.com/json/{ip}").json()
	print("Country : " , response["country"])
	regionName = response.get("regionName")
	print(Fore.GREEN + "RegionName : "  ,regionName) 
	zip = response.get("zip")
	print(Fore.GREEN + "zip : "  ,zip)  
	timezone = response.get("timezone")
	print(Fore.RED + "timezone : "  ,timezone)  
	isp = response.get("isp")
	print(Fore.RED + "isp : "  ,isp)  
	countryCode = response.get("countryCode")
	print(Fore.RED + "countryCode : "  ,countryCode)  
	lat = response.get("lat")
	print(Fore.YELLOW + "lat : "  ,lat) 
	org = response.get("org")
	print(Fore.YELLOW + "org : "  ,org) 
	asn= response.get("as")
	print(Fore.YELLOW + "asn : "  ,asn)      

except Exception as e:
	print (Fore.RED + "Sorry Dude")


