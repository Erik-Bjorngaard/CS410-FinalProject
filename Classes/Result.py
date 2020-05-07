from nvd3 import pieChart, multiBarChart

# The Result class processes a request into a D3.js result using the nvd3 library
class Result:

    def __init__(self):
        ""

    # Determine which graph to display based on the selected data Topic
    def get_graph_type(self, data_topic):
        # display pie chart if comparing population
        if(data_topic == "totalPop"):
            graph_type = "pieChart"

        # else use a bar chart
        else:
            graph_type = "multiBarHorizontalChart"
        return graph_type

    # Send request to API and return result
    def get_result(self, request, graph_type, state_Abrv):

        # define variables
        usResult = request['usResult']
        stateResult = request['stateResult']
        type = graph_type

        # Display pie chart
        if(type == "pieChart"):
            value = int(usResult) - int(stateResult)
            chart = pieChart(name=type, color_category='category20c', height=450, width=450)
            xdata = ["United States", state_Abrv]
            ydata = [int(value), int(stateResult)]
            extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
            chart.add_serie(y=ydata, x=xdata, extra=extra_serie)

        # else display bar chart
        else:
            chart = multiBarChart(width=500, height=400, x_axis_format=None)
            xdata = ["United States", state_Abrv]
            ydata = [usResult, stateResult]
            chart.add_serie(name="", y=ydata, x=xdata)
            chart.show_legend = False
            
        # convert charts into html content (and JavaScript)
        chart.buildcontent()
        result = chart.htmlcontent

        return result