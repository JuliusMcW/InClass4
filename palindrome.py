
def pal(a):
    str(a)
    y=0
    z=len(a)-1;
    x=0
    while(y<len(a)/2 and x==0):
        if(a[y]==a[z]):
            x=0
        else:
            x=1
        y=y+1
        z=z-1
    if(x==1):
        return False
    else:
        return True
        
