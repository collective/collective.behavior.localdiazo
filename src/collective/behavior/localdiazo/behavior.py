# -*- coding: utf-8 *-*
""" Dexterity behavior to enable a local diazo theme. """
from collective.behavior.localdiazo import _
from collective.behavior.localregistry.behavior import ILocalRegistry
from plone.app.theming.interfaces import TEMPLATE_THEME
from plone.app.theming.utils import getAvailableThemes
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import provider
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def getDiazoThemes(context):
    """Get a list of all Diazo themes.
    """
    themes = getAvailableThemes()
    terms = [SimpleTerm(theme.rules, theme.rules, theme.title)
             for theme in themes
             if theme.__name__ != TEMPLATE_THEME]
    terms.insert(0, (SimpleTerm('', '', _(u'No local theme'))))

    return SimpleVocabulary(terms)


@provider(IFormFieldProvider)
class ILocalDiazo(ILocalRegistry):
    """Diazo theme selection."""

    theme = schema.Choice(
        title=_(u'Theme'),
        description=_(u'Select a theme to enable a different look and feel.'),
        vocabulary='collective.behavior.localdiazo.vocabularies.diazo_themes',
        required=True
    )
