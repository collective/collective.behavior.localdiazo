from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings
from Products.Five import BrowserView
from plone.app.theming.utils import getAvailableThemes


class LocalRegistrySetter(BrowserView):
    """ Utility view to set theme in the local registry,
        we need to work in a subrequest to get the local registry.
    """

    def __call__(self):
        """
        """
        registry = queryUtility(IRegistry)
        if registry != self.context['local_registry']:
            return
        import ipdb;ipdb.set_trace()
        settings = registry.forInterface(IThemeSettings, False)
        themes = getAvailableThemes()
        for theme in themes:
            if theme.rules == self.context.theme:
                settings.currentTheme = theme.__name__.decode()
                settings.rules = theme.rules
                settings.absolutePrefix = theme.absolutePrefix
                settings.parameterExpressions = theme.parameterExpressions
                settings.doctype = theme.doctype
