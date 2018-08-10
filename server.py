from flask import Flask, request, render_template, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "SuchWowMuchNinja"

@app.route('/')
def root():
    if 'gold' not in session:
        session['gold'] = 0
    if 'strs' not in session:
        session['strs'] = []
    return render_template('index.html')

@app.route('/process/<location>', methods=['POST'])
def process_post(location):
    logStr = ""
    if location == "farm":
        result = random.randint(10,20)
    if location == "cave":
        result = random.randint(5,10)
    if location == "house":
        result = random.randint(2,5)
    if location == "casino":
        result = random.randint(-50,50)
        if result > 0:
            logStr = ("won", "Entered a Casino and won " + str(result) + " gold. Sick! " + str(datetime.datetime.now()))
        elif result < 0:
            logStr = ("lose", "Entered a Casino and lost " + str(result) + " gold. Sucks to suck. " + str(datetime.datetime.now()))
    if location != "casino":
        logStr = ("black", "Earned " + str(result) + " gold from the " + location + "! " + str(datetime.datetime.now()))
    session['gold'] += result
    new_list = session['strs']
    new_list.append(logStr)
    session['strs'] = new_list
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)

