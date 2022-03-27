from flask import Flask
app = Flask(__hello__)
  
@app.route('/hello/<hello>')
def hello_world(hello):
   return 'Hello World'
  
if __hello__ == '__main__':
   app.run()
