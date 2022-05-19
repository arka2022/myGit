'''
#Q1:

sol=    lambda a,b,c,x:(a*(x*x)+b*x+c)
print(sol(1,2,3,4))
'''

'''
#Q2:
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

def cn(li1):
    return li1.count("a")
print(cn(l1))

for i in lst1:
    print('Occurance of A in string %s is'%(i),cn(i)) #placeholder, use %s

'''
#@2:
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

def count1(x):
    count=0
    for i in range(len(lst1)):
        count=count+lst1[i].count(x)
    return (count)

a=list(map(lambda x:count1(x), ["A","a"]))
print(a)

'''
#Q3:
li3=[1,-2,3,4,-7,-8]

def posit(number):
    if number<0:
        return True
    else:
        return False
newLis1=filter(posit,li3)
l4=[]
for i in newLis1:
    l4.append(abs(i))

print(l4)
'''
#Q4:



'''
#Q5:
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
x=zip(lst1,lst2)
#for i in x:
#    print(i)

y=dict(x)
print('Following Dictionary:  ',y)
'''





