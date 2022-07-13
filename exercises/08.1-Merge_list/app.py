chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_chunk = []
    for i in chunk_one:
        new_chunk.append(i)
    for i in chunk_two:
        new_chunk.append(i)
    return new_chunk

    
print(merge_list(chunk_one, chunk_two))
