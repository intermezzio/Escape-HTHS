import Main

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html");

@app.route("/game")
def playGame():
	Main.mainloop()

if __name__ == '__main__':
	app.run(debug=True)