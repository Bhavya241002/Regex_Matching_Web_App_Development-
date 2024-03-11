from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        text = request.form['text']
        pattern = request.form['pattern']
        matches = re.findall(pattern, text)
        return render_template('results.html',text=text, pattern=pattern, matches=matches)
    return redirect('/')

@app.route('/email', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        email = request.form.get('email')
        error = None
        match = None
        if re.match(r"[^@]+@[^@]+\.com", email):
            match = "Email is valid"
        else:
            error = "Email is not valid"
        return render_template('email_validation.html', error=error, email=email, match=match)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=5000)