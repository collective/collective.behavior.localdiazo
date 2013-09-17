# -*- coding: utf-8 *-*

from plone.subrequest import subrequest


def set_theme(obj, event):
    """
    """
    diazo_setter = subrequest(  # noqa
        '/@@local-diazo-setter', root=obj)
