#!/usr/bin/env python

import nose
from median_2array import *

def test_emptymedian():
    assert main([],[]) == 0

def test_onemedian():
    assert main([1], []) == 1.0

def test_singlemedian():
    assert main([1], [2]) == 1.5

def test_twomedians():
    assert main([1, 2, 3],[3, 4, 5]) == 3.0
