from API import getPopulation
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

# render default index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle query from index.html
@app.route('/runQuery', methods=['POST'])
def runQuery():

    result = "null"     #initialize result variable
    subject = request.form['subject']      #get subject from form
    stateAbrv = request.form['state']       #get state abreviation from form

    #if subject is total population
    if subject == "totalPop":

        #send getPopulation query with state abrv
        result = getPopulation(stateAbrv)
        
        #format result nicely
        output = f'The state of: {stateAbrv}' + \
                        f' has a total population of: {result}'
    
    #render index.html template, send nicely formatted response with display
    return render_template('index.html', display = output)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)