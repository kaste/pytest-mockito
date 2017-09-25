import pytest

import os


class TestEnsureUnstubForFailingTests:

    @pytest.mark.xfail()
    def testFail(self, when):
        when(os.path).exists('/Bar').thenReturn(True)
        assert not os.path.exists('/Bar')  # sic!

    def testCheckIfCleaned(self):
        assert not os.path.exists('/Bar')

    def testSanityCheck(self, when):
        when(os.path).exists('/Foo').thenReturn(True)
        assert os.path.exists('/Foo')  # sanity check


class TestEnsureUnstubWhenStubsAreUnused:

    @pytest.mark.xfail()
    def testFails(self, when):
        when(os.path).exists('/Bar').thenReturn(True)

    def testPass(self, when):
        when(os.path).exists('/Bar').thenReturn(True)
        assert os.path.exists('/Bar')

