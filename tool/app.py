from flask import Flask, render_template, request, jsonify
import cms_finder

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/',methods = ['GET', 'POST'])
def basicInfo():
	param = request.form['website']
	l = cms_finder.cms_find(param)
	return jsonify(results = l)

if __name__ == '__main__':
   app.run(debug = True)
