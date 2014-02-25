#!/usr/bin/python
# -*-coding: UTF-8-*-

import random, platform, subprocess
import sys, os, time, getopt

dev=[{ "Nome": "Neviim",
	   "Status": {"list":[ {"Data":   "18/02/2013"},
						   {"Update": "20/02/2014"},
						   {"Versao": "0.1"}]}}]

class MacTools:
	"""documentação para classe MacTools"""
	def __init__(self, mac=""):
		self.mac = mac
		
	def isLinux(self):
		"""Verifica se a corrente plataforma é Linux"""
		OS = platform.system()
		return OS == 'Linux'
		
	def isOSx(self):
		"""Verifica se a corrente plataforma é OSx"""
		OS = platform.system()
		return OS == 'Darwin'

	def isRoot(self):
		"""Verifica se o corrente usar é root"""
		return os.getuid() & os.getgid() == 0

	def checkOSxMac(self,device,mac):
		"""Returna true se o corrente mac address correspponde ao mac address enviado"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index = output.find('ether') + len('ether ')
		localAddr = output[index:index+17].lower() 
		return mac == localAddr 

	def checkLinuxMac(self,device,mac):
		"""Returna true se o corrente mac address correspponde ao mac address enviado"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index = output.find('HWaddr') + len('HWaddr ')
		localAddr = output[index:index+17].lower() 
		return mac == localAddr

	def getOSxIP(self,device):
		"""Returna o IP corrente do device recebido"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index1 = output.find('inet ') + len('inet ')
		index2 = output.find('netmask ') + len('netmask')
		localIP = output[index1:index1-(index1-index2)-len('netmask ')].lower()
		return localIP 

	def getLinuxIP(self,device):
		"""Returna o IP corrente do device recebido"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index1 = output.find('addr:') + len('addr:')
		index2 = output.find('Bcast:') + len('Bcast:')
		localIP = output[index1:index1-(index1-index2)-len('Bcast: ')].lower()
		return localIP 

	def getOSxMac(self,device):
		"""Returna o corrente mac address correspponde ao device enviado"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index = output.find('ether') + len('ether ')
		localAddr = output[index:index+17].lower() 
		return localAddr 

	def getLinuxMac(self,device):
		"""Returna o corrente mac address correspponde ao device enviado"""
		output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
		index = output.find('HWaddr') + len('HWaddr ')
		localAddr = output[index:index+17].lower() 
		return localAddr

	def setLinuxMAC(self,device,mac):
		"""Sets um novo mac address para esta maquina, se for um sistema Linux"""
		subprocess.check_call(["ifconfig","%s" % device, "up"])
		subprocess.check_call(["ifconfig","%s" % device, "hw", "ether","%s" % mac])

	def setOSxMAC(self,device,mac):
		"""Sets um novo mac address para esta maquina, se for um sistema Darwin"""
		subprocess.check_call(["ifconfig","%s" % device,"up"])
		subprocess.check_call(["ifconfig","%s" % device,"lladdr","%s" % mac])   
