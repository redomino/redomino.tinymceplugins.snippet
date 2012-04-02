#!/usr/bin/env python
# Authors: Maurizio Lupo <maurizio.lupo@redomino.com> and contributors (see docs/CONTRIBUTORS.txt)
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from setuptools import setup, find_packages
import os

version = '0.0.3dev'

setup(name='redomino.tinymceplugins.snippet',
      version=version,
      description="An not so advanced TinyMCE plugin for handling links to galleries",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Plone",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        ],
      keywords='plone tinymce plugin',
      author='Maurizio Lupo',
      author_email='maurizio.lupo@redomino.com',
      url='https://github.com/redomino/redomino.tinymceplugins.snippet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['redomino', 'redomino.tinymceplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.TinyMCE',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
