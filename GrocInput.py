from ast import List
import time


class Task:
    def __init__(self, taskName: str, time: int, dependsOn: List = None):
        self.delay = time
        self.taskName = taskName

    def execute(self):
        print(f"Execute task '{self.taskName}' - {self.delay} sec")
        time.sleep(self.delay)


class TaskOrchestration:

    def __init__(self, tasks):
        self.tasks = tasks

    # 0 - sequential
    # 1 - simultaneous (not optimized)
    # 2 - simultaneous (optimized)
    def execute(self, seq: int = 0):
        # top_sort()
        if seq == 0:
            for task in self.tasks:
                task.execute()
        else:
            raise Exception("not implemented")


task1 = Task("Task 1", 3)
task2 = Task("Task 2", 1, [task1])
task3 = Task("Task 3", 5)
task4 = Task("Task 4", 1)

tasks = [task1, task2, task3, task4]
for t in tasks:
    t.execute()

# measure start time
start = time.time()
to = TaskOrchestration([task1, task2, task3, task4])
to.execute()
end = time.time()
print(f"Elapsed: {end - start}")
# measure end time

mapping = {"file.txt": "t_file"}
