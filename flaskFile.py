from flask import Flask, render_template, request, url_for
from Classes.CensicalInterface import CensicalInterface

app = Flask(__name__)

# render default index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle query from index.html
@app.route('/runQuery', methods=['POST'])
def runQuery():

    # create new interface object
    interface = CensicalInterface(request.form['subject'] ,request.form['state'])
    result = interface.display_result()
    
    #render index.html template, send nicely formatted response with display
    return render_template('result.html', display = result['message'], htmlContent = result['htmlContent'])


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)