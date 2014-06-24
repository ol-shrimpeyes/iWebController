from flask import *
from sh import media
from os import urandom
from conf import *
from time import sleep

app = Flask(__name__)
app.secret_key = urandom(255)

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
			isPlaying = str(media('isPlaying', _ok_code=media_codes))[0]
			isPaused = str(media('isPaused', _ok_code=media_codes))[0]
			return redirect(url_for('controls'))
		else:
			return render_template('controls.html', now_playing=nowPlaying(isPaused, isPlaying))
	elif request.method == 'POST':
		cont = request.form['control']
		return redirect(url_for('controls', control=cont))

def nowPlaying(isPaused,isPlaying):
	if isPlaying == '1':
		artist = str(media('artist', _ok_code=media_codes))
		track = str(media('title', _ok_code=media_codes))
		playing = track +'- '+ artist
	elif isPaused == '1':
		artist = str(media('artist', _ok_code=media_codes))
		track = str(media('title', _ok_code=media_codes))
		playing = Markup(track +'- '+ artist + '<em><strong>[paused]<strong></em>')
	else: 
		playing = 'No music playing!'
	return playing

app.run(debug=DEBUG, host=HOST)
