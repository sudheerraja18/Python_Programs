
tmp_list1 = []
with open('text_file.txt','r') as file:
    for line in file:
        temp = line.rstrip('\n')
        tmp_list1.append(temp.lower())
        
word_dict = {}
for line in tmp_list1:
    line_split = line.split()
    for word in line_split:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1

tmp_list2 = []    
for key,value in word_dict.items():
    if value == 1:
        tmp_list2.append(key)
print (tmp_list2)
     
