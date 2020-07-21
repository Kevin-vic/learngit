from flask import Flask
app = Flask(__name__)
 
@app.route('/')
@app.route('/users')
def hello():
    return '<title>hahaha</title><h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

app.run()