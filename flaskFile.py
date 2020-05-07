from API import Adapter
from flask import Flask, render_template, request, url_for
from nvd3 import pieChart
import sys
from classes.Result import Result
from classes.Request import Request
from classes.CensicalInterface import CensicalInterface

app = Flask(__name__)

# render default index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle query from index.html
@app.route('/runQuery', methods=['POST'])
def runQuery():

    result = "null"     #initialize result variable
    res = ""
    subject = request.form['subject']      #get subject from form
    stateAbrv = request.form['state']       #get state abreviation from form
    # create new interface object
    interface = CensicalInterface(request.form['subject'] ,request.form['state'])

    adapter = Adapter(interface.get_data_topic(), interface.get_geographies())
    result = adapter.execute_query()
    print(result)

    #if subject is total population
    if subject == "totalPop":

        #format result nicely
        output = f'The state of: {stateAbrv}' + \
                        f' has a total population of: {result}'

        
        test = Result()
        graph_type = test.get_graph_type(subject)
        res = test.get_result(result,graph_type,stateAbrv)
        
    else:
        output = f'The state of: {stateAbrv}' + \
                        f' has a median household income of: ${result}'

        test = Result()
        graph_type = test.get_graph_type(subject)
        res = test.get_result(result,graph_type,stateAbrv)

    
    
    #render index.html template, send nicely formatted response with display
    return render_template('result.html', display = output, htmlContent = res)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)