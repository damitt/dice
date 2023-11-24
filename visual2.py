from logic2 import dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice1 = dice()
dice2 = dice(10)
results = []
for i in range(10000):
    result = dice1.roll()+dice2.roll()
    results.append(result)

frequencies = []
max_result = dice1.side+dice2.side
for i in range(2, max_result+1):
    frequency = results.count(i)
    frequencies.append(frequency)
# print(frequencies)

x_sides = list(range(2, max_result+1))
dataset = [Bar(x=x_sides,y=frequencies)]

x_axis_config = {'title': 'sides', 'dtick': 1}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title='result dice6', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': dataset, 'layout': my_layout}, filename='d62.html')
