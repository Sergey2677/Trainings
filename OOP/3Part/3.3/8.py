class DeltaClock:
    """
    str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
    len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
    print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
    """

    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        if (self.clock1.get_time() - self.clock2.get_time()) > 0:
            min = abs(self.clock1.get_time() - self.clock2.get_time()) // 60
            sec = abs(self.clock1.get_time() - self.clock2.get_time()) % 60
            hours = min // 60
            min = min % 60
            return f"{hours:02}: {min:02}: {sec:02}"
        else:
            return f"00: 00: 00"

    def __len__(self):
        return abs(self.clock1.get_time() - self.clock2.get_time())


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        """Возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds)"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
str_dt = str(dt)
print(str_dt)
print(len(dt))  # 5400
