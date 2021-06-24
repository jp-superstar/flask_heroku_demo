from flask import Flask
app= Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    return "<h1>Welcome to flask, I am Jyotiprakash</h1>"
if __name__=="__main__":
    app.run()



