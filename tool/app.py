from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['GET', 'POST'])
def basicInfo():
	key='4ac0c57c5f2ec2b1bf7e0bfaaef52e91f44eaecbd5a8e640cd69435bc95ab96b856aef'
	param=request.form['website']
	url = 'https://whatcms.org/APIEndpoint/Technology?key='+key+'&url='+param
	# r = requests.get(url)
	# var= r.json()
	test='{"request":"https:\/\/whatcms.org\/APIEndpoint\/Technology?key=4ac0c57c5f2ec2b1bf7e0bfaaef52e91f44eaecbd5a8e640cd69435bc95ab96b856aef&url=http:\/\/adgitmdelhi.ac.in\/","request_web":"https:\/\/whatcms.org\/?s=http%3A%2F%2Fadgitmdelhi.ac.in%2F","result":{"code":200,"msg":"Success"},"results":[{"categories":["CMS","Blog"],"name":"WordPress","url":"https:\/\/whatcms.org\/c\/WordPress","version":"5.2.2"},{"categories":["Programming Language"],"name":"PHP","version":""},{"categories":["Database"],"name":"MySQL","version":""},{"categories":["Web Server"],"name":"Nginx","version":"1.17.3"}]}'
	var = json.loads(test) 
	return (var['results'][0]['version'] + '\n' + var['results'][0]['name'])

if __name__ == '__main__':
   app.run(debug = True)
