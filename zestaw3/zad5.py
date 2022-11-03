
class Bug:
    counter = 0
    def __init__(self):
        Bug.counter += 1
        self.id = Bug.counter
    def __del__(self):
        print("Bug id: " + str(self.id) + " counter: " + str(Bug.counter) + " deleted")
        Bug.counter -= 1
        del self
    def __str__(self):
        return "Bug id: " + str(self.id) + " counter: " + str(Bug.counter)

bugs = []
for i in range(100):
 bugs.append(Bug())
 print(bugs[-1])

