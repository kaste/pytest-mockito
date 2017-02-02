import pytest

import os


class TestFixtures:

    @pytest.mark.xfail()
    def testFail(self, when):
        when(os.path).exists('/Bar').thenReturn(True)
        assert not os.path.exists('/Bar')  # sic!

    def testCheckIfCleaned(self):
        assert not os.path.exists('/Foo')

    def testSanityCheck(self, when):
        when(os.path).exists('/Foo').thenReturn(True)
        assert os.path.exists('/Foo')  # sanity check
