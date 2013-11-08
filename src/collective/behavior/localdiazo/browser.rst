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

An now we can go on as if we are after publishers traversal.
Before we do anything, we must register the ```IThemeSettings``` interface
in the registry::

    >>> from zope.component import getUtility
    >>> from plone.registry.interfaces import IRegistry
    >>> child_registry = getUtility(IRegistry)
    >>> from plone.app.theming.interfaces import IThemeSettings
    >>> child_registry.registerInterface(IThemeSettings)
    >>> settings = child_registry.forInterface(IThemeSettings, False)
    >>> settings
    <RecordsProxy for plone.app.theming.interfaces.IThemeSettings>

Once we set the theme for ```child``` folder, we check that
theme settings has been correctly applied::

    >>> child.theme = u'/++theme++example/rules.xml'
    >>> child.restrictedTraverse('@@local-diazo-setter')()
    >>> settings.currentTheme
    u'example'
    >>> settings.rules
    u'/++theme++example/rules.xml'
    >>> settings.absolutePrefix
    u'/++theme++example'
    >>> settings.parameterExpressions
    {}
    >>> settings.doctype
    '<!DOCTYPE html>'

Now we remove the theme, and check again that everything is
back to default (i.e., no theme is applied)::

    >>> child.theme = u''
    >>> child.restrictedTraverse('@@local-diazo-setter')()
    >>> settings.currentTheme
    >>> settings.rules
    >>> settings.absolutePrefix
    >>> settings.parameterExpressions
    {}
    >>> settings.doctype
    ''

Check virtual hosting
---------------------

We'll create a special base request indicating virtual hosting and test
to ensure that a save happens correctly::

   >>> old_script = child.REQUEST._script

Hack that request!::

   >>> child.REQUEST._script = ['dummy_base']
   >>> child.absolute_url_path()
   '/dummy_base/plone/child'
   >>> from plone.subrequest import subrequest
   >>> response = subrequest(child.absolute_url_path()+'/@@local-diazo-setter')
   >>> response.getStatus()
   404
   >>> base = '/'.join(child.getPhysicalPath())
   >>> response = subrequest(base + '/@@local-diazo-setter')
   >>> response.getStatus()
   200

Return the request to normal::

   >>> child.REQUEST._script = old_script
