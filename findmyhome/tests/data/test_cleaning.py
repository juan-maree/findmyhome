
from findmyhome.data.cleaning import std_method

import pytest

def test_std_method():
  data = [44, 50, 38, 96, 42, 47, 40, 39, 46, 50]
  result = std_method(data)
  assert result == [0.8301746953743958, 97.56982530462561]
