from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/number/<num>")
def number(num):
	return f"This is the {num}"
@app.route("/reeba")
def hello():
    return "<p>Hello, World!</p>"\
	"<img src='https://media.giphy.com/media/MeJgB3yMMwIaHmKD4z/giphy.gif'>"
if __name__=="__main__":
	app.run(debug = True)
