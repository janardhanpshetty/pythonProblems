#/usr/bin/env python

import nose
from rotation import *

def test_rotateempty():
    assert rotate_all([], 0, 3) == []

def test_rotateone():
    assert rotate_all([1], 1, 2) == [1]

def test_rotatetwo():
    assert rotate_all([1, 2], 2, 1) == [2, 1]

def test_rotatemany():
    assert rotate_all([1, 2, 3, 4], 4, 1) == [2, 3, 4, 1]

def test_rotate2times():
    assert rotate_all([5, 10, 15, -2, -1], 5, 2) == [15, -2, -1, 5, 10]
