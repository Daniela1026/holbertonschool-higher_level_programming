#!/usr/bin/python3
"""Unittest for rectangle.py"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8


class TestsBase(unittest.TestCase):
    """pep8 testing"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """Test that PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)
