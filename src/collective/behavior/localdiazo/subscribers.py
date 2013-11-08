# -*- coding: utf-8 *-*

from plone.subrequest import subrequest


def set_theme(obj, event):
    """
    """
    # When using /_vh_ subpaths it is safer to use this approach
    base = '/'.join(obj.getPhysicalPath())
    diazo_setter = subrequest(  # noqa
        base + '/@@local-diazo-setter'
    )
