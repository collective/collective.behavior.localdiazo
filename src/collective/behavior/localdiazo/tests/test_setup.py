# -*- coding: utf-8 *-*

from ..testing import COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING
from interlude import interact
from plone.testing import layered
from plone.testing import z2
from zope.interface import Interface

import doctest
import pprint
import unittest2 as unittest


TESTFILES = [
    ('../behavior.rst', COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING),
    ('../browser.rst', COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING),
]

optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
optionflags |= doctest.REPORT_ONLY_FIRST_FAILURE


class IMyDexterityContainer(Interface):
    """ Dexterity container
    """


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([layered(doctest.DocFileSuite(docfile,
                                                 globs={'interact': interact,
                                                        'pprint':
                                                        pprint.pprint,
                                                        'z2': z2,
                                                        },
                                                 optionflags=optionflags,
                                                 ),
                            layer=layer,
                            ) for docfile, layer in TESTFILES])
    return suite
