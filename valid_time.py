'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.

'''
def validTime(time):
    time=time.split(':')
    if len(time)!=2 or len(time[0])!=2 or len(time[1])!=2 or not time[0].isdigit() or not time[1].isdigit() or int(time[0])>23 or int(time[1])>59:
        return False
    return True
print(validTime('15:35'))