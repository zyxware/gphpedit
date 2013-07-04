#! /usr/bin/python

import re

def comstrip(line):
	line=re.sub("['][^[[\][']]]*?[']","",line)
	line=re.sub('["][[\]["]]]*?["]',"",line)
	line=re.sub("[/][/].*","",line)
	line=re.sub("[/][*].*?[*][/]","",line)
	line=re.sub("[/][*].*","",line)
	line=re.sub(".*[*][/]",line)
	return  line
	
	

def check(inputfile,outputfile):
	intendno=0
	arraystat=0
	opencase=0
	phpstat=0
	stat=0
	try:
		ifp=open(inputfile,"r")
		ofp=open(outputfile,"r")
	except IOError:
		return "MESSAGE\nError in opening files",0
	ift=ifp.readlines()
	oft=ofp.readlines()
	fnamelist=[]
	initial=ift[:]
	for i in range(len(oft)):
		oft[i]=oft[i][len(inputfile)+1:]
	for line in oft:
		linename=re.search("^(?P<lineno>.*?)[:]",line)
		lineno=int(linename.group('lineno'))-1
		#if len(ift[lineno])>250:
		#	continue
		if 'no mixed case function or variable names' in line:
			fnamelist.append(lineno+1)
			print lineno
			continue
		if '->' in line[:20]:
			repl=re.search("['](?P<replace>.*?)['][ ][-][>][ ]['](?P<replacewith>.*?)[']",line)
			
			if not repl:
				continue
			print 5
			impline=ift[lineno][:ift[lineno].find(repl.group('replace'))]
			if (impline.count("'")-impline.count("\'"))%2 or (impline.count('"')-impline.count('\"'))%2:
				continue
			ift[lineno]=ift[lineno].replace(repl.group('replace'),repl.group('replacewith'))
			if ift[lineno].count(repl.group('replace'))>1:
				substring="[ ]*"+repl.group('replace')+"[ ]*"
				ift[lineno]=re.sub(substring,repl.group('replacewith'),ift[lineno])
			stat=1
			continue
	for i in range(len(ift)):
		if len(ift[i])>250:
			continue
		if not ift[i][:-1] or not ift[i].strip():
			continue
		if '<?' in ift[i]:
			phpstatus=1
			if '<?php' not in ift[i]:
				aft[i]=aft[i].replace('<?',"<?php")
		if not phpstatus:
			continue
		if '?>' in line:
			phpstatus=0
		if intendno<0:
			intendno=0
		if '$ ' in line:
			impline=ift[i][:ift[i].find('$ ')]
			if not (impline.count("'")-impline.count("\'"))%2 or (impline.count('"')-impline.count('\"'))%2:
				ift[i]=re.sub("[$][ ]*",'$',ift[i])
		if re.search("array[ ]+[(]",ift[i]):
			ift[i]=re.sub("array[ ]+[(]","array(",ift[i])
		if '}' in ift[i]:
			intendno-=1
		if 'case ' in ift[i] or 'default ' in ift[i]:
			intendno-=1
		if ' array(' in ift[i]:
			arraystat=1
		if (');' in ift[i] or re.search("[)][ ]+[;]",ift[i])) and arraystat:	
			arraystat=0
		ift[i]='  '*intendno+ift[i].lstrip()
		if ift[i][-1]!='\n':
			ift[i]=ift[i]+'\n'
		if arraystat:
			ift[i]='  '+ift[i]
		if '{' in ift[i]:
			intendno+=1
		if 'case ' in ift[i] or 'default ' in ift[i]:
			intendno+=1

	
	output="MESSAGE\nOperations handled successfully\nWarnings"
	if initial==ift:
		output="MESSAGE\nAll clear\nWarningsS"
	else:
		ifp=open(inputfile,"w")
		ifp.writelines(ift)
		ifp.close()
	if not fnamelist:
		output=output+" : 0\n"
	else:
		output=output+" : Variable name errors on"
		for i in fnamelist:
			output=output+" "+str(i)
		output=output+"\n"
	ifp.close()
	ofp.close()


	return output,stat
