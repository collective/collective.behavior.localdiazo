# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '1.0b2.dev0'
long_description = (
    open("README.rst").read() + "\n" +
    open(os.path.join("docs", "CREDITS.rst")).read() + "\n" +
    open(os.path.join("docs", "HISTORY.rst")).read()
)

setup(name='collective.behavior.localdiazo',
      version=version,
      description="Dexterity behavior to enable a local Diazo theme.",
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Office/Business :: News/Diary",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone registry local behavior dexterity diazo',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/collective/collective.behavior.localdiazo',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.behavior'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.behavior.localregistry',
          'Pillow',
          'plone.app.theming',
          'plone.behavior',
          'plone.directives.form',
          'plone.registry',
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'develop': [
              'manuel',
              'setuptools-flakes',
              'Sphinx',
          ],
          'test': [
              'interlude',
              'plone.app.dexterity',
              'plone.app.testing',
              'plone.dexterity',
              'plone.testing',
              'unittest2',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
