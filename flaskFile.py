from API import getPopulation
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

# render default index page
@app.route('/')
def index():
    return render_template('index.html')

# render default index page
@app.route('/runQuery', methods=['POST'])
def runQuery():
    result = "null"
    subject = request.form['subject']
    stateAbrv = request.form['state']

    if subject == 1:
        print(subject, stateAbrv)

    result = getPopulation(stateAbrv)
    output = f'There are: {result}' + \
                    f' people in the state of: {stateAbrv}'

    print(output)

    return render_template('index.html', display = output)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)