from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
	return 'Hola mundo'

@app.get('/holaa')
def html():
	return render_template('web.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')