#!/usr/bin/python

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
        return '''<form action="gitpull" method="post" >
                <button value="Testing environment pull" >Testing environment pull</button> </form>             ''';

import commands
@app.route('/gitpull',methods=['POST','GET'])
def gitpull():
        (status, output) = commands.getstatusoutput('git pull origin master')
        status = str(status)
        response = output.replace("\n","<br>")
        html = status+"<br>response:"+response+'<br><a href="javascript:history.go(-1)">Back</a>'
        return html

if __name__ == '__main__':
    app.run(host="0.0.0.0")

