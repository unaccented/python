import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv._status == False
    assert tv._muted == False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._status == True
    tv.power()
    assert tv._status == False

def test_mute():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.mute()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == False

def test_channel_up():
    tv = Television()
    tv.power()  # Turn on the TV
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL
