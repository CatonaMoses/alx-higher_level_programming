#!/usr/bin/python3
"""Defin  object attribute lookup function."""


def lookup(obj):
    """Return list of  object's available attributes."""
    return (dir(obj))
