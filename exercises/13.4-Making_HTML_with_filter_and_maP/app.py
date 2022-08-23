all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(item):
	return item['sexy'] == True
def generate_li(color):
	return '<li>'+color['label']+'<li>'

selector = list(filter(filter_colors,all_colors))
writer = list(map(generate_li,selector))
print(writer)
