from flask import Flask ,render_template
app = Flask(__name__)   
@app.route('/')         
def hello_world1():
    return 'hello World!'

@app.route('/dojo')         
def hello():
    return 'Dojo!'

@app.route('/say/<name>')         
def hello_world(name):
    
    return f"hello {name}!"

@app.route('/repeat/<int:times>/<name>')         
def hello_s(name,times):
    str=f"<p>{name}</p>"
    for i in range(0,times,1):
        str+=f"<p>{name}</p>"
    return str

if __name__=="__main__":    
    app.run(debug=True)    


