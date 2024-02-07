from collections import deque

textile_collection = deque(int(x) for x in input().split())
medicaments = deque(int(y) for y in input().split())

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textile_collection and medicaments:
    current_textile = textile_collection.popleft()
    current_medicament = medicaments.pop()

    result = current_textile + current_medicament

    if result == 30:
        items['Patch'] += 1
    elif result == 40:
        items['Bandage'] += 1
    elif result == 100:
        items['MedKit'] += 1
    elif result > 100:
        items['MedKit'] += 1
        remainder = result - 100
        medicaments[-1]+=remainder
    else:
        current_medicament += 10
        medicaments.append(current_medicament)


if not textile_collection and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not medicaments:
    print("Medicaments are empty.")

elif not textile_collection:
    print("Textiles are empty.")

sorted_dictionary = sorted(
    items.items(),
    key=lambda x: (-x[1],x[0])
)

for key,value in sorted_dictionary:
    if value >0:
        dictionary_result = f'{key} - {value}'
        print(dictionary_result)

if medicaments:
    reversed_mediks = deque(reversed(medicaments))
    print(f'Medicaments left: {", ".join(map(str,reversed_mediks))}')
if textile_collection:
    print(f"Textiles left: {', '.join(map(str,textile_collection))}")