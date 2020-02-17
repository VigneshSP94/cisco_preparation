list2find = [2,45,23,1,23,45,67,45,1]

no_dups = []

for index in range(len(list2find)-1):
    dups = []
    for element in list2find:
        if list2find[index] == list2find[list2find.index(element)+1]:
            dups.append(list2find[index])
    if len(dups) == 0:
        no_dups.append(list2find[index])
    dups=[]

print(no_dups)