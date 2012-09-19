from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig


class CollectiveBehaviorLocalDiazo(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import plone.app.dexterity
        xmlconfig.file('configure.zcml',
                       plone.app.dexterity,
                       context=configurationContext)
        import collective.behavior.localregistry
        xmlconfig.file('configure.zcml',
                       collective.behavior.localregistry,
                       context=configurationContext)
        import collective.behavior.localdiazo
        xmlconfig.file('configure.zcml',
                       collective.behavior.localdiazo,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        self['portal'] = portal
        roles = ('Member', 'Manager')
        portal.portal_membership.addMember('manager', 'secret', roles, [])
        roles = ('Member', 'Contributor')
        portal.portal_membership.addMember('contributor', 'secret', roles, [])

COLLECTIVE_BEHAVIOR_LOCALDIAZO_FIXTURE = CollectiveBehaviorLocalDiazo()
COLLECTIVE_BEHAVIOR_LOCALDIAZO_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_BEHAVIOR_LOCALDIAZO_FIXTURE, ),
                       name="CollectiveBehaviorLocalDiazo:Integration")
