Testing the Layered Proxy Registry
==================================

Basic Setup
-----------

Create ```child``` folder for tests::

    >>> portal = layer.get('app').plone
    >>> z2.login(portal['acl_users'], 'manager')

	>>> from plone.dexterity.fti import DexterityFTI
    >>> fti = DexterityFTI('My Dexterity Container')
    >>> portal.portal_types._setObject('My Dexterity Container', fti)
    'My Dexterity Container'
    >>> fti.klass = 'plone.dexterity.content.Container'
    >>> fti.schema = 'collective.behavior.localdiazo.tests.test_setup.IMyDexterityContainer'
    >>> fti.behaviors = ('collective.behavior.localregistry.behavior.ILocalRegistry',
    ...                  'collective.behavior.localdiazo.behavior.ILocalDiazo',)

    >>> childid = portal.invokeFactory("My Dexterity Container", "child")
    >>> child = portal['child']

