from plone.subrequest import subrequest


def set_theme(obj, event):
    """
    """
    diazo_setter = subrequest(  # noqa
        obj.absolute_url_path() + '/@@local-diazo-setter')
