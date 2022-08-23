def lyrics_generator(item):
    lyric = ''
    counter = 0
    for x in item:
        if x == 0:
            lyric += 'Boom '
        elif x == 1:
            lyric += 'Drop the base '
            counter +=1
            if counter == 3:
                lyric += '!!!Break the base!!! '
                counter = 0
    return lyric


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))