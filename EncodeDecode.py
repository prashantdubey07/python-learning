# Python code​​​​​​‌‌​‌‌‌​​​​‌‌‌‌​‌‌​‌​‌​​‌​ below

def encodeString(stringVal):
    # Your code goes here.
    i = -1
    list = []
    counter = 1
    prevChar = None
    for char in stringVal:
        if char != prevChar:
            i = i+1;
            prevChar = char
            list.insert(i,(char , 1))
        else:
            x = list[i][1]
            list[i] = (char, x+1)
    return list

def decodeString(encodedList):
    # Your code goes here.
    result = ''
    for item_tuple in encodedList:
        result = result + (item_tuple[0]* item_tuple[1])
    return result
