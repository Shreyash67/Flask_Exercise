from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

@app.route("/calculator",methods=["GET","POST"])
def calculator():
    if request.method=="GET":
        return render_template("calculator.html")
    else:
        n1 = float(request.form["Number1"])
        op = request.form["operation"]
        n2 = float(request.form["Number2"])
        
        if op == "addition":
            results = n1+n2
        elif op == "subtraction":
            results = n1-n2
        elif op == "multiplication":
            results = n1*n2
        elif op == "division":
            results = n1/n2
            
        return render_template("result.html",result=results)                
         
if __name__=="__main__":
    app.run(debug=True)