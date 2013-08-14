# -*- coding: utf-8 *-*
""" Dexterity behavior to enable a local diazo theme.
"""
from zope.interface import alsoProvides
from zope import schema
from plone.directives import form
from plone.app.theming.utils import getAvailableThemes
from plone.app.theming.interfaces import TEMPLATE_THEME
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.behavior.localregistry.behavior import ILocalRegistry
from collective.behavior.localdiazo import _


def getDiazoThemes(context):
    """Get a list of all Diazo themes.
    """
    themes = getAvailableThemes()
    terms = [SimpleTerm(theme.rules, theme.rules, theme.title)
             for theme in themes
             if theme.__name__ != TEMPLATE_THEME]
    terms.insert(0, (SimpleTerm('', '', _(u'No local theme'))))

    return SimpleVocabulary(terms)


class ILocalDiazo(ILocalRegistry):
    """
    """
    theme = schema.Choice(
        title=_(u"Theme"),
        description=_(u""),
        vocabulary='collective.behavior.localdiazo.vocabularies.diazo_themes',
        required=True
    )

alsoProvides(ILocalDiazo, form.IFormFieldProvider)
