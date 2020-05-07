from nvd3 import pieChart, multiBarChart

class Result:

    def __init__(self):
        ""

    # Determine which graph to display based on the selected data Topic
    def get_graph_type(self, data_topic):
        if(data_topic == "totalPop"):
            graph_type = "pieChart"
        else:
            graph_type = "multiBarHorizontalChart"
        return graph_type

    # Send request to API and return result
    def get_result(self, request, graph_type, state_Abrv):

        type = graph_type
        if(type == "pieChart"):
            chart = pieChart(name=type, color_category='category20c', height=450, width=450)
            xdata = ["United States", state_Abrv]
            ydata = [12313411, int(request)]
            extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
            chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
        else:
            chart = multiBarChart(width=500, height=400, x_axis_format=None)
            xdata = ["United States", state_Abrv]
            ydata = [123411, int(request)]
            chart.add_serie(name="", y=ydata, x=xdata)
            chart.show_legend = False
            

        chart.buildcontent()
        result = chart.htmlcontent

        return result
        