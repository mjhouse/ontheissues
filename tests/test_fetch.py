# content of test_sysexit.py
import pytest
from ontheissues.search import Search

def test_search():
    source = Search("senate","Jeff Flake")