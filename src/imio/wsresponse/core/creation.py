# -*- coding: utf-8 -*-

from plone import api
from zope.component import getAdapters

from imio.wsresponse.core.interfaces import IValidation


class ObjectCreation(object):

    def __init__(self, wsrequest, **kw):
        self.wsrequest = wsrequest
        for k, v in kw.items():
            setattr(self, k, v)

    @property
    def parameters(self):
        return self.wsrequest.parameters

    @property
    def data(self):
        return self.parameters.get('data')

    @property
    def optional(self):
        return self.parameters.get('optional', {})

    @property
    def obj_kw(self):
        """Return the keyword arguments for the newly created object"""
        params = self.data
        params.update(self.optional)
        return params

    def validate(self):
        """Find and execute the related validations"""
        for name, adapter in getAdapters((self, ), IValidation):
            adapter.validate()

    def create(self):
        """Create the object"""
        self.validate()
        self.obj = api.content.create(type=self.portal_type,
                                      container=self.container,
                                      **self.obj_kw)
        return self.obj.UID(), self.obj.absolute_url()
