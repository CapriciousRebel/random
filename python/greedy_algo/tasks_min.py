max_time = int(input("Enter the time: "))

file = open("tasks.txt", "r")
tasks = []

while 1:
    line = file.readline()
    if(line):

        task_time = line.split(',')
        task = task_time[0]
        time = int(task_time[1].rstrip("\n"))
        tasks.append((task, time))
    else:
        break


def get_next_task(tasks, time_remaining):

    min_time = tasks[0][1]
    task_min = tasks[0]

    for task in tasks:

        if task[1] <= min_time:
            min_time = task[1]
            task_min = task

    if min_time <= time_remaining:
        return tasks.index(task_min)
    return -1


def make_schedule(tasks, t):

    to_do = []
    time_remaining = t
    done = False

    while time_remaining and not done:

        next_task_index = get_next_task(tasks, time_remaining)

        if next_task_index >= 0:
            to_do.append(tasks[next_task_index][0])
            time_remaining -= tasks[next_task_index][1]
            tasks.remove(tasks[next_task_index])
        else:
            done = True
    return to_do


print(make_schedule(tasks, max_time))
