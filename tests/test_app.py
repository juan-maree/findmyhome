from findmyhome.app import *
import pytest

def test_configuration_prompt():
  monkeypatch.setattr('builtins.input', lambda _: "y")
  assert confirmation_prompt("Test positive") == True