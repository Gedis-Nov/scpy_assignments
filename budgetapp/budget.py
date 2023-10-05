#BUDGET APP ASSIGNMENT 3

#CATEGORY CLASS THAT HAS METHODS IN IT TO RUN BUDGET OPERATIONS.
class category:

    def __init__(self, cat):
        self.name = cat
        self.balance = 0
        self.ledger = []

    def deposit(self, dpa, desc=''):
        self.balance += dpa
        self.ledger.append({'amount': dpa, 'description': desc})

    def withdraw(self, wa, desc=''):
        if not self.check_funds(wa): return False
        self.balance -= wa
        self.ledger.append({'amount': -wa, 'description': desc})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, ta, dcat):
        if not self.withdraw(ta, 'Transfer to ' + dcat.name): return False
        dcat.deposit(ta, 'Transfer from ' + self.name)
        return True

    def check_funds(self, wa):
        return self.balance >= wa

    def spent(self):
        spa = 0
        for t in self.ledger:
            if t['amount'] < 0: spa += t['amount']
        return spa

    def __str__(self):
        slip = [f'{self.name:*^30}']
        for t in self.ledger:
            slip.append('{:<23}{:>7.2f}'.format(t['description'][:23], t['amount']))
        slip.append('Total: ' + str(self.balance))
        return '\n'.join(slip)

#FUNCTION SPEND CHART THAT ADAPTS METHODS FROM THE CATEGORY CLASS AND TAKES
#A LIST OF CATEGORIES AS AN ARGUMENT.

def create_spend_chart(cates):
    spnt = [c.spent() for c in cates]
    totspnt = sum(spnt)
    perc = [a/totspnt * 100 for a in spnt]

    #LOOPS THAT CREATE THE TOP HALF OF THE CHART.
    chrt = ['Percentage spent by category']
    for i in range(11):
        lvl = 10 * (10 - i)
        lbar = '{:>3}| '.format(lvl)
        for p in perc: lbar += 'o  ' if p >= lvl else '   '
        chrt.append(lbar)

    #LOOPS TO CREATE THE MIDDLE BAR OF THE CHART.
    mbar = (' ' * 4) + '-'
    for c in cates: mbar += '---'
    chrt.append(mbar)

    #LOOPS TO CREATE THE BOTTOM HALF OF CHART.
    nam = [c.name for c in cates]
    n = max(map(len, nam))
    for i in range(n):
        bbar = ' ' * 5
        for s in nam: bbar += (s[i] + '  ') if len(s) > i else '   '
        chrt.append(bbar)
    return '\n'.join(chrt)
