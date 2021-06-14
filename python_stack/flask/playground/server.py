from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/play')                           
def hello_world():
    return render_template('index.html')  
    
@app.route('/play/<int:x>')                           
def hello(x):
    return render_template('index1.html',x=x)

@app.route('/play/<int:x>/<colorChange>')                           
def third(x,colorChange):
    colorChange=colorChange
    return render_template('index2.html',x=x,colorChange=colorChange)  
    
if __name__=="__main__":
    app.run(debug=True)