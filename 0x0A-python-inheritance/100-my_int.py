#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """waaa mwimti == is now !=."""
        return self.real != value

    def __ne__(self, value):
        """9leb cha9leb same as before but reverseds"""
        return self.real == value