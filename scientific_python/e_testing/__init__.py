def test_suite():
    from . import doctests, unittests
    import unittest

    suite = unittest.TestSuite()
    suite.addTest(doctests.test_suite())
    suite.addTest(unittests.test_suite())
    return suite
