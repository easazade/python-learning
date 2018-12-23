import datetime
import time

now = datetime.datetime
print(now.now())
before = datetime.datetime(2017, 12, 24, 14, 45, 56)
print(before)
time_delta = now.now() - before
print(time_delta)
print(time_delta.days)
print(time_delta.total_seconds())
# adding time to datetime
after = now.now() + datetime.timedelta(days=4)
print(after)

# time

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    print(lst)
    time.sleep(1)
