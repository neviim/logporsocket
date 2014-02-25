#!/usr/bin/python
# -*-coding: UTF-8-*-

# dependencias:
# 	sudo aptitude install uuid
#   sudo aptitude install python-netifaces
#

import sys
import fcntl
import socket
import struct
import commands

import SocketServer
import config as cfg
import simplejson as json

from datetime import datetime
from nvmtools import MacTools

dev=[{"Nome": "Neviim",
	  "Status": {"list":[{"Data":   "14/02/2012"},
	   				     {"Update": "20/02/2014"},
						 {"Versao": "0.5.1"}]}}]

# Classe para gravação de log, duplicação de DVD DAVI
#
class DuplLog:
	""" script para DuplLog
	"""
	# 
	def ping(self):
		""" ping --> pong """
		return "pong"

	def __init__(self, status=0, keymd5=None):
		""" """
		self.maquina = ""
		self.status = status
		self.mac = ""
		self.ip  = ""
		self.keymd5 = keymd5

	def getMaquina(self):
		""" Retorna o nome da maquina. """
		self.maquina = socket.gethostname()
		return(self.maquina)

	def getMac(self, device):
		""" Retorna o MAC address corrente setado no device recebido por parametro. """
		try:
			if nt.isOSx():                                  
				self.mac = nt.getOSxMac(device)
			elif nt.isLinux():
				self.mac = nt.getLinuxMac(device)
 		except Exception, err:
 			raise
		return(self.mac.replace("\n", ""))

	def getIP(self, device):
		""" Retorna o IP corrente setado no device recebido por parametro. """
		try:
			if nt.isOSx():                                  
				self.ip = nt.getOSxIP(device)
			elif nt.isLinux():
				self.ip = nt.getLinuxIP(device)
 		except Exception, err:
 			raise
		return(self.ip.replace(" ", ""))

	def enviaMsgLog(self, server, porta, mensagem):
		""" Envio de mensagem formato texto a um server socket. """
		try:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#host  = socket.gethostname()
			client.connect((server, porta))
			client.send(mensagem)
			client.shutdown(socket.SHUT_RDWR)
			client.close()
			return None
		except Exception as msg:
			return(msg)

	def enviaMsgJson(self, server, porta, data):
		""" """
		#data = {'message':'Ola server json!', 'teste':123.4}
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((server, porta))
		s.send(json.dumps(data))

		result = json.loads(s.recv(1024))
		s.close()
		return(result)

	def geraLog(self, device, status):
		""" 
			device: Placa de rede a ser consultada podendo ser; linux: eth0, eth1, OSx: en0, ef0 etc
			status: 0 --> Gravação bem sucedida
					1 --> Gravação deu error

			O que sera gravado: Maquina
								MAC
								IP         
								Data 
								Status

			Uso: geraLog("eth0", 1)         #Gracaçao com erro (1) 
		""" 
		log = [{"maquina": dl.getMaquina(), "ip": dl.getIP(device) ,"mac": dl.getMac(device), 
			    "status": {"list": [{"data": str(datetime.now())}, {"error": status}]}}]
		#
		return(log)

	
# ========================
if __name__ == "__main__":
	""" """
	if len(sys.argv) > 0:
		status = sys.argv[1]
		keyMd5 = sys.argv[2]

		nt = MacTools()
		dl = DuplLog()

		datalog = dl.geraLog(cfg.DEVICE, status)
		print dl.enviaMsgJson(cfg.SERVER, cfg.PORTA, datalog)
		
	else:
		#sendStatus("Parametro incompleto.")
		print "Negado."
