#PY4E TIME CALCULATOR ASSIGNMENT.

def add_time(start, duration, day=False):
    #BREAK STRING INPUTS & ASSIGN INTEGERS TO VARIABLES.
    try:
        strt = start.split()
        dur = duration.split(':')
        t0 = strt[0].split(':')
        hr1 = int(t0[0])
        mnt1 = int(t0[1])
        hr2 = int(dur[0])
        mnt2 = int(dur[1])
        ampm = strt[1]
    except:
        print('Please enter the correct time formats, eg. 3:00 PM, 3:10, Monday')
        return 'Please enter the correct time formats, eg. 3:00 PM, 3:10, Monday'

    #CONVERT DURATION TIME INTO MINUTES
    mnt3 = (hr2 * 60) + mnt2
    #CALCULATE NEW TIME
    ndays = 0
    while mnt3 > 0 :
        #ADDING MINUTES TOGETHER
        mnt1 += 1
        mnt3 -= 1
        if mnt1 == 60 :
            mnt1 = 0
            hr1 += 1
        #ADDING HOURS, DAYS & TIME OF DAY
        if hr1 == 12 :
            hr1 = 0
            if ampm == 'AM' :
                ampm = 'PM'
            else :
                ampm = 'AM'
                ndays += 1

    if hr1 == 0 : hr1 = 12
    ans = str(hr1) + ':' + str(f'{mnt1:02}') + ' ' + ampm
    ndl = '(n days later)'
    nod = ndl.replace('n', str(ndays), 1)

    #PRINT THE NEW TIME DEPENDING ON THE DAY OF WEEK INPUT
    ans1 = None
    new_time = None
    if day :
        #LOCATE THE DAY OF THE WEEK
        ky = 0
        dayy = None
        dayy = day.lower()
        daysow = {'monday' : 1, 'tuesday' : 2, 'wednesday' : 3, 'thursday' : 4, 'friday' : 5, 'saturday' : 6, 'sunday' : 7}
        for key,val in daysow.items() :
            if key == dayy :
                ky = val
                break
        #CALCULATE NEW DAY VALUE
        nndays = ndays
        if ky == 7 : ky = 0
        while nndays > 0 :
            ky += 1
            nndays -= 1
            if ky == 7 : ky = 0
        if ky == 0 : ky = 7
        #LOCATE THE KEY AND VALUE IN DICTIONARY
        dow = ''
        daysow1 = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
        for key,val in daysow1.items() :
            if val == ky :
                dow = key
                break

        #STRINGING ANDWERS TOGETHER
        ans1 = ans + ','
        dow1 = ' ' + dow
        if ndays == 0 :
            new_time = ans1 + dow1
        elif ndays == 1 :
            new_time = ans1 + dow1 + (' ' + '(next day)')
        elif ndays > 1 :
            new_time = ans1 + dow1 + (' ' + nod)
    else :
        if ndays == 0 :
            new_time = ans
        elif ndays == 1 :
            new_time = ans + (' ' + '(next day)')
        elif ndays > 1 :
            new_time = ans + (' ' + nod)

    print(new_time)

#PROGRAM STARTUP PAGE
while True:
    start = input('Enter the start time:')
    duration = input('Enter the duration time:')
    day = input(''''OPTIONAL' Enter the day of the week:''')
    break
add_time(start, duration, day)
