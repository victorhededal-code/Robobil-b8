TM_TIMER_INTERVAL = 1  # ms

#########################################################
# EVENT list
#########################################################
TASK_NAME = 0
TASK_INTERVAL = 1
TASK_TIMER = 2
TASK_CALLBACK = 3

#########################################################
# List of tasks
#########################################################
task_list = []


#########################################################
# Make Task list func
#########################################################
def create_task(task_name: str, task_interval: int, task_callback):
    list_temp = [task_name, task_interval, 0, task_callback]
    task_list.append(list_temp)


#########################################################
# Task manager isr updater
#########################################################
def tm_update_isr():
    global TM_TIMER_INTERVAL
    i = 0
    for this_task in task_list:
        if this_task[TASK_TIMER] > 0:
            this_task[TASK_TIMER] -= TM_TIMER_INTERVAL
            task_list[i] = this_task
        i += 1


#########################################################
# TM execute tasks
#########################################################
def tm_execute_task():
    i = 0
    for this_task in task_list:
        if this_task[TASK_TIMER] <= 0:
            this_task[TASK_TIMER] = this_task[TASK_INTERVAL]
            task_list[i] = this_task

            if (this_task[TASK_CALLBACK]):
                this_task[TASK_CALLBACK]()
        i += 1
