from flask import Flask
import random

app = Flask(__name__)
n=random.randint(0,10)
@app.route("/")
def guess():
    return "<p>Guess a no. between 0-9...</p>"\
    "<img src='https://media.giphy.com/media/Rs2QPsshsFI9zeT4Kn/giphy.gif'>"
@app.route("/number/<int:num>")
def number(num):
	if(num<n):
		return "It is too low"\
		"<img src='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif'>"
	elif(num>n):
		return "It is too high"\
		"<img src='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif'>"
	else:
		return "Right Guess!!!"\
		"<img src='https://media.giphy.com/media/QJsP0cTAJhg7O47ub2/giphy.gif'>"
if __name__=="__main__":
	app.run(debug = True)
