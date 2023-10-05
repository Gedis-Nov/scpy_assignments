#BUDGET APP ASSIGNMENT 3

class category:
    
    def __init__(self, cat):
        self.name = cat
        self.balance = 0
        self.ledger = []
        print((self.name.upper() + ' CATEGORY IS CONSTRUCTED').center(30))
        print('*' * 30, '\n')

    def deposit(self, dpa, desc=''):
        for k,v in catdict.items():
            if k == dcat: catdict[k] += dpa
        self.balance += dpa
        self.ledger.append({'Amount': dpa, 'Description': desc})

        ln = len('DEPOSIT TO ' + self.name.upper() + ' BUDGET IS SUCCESSFUL')
        print(('DEPOSIT TO ' + self.name.upper() + ' BUDGET IS SUCCESSFUL'))
        print(('*' * ln), '\n')

    def withdraw(self, wa, desc=''):
        if not self.check_funds(wa):
            print('This amount', wa, 'cannot be processed. INSUFFICIENT FUNDS!', '\n')
            print('{:*^30}'.format(self.name.upper()))
            return False

        for k,v in catdict.items():
            if k == sob: catdict[k] -= wa
        self.balance -= wa
        self.ledger.append({'Amount': -wa, 'Description': desc})

        ln = len('WITHDRAWAL FROM ' + self.name.upper() + ' BUDGET IS SUCCESSFUL')
        print('WITHDRAWAL FROM ' + self.name.upper() + ' BUDGET IS SUCCESSFUL')
        print(('*' * ln), '\n')
        return True

    def get_balance(self):
        print('{:*^30}'.format(self.name.upper()))
        print('{:<8}{:>22.2f}'.format('Balance:', self.balance))
        return self.balance

    def transfer(self, ta, dcat):
        if not self.withdraw(ta, 'Transfer to ' + dcat.upper()): return False
        d1 = 'Transfer from ' + self.name.upper()
        exec('{}{}'.format(dcat, '.deposit(ta, d1)'))

        ln = len('TRANSFER FROM ' + self.name.upper() + ' BUDGET TO ' + dcat.upper() + ' BUDGET IS SUCCESSFUL')
        print('TRANSFER FROM ' + self.name.upper() + ' BUDGET TO ' + dcat.upper() + ' BUDGET IS SUCCESSFUL')
        print(('*' * ln), '\n')
        return True

    def check_funds(self, cfa):
        return self.balance >= cfa

    def spent(self):
        spa = 0
        print('{:*^30}'.format(self.name.upper()))
        for t in self.ledger:
            if t['Amount'] < 0: spa += t['Amount']
        print(('{:<22}{:>8.2f}'.format('Total spent: ', spa)), '\n')

    def __str__(self):
        slip = ['{:*^30}'.format(self.name.upper())]
        for t in self.ledger:
            slip.append('{:<22}{:>8.2f}'.format(t['Description'][:22], t['Amount']))
        slip.append('{:<22}{:>8.2f}'.format('Closing balance:', self.balance))
        print('\n'.join(slip))

#PROGRAM STARTUP
catdict = {}
def acc():
    print('EXISTING BUDGET ACCOUNTS')
    print('*' * 24)
    for k,v in catdict.items(): print('{:<16}{:>8.2f}'.format(k, v))
    print('')

while True:
    print('')
    print('DP - DEPOSIT')
    print('WT - WITHDRAWAL')
    print('GB - GET_BALANCE')
    print('TR - TRANSFER')
    print('SP - TOTAL SPENT BALANCE')
    print('PS - PRINT STATEMENT')
    print('EX - EXIT PROGRAM', '\n')
    op = input('PLEASE INPUT THE SHORT CODE FOR OPERATION: ')
    print('')

    if op == 'DP':
        acc()
        dcat = input('ENTER A NEW / EXISTING BUDGET NAME: ')
        dpa = float(input('ENTER THE AMOUNT TO BE DEPOSITED. NUMBERS ONLY: '))
        desc = input('ENTER THE DESCRIPTION OF THE DEPOSIT: ')
        print('')
        #ADDS NEW BUDGET ACCOUNTS AND CREATES VARIABLE FOR THE INPUT STRING
        if not dcat in catdict:
            vars = locals()
            catdict[dcat] = 0
            vars[dcat] = category(dcat)
        exec('{}{}'.format(dcat, '.deposit(dpa, desc)'))

    elif op == 'WT':
        acc()
        sob = input('ENTER SOURCE BUDGET ACCOUNT NAME: ')
        wa = float(input('ENTER THE AMOUNT TO BE WITHDRAWN. NUMBERS ONLY: '))
        desc = input('ENTER THE DESCRIPTION OF THE WITHDRAWAL: ')
        print('')
        exec('{}{}'.format(sob, '.withdraw(wa, desc)'))

    elif op == 'GB':
        acc()
        sob = input('ENTER SOURCE BUDGET ACCOUNT NAME: ')
        print('')
        exec('{}{}'.format(sob, '.get_balance()'))

    elif op == 'TR':
        acc()
        sob = input('ENTER SOURCE BUDGET ACCOUNT NAME: ')
        dcat = input('ENTER TARGET BUDGET ACCOUNT NAME: ')
        ta = float(input('ENTER THE AMOUNT TO BE TRANSFERED. NUMBERS ONLY: '))
        print('')
        exec('{}{}'.format(sob, '.transfer(ta, dcat)'))

    elif op == 'SP':
        acc()
        sob = input('ENTER SOURCE BUDGET ACCOUNT NAME: ')
        print('')
        exec('{}{}'.format(sob, '.spent()'))

    elif op == 'PS':
        acc()
        sob = input('ENTER SOURCE BUDGET ACCOUNT NAME: ')
        print('')
        exec('{}{}'.format(sob, '.__str__()'))

    elif op == 'EX': break
