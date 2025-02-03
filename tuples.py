# tuples and sets
# packing and unpacking = assigning elements in a tuple to a variable
meds = ['tylenol', 'paracetamol', 'asprin', 'panadol']
(morningMeds, afternoonMeds, eveningMeds, nightMeds) = meds

(first_med, second_med, *rest) = meds
print(first_med)
print(second_med)
print(rest)
print(type(rest))