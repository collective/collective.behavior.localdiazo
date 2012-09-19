# -*- coding: utf-8 *-*
""" Dexterity behavior to enable a local diazo theme.
"""
from zope.interface import alsoProvides
from zope import schema
from plone.directives import form
from plone.app.theming.utils import getAvailableThemes
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.behavior.localregistry.behavior import ILocalRegistry


def getDiazoThemes(context):
    """Get a list of all Diazo themes.
    """
    themes = getAvailableThemes()
    terms = [SimpleTerm(theme.rules, theme.rules, theme.title)
             for theme in themes]
    terms.insert(0, (SimpleTerm('', '', u'Choose a theme...')))

    return SimpleVocabulary(terms)


class ILocalDiazo(ILocalRegistry):
    """
    """
    theme = schema.Choice(title=u"Theme",
                          vocabulary='collective.behavior.localdiazo.vocabularies.diazo_themes',
                          required=True
                          )

alsoProvides(ILocalDiazo, form.IFormFieldProvider)
