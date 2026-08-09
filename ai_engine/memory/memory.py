class MemoryStore:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def remember(self, item):
        self.short_term.append(item)

    def recall(self):
        return self.short_term
