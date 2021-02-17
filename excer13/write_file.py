

myfile = open("pelican.txt", "a+")
myfile.write("A wonderful bird is the pelican.")
myfile.write(" His bill holds more than his belican")

lines = [" He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
#\n adds the line breaks in

myfile.writelines(lines)
myfile.close()


myfile = open("pelican.txt", "r")
print(myfile.read())