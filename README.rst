GitHub Download Stats
=====================

|Build Status|
|Coverage|
|Version|
|Support|
|License|

Description
-----------

- Python script to obtain GitHub Release download count and other statistics.
- Can be used as both a standalone script and a Python module.
- Supports both Python 2 and 3 out of the box.

Installation
------------

You can get ``ghstats`` using **one of the following** methods:

- Install from `PyPI`_: ``pip install ghstats``.
- Save `ghstats.py`_ from the repository.
- Download a whole `repository`_.

Usage
-----

::

    ghstats [user] [repo] [tag] [options]
    ghstats [user/repo] [tag] [options]

- *Arguments:*

======== =======================================================================
Argument Description
======== =======================================================================
``user`` Repository owner. If not present, user will be prompted for input.
``repo`` Repository title. If not present, user will be prompted for input.
``tag``  Release tag name. If not present, prints the total number of downloads.
======== =======================================================================

- *Options:*

==================== ==================================================================
Option               Description
==================== ==================================================================
``-d``, ``--detail`` Print detailed statistics for release(s).
``-q``, ``--quiet``  Print only resulting numbers and errors. Overrides ``-d`` option.
``-l``, ``--latest`` Get stats for the latest release. ``Tag`` argument will be ignored.
``-h``, ``--help``   Show help on script usage.
==================== ==================================================================

- *Environment Variables:*

==================== =========================================================
Environment Variable Description
==================== =========================================================
``GITHUB_TOKEN``     `GitHub OAuth token`_. Use to increase API request limit.
==================== =========================================================

Examples
--------

Examples for `atom/atom`_ repository:

.. code:: shell

    ghstats atom atom            # Fetch download count for all releases.
    ghstats atom/atom            # Fetch download count for all releases (alt. syntax).
    ghstats atom atom -q         # Quiet mode (print only numerical result).
    ghstats atom atom -d         # Detailed description for every release.
    ghstats atom atom -l         # Fetch download count for the latest release.
    ghstats atom atom -l -d      # Detailed description for the latest release.
    ghstats atom atom -l -q      # Quiet mode for the latest release.
    ghstats atom atom v1.0.0     # Fetch download count for "v1.0.0" release.
    ghstats atom atom v1.0.0 -d  # Detailed description for "v1.0.0" release.
    ghstats atom atom v1.0.0 -q  # Quiet mode for "v1.0.0" release.
    ghstats                      # Get input for username and repository from user.
    ghstats -h                   # Print help.

License
-------

**MIT License**

You are free to use, modify, distribute (including commercial purposes)
as long as you credit the original author and include the license text.

License text: `MIT License`_

.. _ghstats.py: https://raw.githubusercontent.com/kefir500/ghstats/master/ghstats/ghstats.py
.. _PyPI: https://pypi.python.org/pypi/ghstats
.. _repository: https://github.com/kefir500/ghstats/archive/master.zip
.. _atom/atom: https://github.com/atom/atom
.. _GitHub OAuth token: https://github.com/settings/tokens
.. _issue #1: https://github.com/kefir500/ghstats/issues/1
.. _issue #2: https://github.com/kefir500/ghstats/issues/2
.. _issue #3: https://github.com/kefir500/ghstats/issues/3
.. _issue #4: https://github.com/kefir500/ghstats/issues/4
.. _MIT License: https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/kefir500/ghstats.svg
   :target: https://travis-ci.org/kefir500/ghstats
.. |Coverage| image:: https://coveralls.io/repos/github/kefir500/ghstats/badge.svg?branch=master
   :target: https://coveralls.io/github/kefir500/ghstats?branch=master
.. |Version| image:: https://img.shields.io/pypi/v/ghstats.svg
   :target: https://pypi.python.org/pypi/ghstats
.. |Support| image:: https://img.shields.io/pypi/pyversions/ghstats.svg
   :target: https://pypi.python.org/pypi/ghstats
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE
