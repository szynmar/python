import itertools as it

data = [{'type': 'Alarm', 'action': 'WAIT'},
        {'type': 'Alarm', 'action': 'WAIT'},
        {'type': 'Error', 'action': 'TIMEOUT'},
        {'type': 'Error', 'action': 'STOP'},
        {'type': 'Alarm', 'action': 'WAIT'},
        {'type': 'Error', 'action': 'TIMEOUT'},
        {'type': 'Error', 'action': 'STOP'}]

# print dane rows with for
for row in data:
    print(row)

print("-"*10)
data = sorted(data, key = lambda x: x['type'])
for keyy, elements in it.groupby(data, key = lambda x: x['type']):
    # print(f"{keyy}: {list(elements)}")
    print(f"{keyy}: ({len(list(elements))})")
