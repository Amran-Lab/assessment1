#!/usr/bin/env python3.8	
import pytest
from Code import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True