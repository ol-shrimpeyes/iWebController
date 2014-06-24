from flask import *
from sh import media
from os import urandom
from conf import *

app = Flask(__name__)
app.secret_key = urandom(255)

media=media(_ok_code=media_codes)
media_codes = [0,2,4,12,13]

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
			return render_template('controls.html', now_playing=nowPlaying())
	elif request.method == 'POST':
		cont = request.form['control']
		return redirect(url_for('controls', control=cont))

def nowPlaying():
	if str(media('isPlaying'))[0] == '1':
		artist = str(media('artist'))
		track = str(media('title'))
		playing = track +'- '+ artist
	elif str(media('isPaused')) == 1:
		artist = str(media('artist'))
		track = str(media('title'))
		playing = track +'- '+ artist
	else: 
		playing = 'No music playing!'
	return playing

app.run(debug=DEBUG, host=HOST)
