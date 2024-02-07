from collections import deque

time_per_task = deque(int(x) for x in input().split())
numbers_of_tasks = deque(int(y) for y in input().split())

duky_dictionary = {'Darth Vader Ducky':0,'Thor Ducky':0,'Big Blue Rubber Ducky':0,'Small Yellow Rubber Ducky':0}

while time_per_task and numbers_of_tasks:
    current_time = time_per_task.popleft()
    current_task = numbers_of_tasks.pop()

    result = current_time * current_task

    if 0 <= result <= 60:
        duky_dictionary['Darth Vader Ducky']+= 1

    elif 61<=result<=120:
        duky_dictionary['Thor Ducky'] +=1

    elif 121 <= result <= 180:
        duky_dictionary['Big Blue Rubber Ducky'] +=1

    elif 181<=result<=240:
        duky_dictionary['Small Yellow Rubber Ducky']+=1

    elif result > 240:
        current_task -= 2
        numbers_of_tasks.append(current_task)
        time_per_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for key,value in duky_dictionary.items():
    print(f'{key}: {value}')




