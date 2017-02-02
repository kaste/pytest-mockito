Convenience plugin on top of mockito.

.. image:: https://travis-ci.org/kaste/pytest-mockito.svg?branch=master
    :target: https://travis-ci.org/kaste/pytest-mockito

Install
=======

``pip install pytest-mockito``

After that the plugin is enabled by default.


Fixtures
========

The plugin provides fixtures for the main entrypoints of mockito which guarantee that you `unstub()` on teardown. Usage is *very* simple and straightforward::

    def test_foo(when):
        when(os.path).exists('/foo').thenReturn(False)
        assert os.path.exists('/foo')  # sic!
        # will still unstub/unpatch bc pytest will run the teardown

For convenience `verifyStubbedInvocationsAreUsed` is called just before `unstub`. This should warn you when you setup stubs that you actually don't use.

You can also use a marker. `usefixtures <http://doc.pytest.org/en/latest/fixture.html#using-fixtures-from-classes-modules-or-projects>`_ here will ensure an `unstub` at the end of each test, but does not actually inject the fixture::

    import pytest

    @pytest.mark.usefixtures('unstub')
    class TestDog:
        def test(self):
            ...

To mark *all* test cases at the module level::

    pytestmark = pytest.mark.usefixtures('unstub')


All of the following fixtures just export the equivalent mockito function but `unstub()` on teardown. The exception here is `expect` which also calls `verifyNoUnwantedInteractions()`::

    when
    when2
    expect
    patch
    unstub
    spy2



