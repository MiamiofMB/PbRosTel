import flask
from flask import Flask
from flask import render_template
from flask import request
from test import get_pb
app = Flask(__name__)

@app.route('/',methods=['get','post'])
def index():
   if request.method == "POST":
      if request.form['submit_button'] == 'Взять повербанк':
         get_pb()
   return render_template('index.html')

 if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0')
