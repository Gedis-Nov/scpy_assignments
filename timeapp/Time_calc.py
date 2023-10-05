#PY4E TIME CALCULATOR ASSIGNMENT.

def add_time(start, duration, day=False):
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
        return 'Please enter the correct time formats, eg. 3:00 PM, 3:10, Monday'

    #CONVERT DURATION TIME INTO MINUTES & CALCULATING NEWW TIME.
    mnt3 = (hr2 * 60) + mnt2
    ndays = 0
    while mnt3 > 0 :
        mnt1 += 1
        mnt3 -= 1
        if mnt1 == 60 :
            mnt1 = 0
            hr1 += 1
        if hr1 == 12 :
            hr1 = 0
            if ampm == 'AM' : ampm = 'PM'
            else :
                ampm = 'AM'
                ndays += 1

    if hr1 == 0 : hr1 = 12
    ans = str(hr1) + ':' + str(f'{mnt1:02}') + ' ' + ampm
    ndl = '(n days later)'
    nod = ndl.replace('n', str(ndays), 1)

    #PRINT THE NEW TIME DEPENDING ON THE DAY OF WEEK INPUT
    if day :
        dy = day.capitalize()
        daysow = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
        for key,val in daysow.items() :
            if key == dy : ky = val

        dys = ndays
        if ky == 7 : ky = 0
        while dys > 0 :
            ky += 1
            dys -= 1
            if ky == 7 : ky = 0
        if ky == 0 : ky = 7

        for key,val in daysow.items() :
            if val == ky :
                dow = key

        #STRINGING ANDWERS TOGETHER
        if ndays == 0 : new_time = '{}, {}'.format(ans, dow)
        elif ndays == 1 : new_time = '{}, {} (next day)'.format(ans, dow)
        elif ndays > 1 : new_time = '{}, {} {}'.format(ans, dow, nod)
    else :
        if ndays == 0 : new_time = ans
        elif ndays == 1 : new_time = '{} (next day)'.format(ans)
        elif ndays > 1 : new_time = '{} {}'.format(ans, nod)

    return new_time
