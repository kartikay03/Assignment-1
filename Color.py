color_list= [ 'Red', 'Green', 'White' , 'Black' , 'Pink' , 'Yellow' ]
new_list=[]
for index, value in enumerate(color_list):
    if index not in [3]:
       new_list.append(value)
print(new_list)