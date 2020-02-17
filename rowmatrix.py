list2work = [[1,2,3],[4,5,6],[7,8,9]]

updated_list = []
count = 0

def updatelist(test):
    temp_list=[]
    for element in test:
        temp_list.append(element[count])
    updated_list.append(temp_list)

for l in range(len(list2work)):
    updatelist(list2work)
    count+=1

print(updated_list)

