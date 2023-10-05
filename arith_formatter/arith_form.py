#arithmetic calculator app assignment 1

def arithmetic_arranger(problems, answers=False):

    #IF LOOP TO SOLVE TOO MANY PROBLEMS IN PROBLEMS LIST.
    if len(problems) > 5: return 'Error: Too many problems.'

    #FOR LOOP TO GO THROUGH EACH ENTRY IN PROBLEMS LIST.
    fans = []
    for problem in problems:
        #FOR LOOP TO SOLVE OPERATOR PROBLEM & SOLVE ANSWER.
        for char in problem:
            if '/' in char or '*' in char: return "Error: Operator must be '+' or '-'."

        #SPLITTING PROBLEM & ASSIGNING CHARACTERS TO VARIABLES.
        probx = problem.split()
        num1 = probx[0]
        num2 = probx[2]
        op = probx[1]

        #SOLVING MAXIMUM DIGITS ERROR.
        if len(num1) > 4 or len(num2) > 4: return 'Error: Numbers cannot be more than four digits.'

        #TO SET UP CORRECT LENGTH FORMATTING.
        if len(num1) >= len(num2): ln = len(num1)
        else: ln = len(num2)

        #IF LOOP SOLVING EACH PROBLEM & SOLVING NUMBERS MUST BE DIGITS ONLY.
        if op == '+':
            try: ans = str(int(num1) + int(num2))
            except: return 'Error: Numbers must only contain digits.'
        else:
            try: ans = str(int(num1) - int(num2))
            except: return 'Error: Numbers must only contain digits.'

        #BUILDING FINAL ANSWER FORMATTING.
        if len(fans) == 0:
            fans.append(num1.rjust(ln + 2))
            fans.append(op + num2.rjust(ln + 1))
            fans.append('-' * (ln + 2))
            if answers: fans.append(ans.rjust(ln + 2))
        else:
            fans[0] += '    ' + num1.rjust(ln + 2)
            fans[1] += '    ' + op + num2.rjust(ln + 1)
            fans[2] += '    ' + '-' * (ln + 2)
            if answers: fans[3] += '    ' + ans.rjust(ln + 2)

    return '\n'.join(fans)
