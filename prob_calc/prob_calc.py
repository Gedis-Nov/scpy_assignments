#PROBABILITY CALCULATOR ASSIGNMENT 5
import random
import copy

class Hat:

    def __init__(self, **color):
        self.content = []
        for k,v in color.items():
            self.content += [k] * int(v)
            #for i in range(v): self.content.append(k)

    def draw(self, n):
        ln = len(self.content)
        if n >= ln: return self.content
        tmp = []
        for i in range(n):
            rn = random.randint(0, ln - 1)
            tmp.append(self.content.pop(rn))
            ln -= 1
        return tmp

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for e in range(num_experiments):
        ht = copy.deepcopy(hat)
        db = ht.draw(num_balls_drawn)
        d = {}
        for bal in db: d[bal] = d.get(bal, 0) + 1

        found = True
        for b, v in expected_balls.items():
            #if d.get(b, 0) < v or d.get(b, 0) > v:
            if d.get(b, 0) < v:
                found = False
                break

        if found: count += 1

    return count / num_experiments
