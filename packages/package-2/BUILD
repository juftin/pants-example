python_sources(
    name="lib",
    sources=[
        "package_2/**/*.py",
        "package_2/*.py",
    ],
)

python_test_utils(name="conftest", sources=["tests/conftest.py"])

python_tests(
    name="tests",
    sources=[
        "tests/**/test_*.py",
        "tests/test_*.py",
    ],
    dependencies=[
        ":lib",
        ":conftest",
    ],
)

python_distribution(
    name="dist",
    dependencies=[
        ":lib",
    ],
    provides=setup_py(
        name="package-2",
        version="0.1.0",
    ),
    generate_setup=True,
)
