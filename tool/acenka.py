import subprocess
import requests
import json
import socket
from urlparse import urlparse

###!---- Finding Out the Name and the Version ----!
key='4ac0c57c5f2ec2b1bf7e0bfaaef52e91f44eaecbd5a8e640cd69435bc95ab96b856aef'
#param='http://adgitmdelhi.ac.in/'  --> wp
#param'https://unric.org/en/' --> joomla
#param='https://www.rutgers.edu/' --> drupal

def cms_find(param):
	List=[]
	url = 'https://whatcms.org/APIEndpoint/Technology?key='+key+'&url='+param
	r = requests.get(url)
	var= r.json()
	dummy_to_save_requests='{"request":"https:\/\/whatcms.org\/APIEndpoint\/Technology?key=4ac0c57c5f2ec2b1bf7e0bfaaef52e91f44eaecbd5a8e640cd69435bc95ab96b856aef&url=http:\/\/adgitmdelhi.ac.in\/","request_web":"https:\/\/whatcms.org\/?s=http%3A%2F%2Fadgitmdelhi.ac.in%2F","result":{"code":200,"msg":"Success"},"results":[{"categories":["CMS","Blog"],"name":"Joomla","url":"https:\/\/whatcms.org\/c\/WordPress","version":"5.2.2"},{"categories":["Programming Language"],"name":"PHP","version":""},{"categories":["Database"],"name":"MySQL","version":""},{"categories":["Web Server"],"name":"Nginx","version":"1.17.3"}]}'
	#var = json.loads(dummy_to_save_requests)
	List.append(var['results'][0]['version'].encode("utf-8"))
	List.append(var['results'][0]['name'].encode("utf-8"))
	return List

def ip_find(param):
	uparse = urlparse(param)
	ip = socket.gethostbyname(uparse[1])
	return ip

def port_find(param):
	f = open("reports/portScan.txt", "w")
	subprocess.call(["nmap","-A",param],stdout = f)
	f.close()

def scan(cmslist,param):
	target=[]
	target.append(cmslist)
	###!---- Generating the report in Text Format ----!
	f = open("reports/cms_Scan.txt","w")
	if(target[0][1]=="WordPress"):
		print "!---Starting WordPress Scan---!"
		subprocess.call("wpscan --url "+ param +" --no-banner --ignore-maine-redirect --detection-mode aggressive".split(), stdout=f)
	elif(target[0][1]=="Joomla"):
		print "!---Starting Joomla Scan---!"
		subprocess.call(("joomscan -u "+param+" > target_reportJoomla.txt").split(),stdout=f)
	elif(target[0][1]=="Drupal"):
		print "!---Starting Drupal Scan---!"
		subprocess.call(("droopescan scan drupal -u "+param+" > target_reportDrupal.txt").split(),stdout=f)
	else:
		no_supp =  "No support for "+target[0][1]+" yet."
		f.write(no_supp)
		print no_supp
	f.close()
###!---- Beautify the text file for pdf generation ----!
# to be implemented
