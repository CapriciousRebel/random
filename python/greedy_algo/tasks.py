# prompt for the time input
max_time = int(input("Enter the time: "))

# open the file, and initiate an empty list for tasks
file = open("tasks.txt", "r")
tasks = []

# read all the lines from the file
while 1:
    line = file.readline()
    if(line):

        task_time = line.split(',')              # split the line about ','
        task = task_time[0]                      # store the task
        time = int(task_time[1].rstrip("\n"))    # typcast the time into integer, after removing the '\n'
        tasks.append((task, time))               # save each line as a tuple in the list
    else:
        break


def get_next_task(tasks, time_remaining):
    '''
    returns the next task which can be done in the time remaining
    '''
    for task in tasks:
        if task[1] <= time_remaining:
            return tasks.index(task)
    return -1


def make_schedule(tasks, t):
    '''
    returns the list of tasks possible in the given time
    '''

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

# Driver code
print(make_schedule(tasks, max_time))
