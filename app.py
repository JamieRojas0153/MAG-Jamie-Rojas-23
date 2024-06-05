from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    gain = roi = None
    if request.method == 'POST':
        try:
            returned_amount = float(request.form['returned_amount'])
            invested_amount = float(request.form['invested_amount'])
            gain = returned_amount - invested_amount
            roi = (gain / invested_amount) * 100
        except ValueError:
            gain = roi = 'Invalid input. Please enter numeric values.'
    
    return render_template('index.html', gain=gain, roi=roi)

if __name__ == '__main__':
    app.run(debug=True)
