from flask import Flask, render_template, jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/math",methods=['POST'])
def math_ops():
    if(request.method=='POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops=="add":
            r = num1 + num2
            result = " The Sum of " + str(num1) +" and " +str(num2) + " is " + str(r)

        if ops=="subtract":
            r = num1 - num2
            result = " The Subtraction of " + str(num1) +" and " +str(num2) + " is " + str(r)
    
        if ops=="mutiply":
            r = num1 * num2
            result = " The Multiplication of " + str(num1) +" and " +str(num2) + " is " + str(r)

        if ops=="divide":
            r = num1 / num2
            result = " The Division of " + str(num1) +" and " +str(num2) + " is " + str(r)

        return render_template('results.html',result=result)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
