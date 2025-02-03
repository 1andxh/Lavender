# list tutorials - 29/01/2025

futureCars = ['tesla', 'BMW', 'audi', 'mercedes', 'audi' 'ford', 'toyota', 'audi']
futureCars[4] = "chevrolet"
print(futureCars[:4])
futureCars.pop(4)
futureCars.append('honda')
print(futureCars)
for car in futureCars:
    if 'audi' in futureCars:
        futureCars.remove('audi')

print(futureCars)
