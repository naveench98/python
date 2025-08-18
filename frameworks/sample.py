from flask import Flask
#This program about flask
app=Flask(__name__)

@app.route('/')
def result():
    return "please subscribe"


if __name__=='__main__':
    app.run()