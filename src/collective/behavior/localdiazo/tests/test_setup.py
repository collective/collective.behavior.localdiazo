import unittest2 as unittest
import doctest
import pprint
from interlude import interact
from zope.interface import Interface
from plone.testing import (
    layered,
    z2,
)

from collective.behavior.localdiazo.testing import\
    COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING


TESTFILES = [
    ('../behavior.rst', COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING),
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
