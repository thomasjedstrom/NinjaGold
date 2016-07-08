from flask import Flask, render_template, request, redirect, session, Markup
from time import strftime
import random, datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'log' not in session:
		session['log'] = ''
	print session['gold']
	return render_template("index.html", gold=session['gold'], log=session['log'])    

@app.route('/process', methods=['POST'])
def process():
	if request.form['action'] == 'farm':
		goldNow = random.randrange(10, 21)
		session['gold'] += goldNow
		session['log'] += Markup('<p class="green">Earned ' + str(goldNow) + ' gold from the farm (' + strftime("%Y/%m/%d %I:%M %p") + ')</p>')
		return redirect('/')
	elif request.form['action'] == 'cave':
		goldNow = random.randrange(5, 11)
		session['gold'] += goldNow
		session['log'] += Markup('<p class="green">Earned ' + str(goldNow) + ' gold from the cave (' + strftime("%Y/%m/%d %I:%M %p") + ')</p>')
		return redirect('/')
	elif request.form['action'] == 'house':
		goldNow = random.randrange(2, 6)
		session['gold'] += goldNow
		session['log'] += Markup('<p class="green">Earned ' + str(goldNow) + ' gold from the house (' + strftime("%Y/%m/%d %I:%M %p") + ')</p>')
		return redirect('/')
	else:
		goldNow = random.randrange(-50, 51)
		session['gold'] += goldNow
		if int(goldNow) > 0:
			session['log'] += Markup('<p class="green">Entered a casino and won ' + str(goldNow) + ' gold... YAY! (' + strftime("%Y/%m/%d %I:%M %p") + ')</p>')
		else:
			goldNow = int(-goldNow)
			session['log'] += Markup('<p class="red">Entered a casino and lost ' + str(goldNow) + ' gold... Ouch... (' + strftime("%Y/%m/%d %I:%M %p") + ')</p>')
		return redirect('/')

@app.route('/reset')
def reset():
	session.pop('log')
	session.pop('gold')
	return redirect('/')

app.run(debug=True)



session['gold'] = random.randrange(0, 50)