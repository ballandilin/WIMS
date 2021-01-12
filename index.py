from flask import Flask, render_template, request
import main as find
from flask_socketio import SocketIO
import pypugjs
import gunicorn

app = Flask(__name__, static_url_path='/static')
app.jinja_env.filters['zip'] = zip
socketio = SocketIO(app)

img1 = "../img/imgSet/"



@app.route('/')
def index():
   return render_template('index.html', title="WIMS")

@app.route('/', methods=['GET','POST'])
def test():
   temp = None
   # app = find.App(img1, "../img/imgComp/0.jpg")
   if request.method == 'POST':
      temp=request.json['img']
      app = find.App(img1, temp)
      name = app.begin()
      print(name)
      socketio.emit('result', name, namespace='/')

   return render_template('index.html', title=name)


if __name__ == '__main__':
   socketio.run(app, debug = True)