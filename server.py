ffffvghfrom flask import *
from sh import media
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(255)

@app.route('/')
def main():
	return redirect(url_for('controls'))

@app.route('/controls', methods=['GET', 'POST'])
@app.route('/controls/<control>', methods=['GET', 'POST'])
def controls(control=None):
	if request.method == 'GET':
		if control:
			media(control)
			return redirect(url_for('controls'))
		else:
			return render_template('controls.html')
	elif request.method == 'POST':
		cont = request.form['control']
		return redirect(url_for('controls', control=cont, now_playing=playing))

app.run(debug=True)
