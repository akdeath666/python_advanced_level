N=int(input("ENTER NO. OF TERMS TO BE PRINT THE FIBONACCI SERIES: "))
a=0
b=1
sum=a+b

#HERE I AM PRINTING FIRST THREE TERMS THEN I WILL USE RECURSION TO PRINT NEXT TERMS
print(a,b,sum,sep=" ",end=" ")
a=b
b=sum

def fiboNacci(a,b,n):
    '''FIBONACCI SERIES PRINTING BY RECURSION'''
    if(n==0):
        return 
    else:
        sum=a+b
        print(sum,end=" ")
        return fiboNacci(a=b,b=sum,n=n-1) 

#print(fiboNacci.__doc__)  BY USING WE CAN PRINT DOCSTRING ALSO

fiboNacci(a,b,N-3)

    