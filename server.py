from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def root():
    if 'result' not in session:
        session['result'] = ""
    if 'rand_num' not in session:
        session['rand_num'] = random.randrange(1, 101)
        print "the rand num is: ",session['rand_num']
    return render_template('index.html', result=session['result'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    print "the guess is", guess

    if guess > session['rand_num']:
        session['result'] = "Too high!"
    elif guess < session['rand_num']:
        session['result'] = "Too low!"
    else:
        session['result'] = "You got it!"

    print session['result']

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('rand_num')
    session.pop('result')

    return redirect('/')

app.run(debug=True)
