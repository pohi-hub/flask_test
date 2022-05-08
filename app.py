from flask import Flask 
 
app = Flask(__name__)
 
@app.route('/')
def index():
   return "hello world,let try the build something"
   
if __name__ == '__main__':
   app.run(debug=True)