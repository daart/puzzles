def haveConflict(event1, event2):
    return event1[0] <= event2[1] and event2[0] <= event1[1]

t1 = haveConflict(["01:15","02:00"], ["02:00","03:00"])
t2 = haveConflict(["01:00","02:00"], ["01:20","03:00"])
t3 = haveConflict(["10:00","11:00"], ["14:00","15:00"])