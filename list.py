names = ["john", "brain", "mina", "daniel"]
names[0] = "solomon"

names.sort(reverse=True)
names.sort(key=str.casefold)
names.pop()   
names.append()
names.clear()
del names
 
print(names)