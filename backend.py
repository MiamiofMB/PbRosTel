import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import http.client
import sqlite3
import time
from api import get_pb,check_pbs
import psycopg2


#connection = psycopg2.connect(database="dbname", user="username", password="pass", host="hostname", port=5432)
#cur = connection.cursor()
#<form action="{{ url_for('return1') }}" method="post">


def set_time(user,cred):
   cur.execute(f"INSERT INTO data user,take_time,credentials VALUES {user},{cred},{time.time()}")


def if_returned(id,station_id):
   #проверить какие айди возвращает и дальше наладить работу с этими айди в функциях ниже.
   if id in check_pbs(station_id):
      return True
   return False








app = Flask(__name__)
#разобраться с кнопками. разобраться как вставить параметр запроса в редирект. активировать станцию
@app.route('/',methods=['get','post'])
def index():
   if request.method == "POST":
      res = request.json
      if res["btn_type"]=='submit':
         return {'re':url_for('giveout',id = res['pb_id'])}
      elif res["btn_type"]=='return':
         return {'re': url_for('return1', id=res['pb_id'])}

   return render_template('index.html')



@app.route('/giveout',methods=['get','post'])
def giveout():
   query = request.args
   station_id=query['id']

   if request.method == "POST":
      res = request.json
      if res["btn_type"] == 'submit':
         #заполнение формы оплаты. Сделать разветвление на если данные были привязаны или нет
         user,cred= 'test','test'
         get_pb(station_id)
         #set_time(user,cred)

         return {'status':'ok'}
   return render_template('index1.html')


# то есть по айди станции есть страница где берешь и где возвращаешь. На странице возврата вводишь айди повербанка и нажимаешь кнопку вернуть после чего вставляешь павербанк обратно. Если не вернуть, то счетчик бабок продолжит капать. И каждый час выписывается счет от тинька.
# после того как ввел айди и нажал на кнопку вернуть, запускается таймер 10 сек если за 10 сек не вставляешь, то пизда вася давай по новой
@app.route('/return',methods=['get','post'])
def return1():
   query = request.args
   station_id=query['id'] #id станции который получаем из параметра запроса
   if request.method == "POST":
      client_message = request.form.get('message') #код на павербанке
      change = ''
      if request.form['submit_button'] == 'Вернуть':
         if if_returned(client_message,station_id):
            #Дальше идет закрытие оплаты
            user = 'test'
            change = 'Все окэй'
            cur.execute(f"DELETE FROM status WHERE user = {user}")
         else:
            change = 'Вставьте павербанк пожалуйста, в противном случае оплата продолжит начисляться и в итоге мы спишем с вам большую блин сумму'


   return render_template('index1_r.html',change=change)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=86, debug=False)
