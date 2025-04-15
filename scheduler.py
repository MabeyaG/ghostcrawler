class Scheduler:
    def __init__(self, urls):
        self.queue = list(urls)

    def get_next(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0