# from django.test import TestCase


# class TestClass(TestCase):
#     def test_hello_world(self):
#         self.assertEqual("Hello", "Hello")

import pytest


def test_hello_world1(test_fixture1):
    print("function_fixture1")
    assert test_fixture1 == 1


def test_hello_world2(test_fixture1):
    print("function_fixture2")
    assert test_fixture1 == 1
