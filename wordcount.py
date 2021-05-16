def count(word):
    x=0
    y=0
    while(x<len(word)):
        if(word[x]==' '):
            y=y+1
        x=x+1
    y=y+1
    return y   
