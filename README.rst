******************************
collective.behavior.localdiazo
******************************

.. contents:: Table of Contents

Life, the Universe, and Everything
----------------------------------

Dexterity behavior to enable a local Diazo theme.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.behavior.localdiazo.png?branch=master
    :target: http://travis-ci.org/collective/collective.behavior.localdiazo

.. image:: https://coveralls.io/repos/collective/collective.behavior.localdiazo/badge.png
    :target: https://coveralls.io/r/collective/collective.behavior.localdiazo?branch=master

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

2. If you are using Plone 4.1 you may need to extend a Dexterity known good
   set (KGS) to make sure that you get the right versions of the packages that
   make up Dexterity::

    [buildout]
    ...
    extends =
        http://good-py.appspot.com/release/dexterity/1.2.1

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Use
^^^

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

.. _`opening a support ticket`: https://github.com/collective/collective.behavior.localdiazo/issues
