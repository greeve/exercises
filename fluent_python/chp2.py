# Example 2.4
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
more_tshirts = [(color, size) for size in sizes for color in colors]
print('tshirts: ', tshirts)
print('more_tshirts: ', more_tshirts)

r = [x for x in range(10)]
s = [x for x in range(5)]
print(r)
print(s)
print(r * 4)
