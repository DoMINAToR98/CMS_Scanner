__author__='kshitij'

from flask import Flask, render_template, request, jsonify
import acenka
from threading import Thread
import Queue
# from flask_executor import Executor

que = Queue.Queue()
threads_list = list()


# def thread_basic(arg):
    # ip = acenka.ip_find(arg)
    # cms = acenka.cms_find(cms)
    # cms = ' '.join(cms)
    # final = "*" + cms + "<br/>" + "*" + ip
    # return final

def thread_cms(cms,arg):
    # cms = acenka.cms_find(arg)
    print str(cms)
    acenka.scan(cms,arg)
    import time
    time.sleep(2000)

def thread_nmap(arg):
    ipadr = acenka.ip_find(arg)
    acenka.port_find(ipadr)
    import time
    time.sleep(2000)

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
    cms = ' '.join(cms)
    final = "&#8611;" + cms + "<br/>" + "&#8611;" + ip + "<br/> &#8611;NMAP Started <br/> &#8611;" + cms2+" scan Started<br/>"
    t3 = Thread(target=lambda q, arg1: q.put(thread_nmap(arg1)), args=(que,param))
    t3.start()
    t2 = Thread(target=lambda q, arg1, arg2: q.put(thread_cms(cms2,arg2)), args=(que,cms2,param))
    print cms2
    t2.start()
    # threads_list.append(t2)
    # threads_list.append(t3)
    #
    # for t in threads_list:
    #     t.join()

    return jsonify(result = final)




    #

#  threads_list.append(t1)

#   threads_list.append(t4)
#     for t in threads_list:
#         t.join()
#
#     while not que.empty():
#         res = que.get()
#         return jsonify(result=res)


if __name__ == '__main__':
    app.run(debug = True)
