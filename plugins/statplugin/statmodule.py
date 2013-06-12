#! /usr/bin/python

#This is the configuration module for the status plugin
#for gphpedit, php editor
#For more details, read the readme distributed along with the plugin


import re
import string
import statconf



def commentmanagerphp_c(lines):
	index=0
	for line in lines:
		lines[index]=re.sub(r"//.*","",line,re.DOTALL)
		index+=1	
	text=string.join(lines)
	while 1:
		if re.search(r"/\*.*\*/",text,re.DOTALL):
			text=re.sub(r"/\*([^\*/]+)\*/","\n",text,re.DOTALL)
		else:
			break
	tempob=string.split(text,'\n')
	retob=[]		
	for line in tempob:
		if not(statconf.BlankLineCount):
			if line.strip():
				retob.append(line)
		else:
			retob.append(line)			
	return retob		

		



def commentmanagerhtml(lines):
	text=string.join(lines)
	while 1:
		if re.search(r"<!\-\-",text,re.DOTALL):
			text=re.sub(r"<!\-\-([^\*/]+)\-\->","\n",text,re.DOTALL)
		else:
			break
	tempob=string.split(text,'\n')
	retob=[]		
	for line in tempob:
		if not(statconf.BlankLineCount):
			if line.strip():
				retob.append(line)
		else:
			retob.append(line)			
	return retob		



def commentmanagerpy(lines):
	index=0
	for line in lines:
		if re.search("#".line):
			if not (re.search(r'''['"]{1,3}.*#.*['"]{1,3}''',lines) and (not re.search(r'''['"]{2}.*#.*['"]{2}''',lines))):
				lines[index]=re.sub(r"#.*","",line,re.DOTALL)
		index+=1		
	for line in lines:
		if not(statconf.BlankLineCount):
			if line.strip():
				retob.append(line)
		else:
 			retob.append(line)						
	return retob		
	
			


def messagemanager(lines):
	lineno=0
	charno=0
	wordno=0
	if lines:
		lineno=len(lines)
		for line in lines:
			if statconf.SpaceCount: charno+=len(line)
			words=line.split()
			for word in words:
				if not statconf.SpaceCount: charno+=len(word.strip())
				for key in ['\"','\'','.','<','>','?',',','#','-','+','_','&','$','/','(',')','~']:
					word=word.replace(key," ")
				for w in word.split():
					if w.strip():
						wordno+=1
	string=""
	if statconf.Printline:
		string=string+"\nNumber of lines : "+str(lineno)
	if statconf.Printword:
		string=string+"\nNumber of words : "+str(wordno)
	if statconf.Printchar:
		string=string+"\nNumber of characters : "+str(charno)		
	return string


def commentmanager(lines,filename):
	if not statconf.CommentStatus: 
		linetemp=[]
		if re.search(r"\.php$|\.c$|\.cpp$",filename):
			linetemp=commentmanagerphp_c(lines)
		elif re.search(r"\.htm$|\.html$",filename):
			linetemp=commentmanagerhtml(lines)
			linetemp=commentmanagerphp_c(linetemp)
		elif re.search(r"\.py$",filename):
			linetemp=commentmanagerpy(lines)	
		else:
			linetemp=lines		
		return linetemp
	else:
		return lines		
