__author__='kshitij'

from flask import Flask, render_template, request, jsonify, send_from_directory
import acenka
from threading import Thread
import Queue
import subprocess


que = Queue.Queue()
threads_list=[]

def thread_cms(cms,arg):
    # cms = acenka.cms_find(arg)
    acenka.scan(cms,arg)

def thread_nmap(arg):
    #ipadr = acenka.ip_find(arg)
    acenka.port_find(arg)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def basicInfo():
    param = request.args.get('website',0,type=str)
    ip = acenka.ip_find(param)
    cms = acenka.cms_find(param)
    cms2 = str(cms[1])
    cmsV = str(cms[0])

    if cmsV == ' ':
        final = cmsV+ "<br/>" + cms2 + "<br/>" + ip
    else:
        final = cms2 + "<br/>" + ip
    t1 = Thread(target=lambda q, arg1: q.put(thread_nmap(arg1)), args=(que,ip))
    t1.start()
    t2 = Thread(target=lambda q, arg1, arg2: q.put(thread_cms(arg1,arg2)), args=(que,cms,param))
    t2.start()

    threads_list.append(t1)
    threads_list.append(t2)

    #dict = {'IP Address':ip, 'CMS Version':cmsV, 'CMS Name':cms2}

    return jsonify(result=final)

@app.route('/reportDownload/<filename>')
def reportDownload(filename):
    if filename == "portScan.txt":
        threads_list[0].join()
        return send_from_directory('reports',filename)
    elif filename == "cms_Scan.txt":
        threads_list[1].join()
        return send_from_directory('reports',filename)

if __name__ == '__main__':
    app.run(debug = True)
