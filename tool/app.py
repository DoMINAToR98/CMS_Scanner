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
    ipadr = acenka.ip_find(arg)
    acenka.port_find(ipadr)

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
    if cmsV == '':
        final = "<span data-ty=\"input\">CMS Name</span><span data-ty=\"progress\"></span><span data-ty>" + cms2 + "</span><span data-ty=\"input\">IP Address</span><span data-ty=\"progress\"></span><span data-ty>"+ip+"</span><span data-ty=\"input\">Scanning for open ports...</span><span data-ty=\"progress\"></span><span data-ty ></span><span data-ty=\"input\">Scanning Website...</span><span data-ty=\"progress\"></span>"
        print final
    else:
        final = "<span data-ty=\"input\">CMS Version</span><span data-ty=\"progress\"></span><span data-ty>"+cmsV+"</span><span data-ty=\"input\">CMS Name</span><span data-ty=\"progress\"></span><span data-ty>" + cms2 + "</span><span data-ty=\"input\">IP Address</span><span data-ty=\"progress\"></span><span data-ty>"+ip+"</span><span data-ty=\"input\">Scanning for open ports...</span><span data-ty=\"progress\"></span><span data-ty prompt=\">>>\"></span><span data-ty=\"input\">Scanning Website...</span><span data-ty=\"progress\"></span>"

    t3 = Thread(target=lambda q, arg1: q.put(thread_nmap(arg1)), args=(que,param))
    t3.start()
    t2 = Thread(target=lambda q, arg1, arg2: q.put(thread_cms(arg1,arg2)), args=(que,cms,param))
    t2.start()

    threads_list.append(t3)
    threads_list.append(t2)

    return jsonify(result = final)

@app.route('/reportDownload/<filename>')
def reportDownload(filename):
    for t in threads_list:
        t.join()

    return send_from_directory('reports',filename)


if __name__ == '__main__':
    app.run(debug = True)
