def read_file_content():
    myfile = open("story.txt")
    contents = myfile.read()
    print(contents)
    

    

    return contents
read_file_content()  


def count_words():
    text= open("story.txt")
    d = dict()

    for line in text:
        line= line.strip()
        line= line.lower()
        words= line.split(" ")
        
        for word in words:
            if word in d:
                d[word]= d[word]+1
            else:
                d[word]= 1

    for key in list(d.keys()):
        print(key,": ",d[key])

    return (key,": ",d[key])
count_words()


