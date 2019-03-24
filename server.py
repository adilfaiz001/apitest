from flask import Flask, redirect, url_for, request, render_template
from database import insert_data


app = Flask(__name__)


@app.route('/')
def render():
    return render_template('home.html')


@app.route('/success')
def success():
   return 'Successfully added to database'

@app.route('/pin_exist')
def pin_exist():
   return 'Pincode already exist OR latitude+longitude already present'

@app.route('/post_location', methods = ['POST'])
def post_location():
   pin = request.form['pin']
   addr = request.form['address']
   city = request.form['city']
   lat = float(request.form['lat'])
   lng = float(request.form['long'])
   
   res = insert_data(key = pin,
                     place_name = addr,
                     admin_name1 = city,
                     latitude = lat,
                     longitude = lng)
   if res:
      return redirect(url_for('success'))
   else:
      return redirect(url_for('pin_exist'))




if __name__ == '__main__':
   app.run(debug = True)