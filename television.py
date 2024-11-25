class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False  # TV is initially off
        self.__muted = False   # TV is initially not muted
        self.__volume = self.MIN_VOLUME  # Volume set to minimum
        self.__channel = self.MIN_CHANNEL  # Channel set to minimum

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:  # Only mute/unmute if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:  # Only change channels if the TV is on
            self.__channel = self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1

    def channel_down(self):
        if self.__status:  # Only change channels if the TV is on
            self.__channel = self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1

    def volume_up(self):
        if self.__status:  # Only adjust volume if the TV is on
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:  # Only adjust volume if the TV is on
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        status = "On" if self.__status else "Off"
        muted = " (Muted)" if self.__muted else ""
        return f"Power: {status}, Channel: {self.__channel}, Volume: {self.__volume}{muted}"
