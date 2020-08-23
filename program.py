def area_trapped_pipes(liste):
    length = len(liste)
    index = 0
    pipe = liste[index]
    area = 0
    while index != length-1:
        bo = False
        for j in range(index+1,length):
            if liste[j] >= pipe:
                bo = True
                break
        if bo :
            for k in range(index+1,j):
                area +=pipe-liste[k]
        index = j
        pipe = liste[index]
    return area
    
# liste = [5,4,5,3,2,1,6]
# area_trapped_pipes(liste)