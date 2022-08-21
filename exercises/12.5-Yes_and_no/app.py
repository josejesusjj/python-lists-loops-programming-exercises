theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def type_list(items):
    if items == 1:
        return 'wiki'
    elif items == 0:
        return 'woko'

print(list(map(type_list, theBools)))

