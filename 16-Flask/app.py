from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to again web dev borinng flask course"


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/tictac")
def tictac():
    return render_template('index.html'),render_template('script.js')

if __name__=="__main__":
    app.run(debug=True)