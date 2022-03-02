
class AlarmClock:

    def __init__(self):
        self.current_time = "12:34pm"
        self.power_on_or_off = True
        self.alarm_time = "12:00am"

    def change_current_time(self, new_time):
        self.current_time = new_time
        print(self.current_time)

    def turn_on_or_off(self):
        if self.power_on_or_off == True:
            self.power_on_or_off = False
            print("Off")
        elif self.power_on_or_off == False:
            self.power_on_or_off = True
            print("On")

    def set_alarm_time(self, alarm_time):
        self.alarm_time = alarm_time
        print(self.alarm_time)