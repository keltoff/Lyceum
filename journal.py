# class to record character´s progress, quest, and discoveries


class Journal:
    def __init__(self):
        self.mysteries = dict()

    def discover(self, mystery, knowledge=0, hint=None):
        if mystery not in self.mysteries:
            self.mysteries[mystery] = Mystery(mystery)

        self.mysteries[mystery].learn(knowledge, hint)


class Mystery:
    def __init__(self, name):
        self.name = name
        self.hints = []
        self.knowledge = 0

    def learn(self, knowledge=0, hint=None):
        if hint:
            self.hints.append(hint)

        self.knowledge += knowledge

    def __str__(self):
        return 'Mystery: {}\n{}'.format(self.name, '\n'.join([' - ' + h for h in self.hints]))
