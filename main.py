#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 vladislav <vladislav@vladislav-UX303UA>
#  
#  
import os

def main(args):
	path="/home/vladislav/docker/"
	if not os.path.exists(path):
		os.mkdir(path)
		os.chdir(path)
	
	f=open(path+"Dockerfile", 'w') #создание файла-инструкции образа Docker
	
	############################################
	##########	Текст Докерфайла	############
	############################################
	text="FROM ubuntu "+
		"MAINTAINER nuttzipper@gmail.com"+
		"RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends gcc  g++  python  git"+
		"RUN git clone git://github.com/nuttzipper/ns-3.git"+
		"RUN cd ns-3-dev-git/; ./waf configure; ./waf build"+
		"RUN ln -s ns-3-dev-git/waf /ns3"
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
