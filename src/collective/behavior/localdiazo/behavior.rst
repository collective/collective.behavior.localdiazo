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
    >>> fti.behaviors = ('collective.behavior.localdiazo.behavior.ILocalDiazo',)

    >>> childid = portal.invokeFactory("My Dexterity Container", "child")
    >>> child = portal['child']

Check registry creation
-----------------------

::    

    >>> from zope.component import getSiteManager
    >>> csm = getSiteManager(child)
    >>> csm
    <PersistentComponents child>
        
XXX: Here test is cheating: We need to check if ```getUtility(IRegistry)```
returns the childs sitemanager registry. Well, this needs publishers traversal
as far as i know. No idea how to do this in a test. To be done.

What actually happens is::

    >>> from zope.component.hooks import setSite
    >>> setSite(child)
    
An now we can go on as if we are after publishers traversal::

    >>> from zope.component import getUtility
    >>> from plone.registry.interfaces import IRegistry     
    >>> child_registry = getUtility(IRegistry)
    >>> child_registry
    <LocalRegistry at /plone/child/local_registry>
