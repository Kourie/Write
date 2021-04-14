from flask import Flask, render_template, g, request, redirect
import sqlite3
import os
app = Flask(__name__)





def login():
    while True:
        username = input("please insert your username: ")
        password = input("please insert your password: ")
        with sqlite3.connect("time.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM Account WHERE Account =  ? AND Password = ?")
        cursor.excecute(find_user,[(username), (password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print ("welcome " +i[2])
       #     return("exit")
                break

        else:
            print ("account and/or passoword not found")
            again = input("do you want to try again?")
            if again.lower == "n":
                print ("kay")
#                return("exit")
                break

login()
































if __name__ == "__main__":
    app.run(debug=True)