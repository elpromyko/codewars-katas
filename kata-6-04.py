"""
Please complete the method which is provided with mirror time as string, and return the real time as string.

The return time value should always be between 1<= time < 13. This is the convenient way that human read the clock.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

"""
def what_is_the_time(time_in_mirror):
    time_split = time_in_mirror.split(':')
    if time_split[0] != '12':
        minutes = int(time_split[0]) * 60 + int(time_split[1])
    else:
        minutes = int(time_split[1])

    mirror_hour = int((720 - minutes) / 60)
    mirror_minute = (720 - minutes) % 60

    if mirror_hour == 0:  # works but need to written in a better way
        mirror_hour = 12

    return "{:02}:{:02}".format(mirror_hour, mirror_minute)
