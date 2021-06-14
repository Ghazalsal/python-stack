from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

@app.route('/')
def mm():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
   
    return render_template("show.html", name=request.form["name"], loc=request.form['loc'], lang=request.form['lang'], comm=request.form['comm'])


if __name__=="__main__":   
    app.run(debug=True) 