from flask import Flask, redirect, url_for, request, render_template
from database import insert_data


app = Flask(__name__)


@app.route('/')
def render():
    return render_template('home.html')


@app.route('/success')
def success(name):
   return 'Successfully added to database'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/post_location', methods = ['POST'])
def post_location():
   pin = request.form['pin']
   addr = request.form['address']
   city = request.form['city']
   lat = request.form['lat']
   lng = request.form['long']
   
   insert_data(pin,
               addr,
               city,
               lat,
               lng)

   return redirect(url_for('success'))




if __name__ == '__main__':
   app.run(debug = True)