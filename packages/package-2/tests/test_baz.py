from package_2.baz import qux


def test_baz_qux():
    assert qux() == 2
