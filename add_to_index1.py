index =[]
def isKeywordPresent(single_list,keyword,url):
    for single_list in index:
        if keyword is single_list[0]:
            if url not in single_list[1]:
                single_list[1].append(url)
            return True
    return False

def add_to_index(index,keyword,url):
    # if len(index)==0:
    #     newlist=[keyword,[url]]
    #     index.append(newlist)
    if not isKeywordPresent(index,keyword,url):
        newlist=[keyword,[url]]
        index.append(newlist)
    return index

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')

print index
