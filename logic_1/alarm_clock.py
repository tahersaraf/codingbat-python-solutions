"""
CodingBat: alarm_clock
https://codingbat.com/prob/p119867

Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
"""

def alarm_clock(day, vacation):
    if vacation:
        if day >= 1 and day <= 5:
            return "10:00"
        else:
            return "off"
    elif day >= 1 and day <= 5:
        return "7:00"
    else:
        return "10:00"
    

# Tests
if __name__ == "__main__":
    print(alarm_clock(1, False) )
    print(alarm_clock(5, False) )
    print(alarm_clock(0, False) )