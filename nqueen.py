n=7
temp_list=[]
def isQueenSafe(r,c):
    count=0
    if(len(temp_list)==0):
        return True
    else:
        #print(temp_list)
        for x in range(len(temp_list)):
        #    print(temp_list[x],'value of x',r,'value of y',c)
            if((temp_list[x][0]!=r) and (temp_list[x][1]!=c)):
                if((temp_list[x][0]-r==temp_list[x][1]-c) or (temp_list[x][0]+temp_list[x][1]==r+c)):
         #          print('False') 
                   count+=1         
            else:
                count+=1   
       # print(count)
        if(count!=0):
            return False
        else:
            return True

def nQueen(r,c):
    while(c<n):
        if(isQueenSafe(r,c)==True):
            c+=1
        else:
            temp_list.append((r,c))
            if(r==n-1):
                return True
            else:
                rec=nQueen(r+1,0)
                if(rec==True):
                    return True
                else:
                    temp_list.pop()
                    c+=1
a=nQueen(0,0)
print(temp_list)
