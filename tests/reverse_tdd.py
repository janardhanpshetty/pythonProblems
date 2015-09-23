#!/usr/bin/env python

import nose
from reverse import *

def test_empty():
    assert rev([]) == []

def test_oneelem():
    assert rev([1]) == [1]

def test_twoelem():
    assert rev([2, 1]) == [1, 2]

def test_manyelem():
    assert rev([1, 2, 3]) == [3, 2, 1]
