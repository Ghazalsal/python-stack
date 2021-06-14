from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('index.html',x=int(8),y=int(8))  
    
@app.route('/<int:x>')                           
def hello(x):
    
    return render_template('index.html',x=x,y=int(8))

@app.route('/<int:x>/<int:y>')                           
def third(x,y):
    return render_template('index.html',x=x,y=y)  
    
if __name__=="__main__":
    app.run(debug=True)