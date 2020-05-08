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
    
    # bool variables to handle the error checking.
    # initialized to True. Assumes there IS an error in the request.
    stateError = True
    subjectError = True

    # check every item in the request.form
    for item in request.form:
        
        #if the request.form has an item called state. Error = false
        if item == 'state':
            stateError = False 
        # else if request.form has an item called subject. Error = false
        elif item == 'subject':
            subjectError = False


    # if stateError OR subjectError are true. user did not check either a subject or state box in form. 
    if stateError == True or subjectError == True:
        # Display error on website
        return render_template('result.html', display = 'Error please select a subject and state')
    
    # Else no error present. Proceed with normal interface calls
    else:
        # create new interface object
        interface = CensicalInterface(request.form['subject'] ,request.form['state'])
        result = interface.display_result()

    #render index.html template, send nicely formatted response with display
    return render_template('result.html', display = result['message'], htmlContent = result['htmlContent'])

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)