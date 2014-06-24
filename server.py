from flask import *
from sh import media
from os import urandom
from conf import *

app = Flask(__name__)
app.secret_key = urandom(255)

media = [0,12]

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
		return redirect(url_for('controls', control=cont))

def nowPlaying():
	if media('isPlaying', _ok_code=media_codes) == 1:
			artist = media('artist', _ok_code=media_codes)
			track = media('title', _ok_code=media_codes)
			playing = track + artist
		else:
			playing = 'No music playing!'

app.run(debug=DEBUG, host=HOST)
