#!/usr/bin/python
# -*-coding: UTF-8-*-

import SocketServer
import json

import config as cfg

dev=[{ "Nome": "Neviim",
			   "Status": {"list":[ {"Data":   "18/02/2013"},
								   {"Update": "24/02/2014"},
								   {"Versao": "0.2"}]}}]

class NvmTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class NvmTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			data = json.loads(self.request.recv(1024).strip())
			# 
			print data
			# dados recebido tetorna um ok
			self.request.sendall(json.dumps({'retorno':'ok'}))
		except Exception, err:
			print "Expreção recebida por mensagem: ", err

###
#
print "Inicializando server: " +str(cfg.SERVER)+ " porta: " +str(cfg.PORTA)

server = NvmTCPServer((cfg.SERVER, cfg.PORTA), NvmTCPServerHandler)
server.serve_forever()

