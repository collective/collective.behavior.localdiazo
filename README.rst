******************************
collective.behavior.localdiazo
******************************

.. contents:: Table of Contents

Life, the Universe, and Everything
----------------------------------

Dexterity behavior to enable a local Diazo theme. This package aims to make
easier the creation of microsites on big web sites.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.behavior.localdiazo.png?branch=master
    :target: http://travis-ci.org/collective/collective.behavior.localdiazo

.. image:: https://coveralls.io/repos/collective/collective.behavior.localdiazo/badge.png?branch=master
    :target: https://coveralls.io/r/collective/collective.behavior.localdiazo

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

Don't Panic
-----------

Installation
^^^^^^^^^^^^

To enable this product in a buildout-based installation:

1. Edit your buildout.cfg and add ``collective.behavior.localdiazo`` to the
   list of eggs to install::

    [buildout]
    ...
    eggs =
        collective.behavior.localdiazo

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Usage
^^^^^

In Plone's control panel go to 'Dexterity Content Types', select your content
type, go to the 'Behaviors' tab and enable the 'Local registry' and 'Local
Diazo theme' behaviors.

.. figure:: https://raw.github.com/collective/collective.behavior.localdiazo/master/1.png
    :align: center
    :height: 670px
    :width: 700px

Add a new object; you will see a new field called 'Theme' and select a Diazo
theme from the list.

.. figure:: https://raw.github.com/collective/collective.behavior.localdiazo/master/2.png
    :align: center
    :height: 360px
    :width: 700px

Now when you access your container you will see the Diazo theme applied to it.

.. figure:: https://raw.github.com/collective/collective.behavior.localdiazo/master/3.png
    :align: center
    :height: 500px
    :width: 700px

Troubleshooting
^^^^^^^^^^^^^^^

If you followed all the instructions and the theme is not aplied, make sure
Diazo theming is enabled on 'Theme settings'.

.. figure:: https://raw.github.com/collective/collective.behavior.localdiazo/master/4.png
    :align: center
    :height: 430px
    :width: 700px

Not entirely unlike
-------------------

You may also want to take a look on the following packages:

`collective.lineage`_
    Lineage is a Plone product that allows subfolders of a Plone site to
    appear as autonomous Plone sites to the everyday user.

`collective.spaces`_
    collective.spaces is a simple way of creating mini-sites within the Plone
    CMS, with each mini-site based on a fully-customisable template.

.. _`collective.lineage`: https://pypi.python.org/pypi/collective.lineage
.. _`collective.spaces`: https://pypi.python.org/pypi/collective.spaces
.. _`opening a support ticket`: https://github.com/collective/collective.behavior.localdiazo/issues
