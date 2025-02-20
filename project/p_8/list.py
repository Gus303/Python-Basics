animals = ['dog', 'cat', 'bird']
print(animals)
print(type(animals))

print(animals[0])
print(len(animals))

more_animals = ['duck', 'hamster', 'fish']

new_list = animals + more_animals
print(new_list)

new_list.append('frog')
print(new_list)

print(new_list.sort)

new_list.insert(3, 'lion')
new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)

numbers = [1, 2, 3, 4]
print(numbers)
print(max(numbers))
print(min(numbers))

numbers.append(5)
print(numbers)