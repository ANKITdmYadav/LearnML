from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "welcome to home page"

@app.route("/result/<int:score>")
def result(score):
    return f'you got {score} marks'


# jinja 2 template engine
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=33:
        res="PASS"
    else :
        res="FAIL"
    # return render_template('result.html',result=res,ss=score)

    exp={'score':score,'res':res}
    return render_template('result1.html',result=exp)



# Building dynamic URL

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        total_score=(science+maths)/2
    else:
        return render_template('getresult.html')
    return redirect(url_for('success',score=total_score))






if __name__=="__main__":
    app.run(debug=True)