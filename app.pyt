from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return ('userText')

if __name__ == '__main__':
   app.run(debug = True)