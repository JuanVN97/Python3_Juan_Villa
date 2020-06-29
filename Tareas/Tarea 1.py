def sortFuntion(t):
    band=0
    for i in t:
        if (isinstance(i, int)) == True:
            band += 1
        else:
            band=0
    t2 = t.copy()
    lengt = len(t)
    if band == lengt:
        while lengt != 0:
            number = max(t)
            t2.insert(lengt, number)
            pos = t2.index(number)
            t2.pop(pos)

            pos2 = t.index(number)
            t.pop(pos2)

            lengt -= 1
    print(t2)

if __name__ == '__main__':
    t = [4, 7, 6, 9, 5, 8, 2, 1, 3]
    sortFuntion(t)