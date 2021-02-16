

myfile = open("pelican.txt")
pelican_list = myfile.readlines()
each_item = [x[:-1] for x in pelican_list]

for i in pelican_list:
    each_item.append(i)

print(each_item)

number_elements = len(each_item)
print("Number of items in list: ", number_elements)

count = 0

for pelican_list in each_item:
    count += len(pelican_list)

print("Number of items in list: ", count)


for list in pelican_list:
    print(list)
