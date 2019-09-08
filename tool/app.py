from flask import Flask, render_template, request, jsonify
import acenka

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/',methods = ['GET', 'POST'])
def basicInfo():
	param = request.form['website']
	l = acenka.cms_find(param)
	return acenka.scan(l)

if __name__ == '__main__':
   app.run(debug = True)
