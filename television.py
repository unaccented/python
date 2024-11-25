class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initializes the Television instance with default settings.
        """
        self.__status = False  # TV is initially off
        self.__muted = False   # TV is initially not muted
        self.__volume = self.MIN_VOLUME  # Volume set to minimum
        self.__channel = self.MIN_CHANNEL  # Channel set to minimum

    def power(self):
        """
        Toggles the power state of the TV.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Mutes or unmutes the TV.
        """
        if self.__status:  # Only mute/unmute if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increases the TV channel. Loops to the minimum channel if the maximum channel is exceeded.
        """
        if self.__status:  # Only change channels if the TV is on
            self.__channel = self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1

    def channel_down(self):
        """
        Decreases the TV channel. Loops to the maximum channel if the minimum channel is exceeded.
        """
        if self.__status:  # Only change channels if the TV is on
            self.__channel = self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1

    def volume_up(self):
        """
        Increases the TV volume. If the TV is muted, it unmutes and adjusts the volume.
        Volume does not exceed the maximum volume.
        """
        if self.__status:  # Only adjust volume if the TV is on
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases the TV volume. If the TV is muted, it unmutes and adjusts the volume.
        Volume does not go below the minimum volume.
        """
        if self.__status:  # Only adjust volume if the TV is on
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Returns the TV's current state as a formatted string.
        Format: "Power: [On/Off], Channel: [current_channel], Volume: [current_volume]"
        """
        status = "On" if self.__status else "Off"
        muted = " (Muted)" if self.__muted else ""
        return f"Power: {status}, Channel: {self.__channel}, Volume: {self.__volume}{muted}"
