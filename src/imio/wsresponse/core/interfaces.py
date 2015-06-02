# encoding: utf-8

from zope.interface import Interface


class IResponse(Interface):
    """Marker interface for response message"""


class IValidation(Interface):
    """Marker interface for response related validations"""
