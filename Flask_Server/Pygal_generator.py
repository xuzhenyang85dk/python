import pygal

def createPie(data, title):

    pie_chart = pygal.Pie()
    pie_chart.title = title
    for key, value in data.items():
        pie_chart.add(key,value)
    return pie_chart.render_data_uri()


'''    pie_chart = pygal.Pie()
pie_chart.title = 'Browser usage in February 2012 (in %)'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)
pie_chart.render() '''

'''Takes a dictionary of countries and values'''
def createMap(title, data):

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = title
    worldmap_chart.add('1kg Bananas in DKK', data)

    return worldmap_chart.render_data_uri()

    '''.render_to_file('./data/map.svg')'''
