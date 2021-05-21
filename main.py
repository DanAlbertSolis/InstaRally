from flask import Flask, render_template, request, Response
from random import choice
import json

web_site = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

locationsList = []
@web_site.route('/location_update', methods = ['POST'])
def turnToJson():
  global locationsList
  print(request)
  newLocations = request.json
  print(newLocations)
  locationsList.append(newLocations)
  return Response(status=201)

@web_site.route('/')
def welcome():
	return render_template('welcome.html')

@web_site.route('/test')
def test():
	return render_template('test.html')

@web_site.route('/maps')
def maps():
	return render_template('maps.html')

@web_site.route('/events')
def events():
	return render_template('events.html', locations = locationsList)

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)


web_site.run(host='0.0.0.0', port=9090)