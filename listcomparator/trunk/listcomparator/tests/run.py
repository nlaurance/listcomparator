# -*- coding: utf-8 -*-
"""
    listcomparator unit tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Usage::

        python run.py [testfile ...]

"""

import sys

try:
    import nose
except ImportError:
    print ('nose is required to run the test suite')
    sys.exit(1)

try:
    # make sure the current source is first on sys.path
    sys.path.insert(0, '..')
    import listcomparator
except ImportError:
    print ('Cannot find listcomparator to test: %s' % sys.exc_info()[1])
    sys.exit(1)
else:
    print ('listcomparator %s test suite running (Python %s)...' %
           (listcomparator.__version__, sys.version.split()[0]))

nose.main()
