#Q1: 1.	Return all the duplicate values from list of arraylist
#Input:   [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
l=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in l:   #getting each individusal list
    #print(l1)
    new_dict, new_list = {}, []

    for j in i:
        if not j in new_dict:
            new_dict[j] = 1
        else:
            new_dict[j] += 1

    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)
    print(new_list)

#Q2:

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        x=i+j
        print(x)

#Q3:

#Q4:
Keys = ['Ten','Twenty','Thirty']
Value = [10,20,30]

Dic=dict() #Created an empty dictionary
for i in range(len(Keys)):  #put values
    Dic[Keys[i]]=Value[i]

print(Dic)

#Q5:

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print('After Merging: ')
print(dict1 | dict2)  # using  | operator to merge

#Q6:
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict['location']=sampleDict.pop('city')  #changing old key with new one using pop
print(sampleDict)

#Q7:
dic={'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
li=list(dic.items())
print(li)






