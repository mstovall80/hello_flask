from flask import Flask, render_template               
app=Flask(__name__)


app = Flask(__name__)                      
@app.route('/')                             
def hello_world():
    print ('Hello World!!')  
    return render_template("index.html", phrase="hello world", times=5)
    
@app.route('/HI/<name>') 
def Hi(name):  
    print(name)
    return "Hi " + name           

@app.route('/repeat/<word>/<int:num>')
def repeater(word, num):
    return word * num


@app.route('/success')
def success():
    return "success"  

@app.route('/Hello/<name>') 
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') 
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":                      
    app.run(debug=True)   