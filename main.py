#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 vladislav <vladislav@vladislav-UX303UA>
#  
#  
import os
from subprocess import Popen, PIPE

def main(args):
	path="/home/vladislav/docker/"
	if not os.path.exists(path):
		os.mkdir(path)
		
	
	f=open(path+"Dockerfile", 'w') #создание файла-инструкции образа Docker
	
	############################################
	##########	Текст Докерфайла	############
	############################################
	text='''FROM ubuntu
		MAINTAINER wlad.babkin@mail.com
		RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
		RUN apt-get update
		RUN apt-get -y install  --no-install-recommends g++
		RUN apt-get -y install  --no-install-recommends gcc 
		RUN apt-get -y install  --no-install-recommends python
		RUN apt-get -y install git
		RUN mkdir /ns3
		RUN cd /ns3
		RUN git clone git://github.com/Wladikgadik/ns3-not-compiled.git
		
		RUN cd /ns3-not-compiled/ns-3.26; ./waf configure; ./waf build'''
	f.write(text)
	f.close()
	#subprocess.call(["docker build "+path])
	Popen("docker build "+path, shell=True)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
