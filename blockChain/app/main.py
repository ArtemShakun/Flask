from flask import Flask, render_template, request, url_for, redirect
from block import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        to_who = request.form['to_who']

        write_block(name = lender, amount = amount, to_who = to_who)
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
