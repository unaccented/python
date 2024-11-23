class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False 
        self._muted = False  
        self._volume = self.MIN_VOLUME  
        self._channel = self.MIN_CHANNEL  

    def power(self):
        """Turns the TV on or off."""
        self._status = not self._status

    def mute(self):
        """Mutes or unmutes the TV."""
        if self._status:  
            self._muted = not self._muted

    def channel_up(self):
        """Increases the channel, loops to the minimum channel if it goes past the maximum."""
        if self._status:  
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

    def __str__(self):
        """Returns a string representation of the TV's current state."""
        status = "On" if self._status else "Off"
        muted = "Muted" if self._muted else "Not Muted"
        return f"Status: {status}, Channel: {self._channel}, Volume: {self._volume}, {muted}"
