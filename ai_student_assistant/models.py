class TaskManager:
    def __init__(self):
        self.tasks = {}  # user-based storage

    def get_tasks(self, user):
        return self.tasks.get(user, [])

    def add_task(self, user, title):
        if not title:
            return

        if user not in self.tasks:
            self.tasks[user] = []

        self.tasks[user].append({
            "title": title,
            "done": False
        })

    def complete_task(self, user, task_id):
        if user in self.tasks and 0 <= task_id < len(self.tasks[user]):
            self.tasks[user][task_id]["done"] = True

    def delete_task(self, user, task_id):
        if user in self.tasks and 0 <= task_id < len(self.tasks[user]):
            self.tasks[user].pop(task_id)