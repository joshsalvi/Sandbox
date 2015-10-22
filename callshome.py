def total_cost(calls):
    import math
    coins = 0
    calltimeperday = 0
    calltimes = []
    day0 = ''
    days = 0
    for ind in range(0, len(calls)):
        callinfo = calls[ind].split(' ')
        if str(callinfo[0]) != day0:
            calltimes.append(calltimeperday)
            days += 1
            day0 = str(callinfo[0])

            calltimeperday = int(math.ceil(int(callinfo[2]) / 60.))
        elif ind == len(calls) - 1:
            calltimeperday += int(math.ceil(int(callinfo[2]) / 60.))
            calltimes.append(calltimeperday)

        else:
            calltimeperday += int(math.ceil(int(callinfo[2]) / 60.))
    else:
        if calltimeperday != calltimes[len(calltimes) - 1]:
            calltimes.append(calltimeperday)
        elif days != len(calltimes) - 1:
            calltimes.append(calltimeperday)
    for item in calltimes:
        if item <= 100:
            coins += item
        else:
            coins += 100 + (item - 100) * 2
    return coins


print total_cost(
    ("2051-09-09 12:00:00 1",
     "2051-09-10 12:00:00 1",
     "2051-09-12 12:00:00 1",
     "2051-09-14 12:00:00 1",
     "2051-09-15 12:00:00 1",
     "2051-09-18 12:00:00 1",
     "2051-09-23 12:00:00 1",
     "2051-09-25 12:00:00 1",
     "2051-09-28 12:00:00 1",
     "2051-10-01 12:00:00 1",
     "2051-10-02 12:00:00 1",
     "2051-10-04 12:00:00 1",
     "2051-10-05 12:00:00 1",
     "2051-10-06 12:00:00 1",
     "2051-10-07 12:00:00 1",
     "2051-10-08 12:00:00 1",
     "2051-10-09 12:00:00 1",
     "2051-10-10 12:00:00 1",
     "2051-10-11 12:00:00 1",
     "2051-10-12 12:00:00 1",
     "2051-10-13 12:00:00 1",
     "2051-10-14 12:00:00 1",
     "2051-10-15 12:00:00 1",
     "2051-10-16 12:00:00 1",
     "2051-10-17 12:00:00 1",
     "2051-10-18 12:00:00 1",
     "2051-10-19 12:00:00 1",
     "2051-10-20 12:00:00 1",
     "2051-10-21 12:00:00 1",
     "2051-10-22 12:00:00 1"))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
