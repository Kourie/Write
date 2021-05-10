from flask import Flask, render_template, g, request, redirect
import sqlite3
import os
app = Flask(__name__)

DATABASE = 'time.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def contents():
    return render_template ("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/add', methods=["GET","Post"])
def login_function():
    cursor = get_db().cursor()
    username = ("please insert your username: ")
    password = ("please insert your password: ")
    find_user = ("SELECT * FROM Account WHERE user_id =  ? AND password = ?")
    cursor.execute(find_user,[(username), (password)])
    results = cursor.fetchall()
    return render_template ("logged.html", results=results)

#    if results:
 #       for i in results:
  #          print ("welcome " +i[2])
   #         return render_template ("home.html")

    #else:
     #   print ("account and/or passoword not found")
      #  again = input("do you want to try again?")
       # if again.lower == "n":
        #    print ("kay")
         #   return render_template ("home.html")

#login()



if __name__ == "__main__":
    app.run(debug=True)


