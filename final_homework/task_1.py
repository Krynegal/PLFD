class Stack:
    def __init__(self):
        self.__list = list()

    def push(self, el):
        self.__list.append(el)

    def pop(self):
        if len(self.__list) == 0:
            return
        return self.__list.pop()

    def __str__(self):
        return str(", ".join(self.__list))


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        res = ""
        for k in sorted(self.task.keys()):
            res += str(k) + " " + str(self.task[k]) + ";\n"
        return res

    def new_task(self, task, priority):
        if priority not in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].add(task)
        else:
            new_stack = Stack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.push(value)
            new_stack.push(task)
            self.task[priority] = new_stack

    def delete_task(self, priority):
        if priority not in self.task.keys():
            print("Задачи с таким приоритетом не существует")
            return

        print(f"Удалена задача: {self.task[priority].pop()}")
        if len(str(self.task[priority])) == 0:
            self.task.pop(priority)


if __name__ == "__main__":
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)
    manager.new_task("сделать уборку", 4)
    manager.delete_task(4)
    manager.delete_task(1)
    print(manager)
