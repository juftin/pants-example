resources(
    name="pyrex-sources",
    sources=["package_1/*.pyx"],
)

python_sources(
    name="lib",
    sources=[
        "package_1/**/*.py",
        "package_1/*.py",
    ],
    dependencies=[
        ":pyrex-sources",
    ],
)

resources(
    name="test-resources",
    sources=[
        "tests/**",
        "!tests/**/test_*.py",
        "!tests/test_*.py",
        "!tests/conftest.py",
    ],
)

python_tests(
    name="tests",
    sources=[
        "tests/**/test_*.py",
        "tests/test_*.py",
    ],
    dependencies=[
        ":dist",
        ":test-resources",
    ],
)

resources(
    name="lib-install-files",
    sources=["pyproject.toml", "setup.py", "README.md", "MANIFEST.in"],
)


python_distribution(
    name="dist",
    dependencies=[
        ":lib",
        ":lib-install-files",
    ],
    provides=setup_py(
        name="package-1",
        version="0.1.0",
    ),
    generate_setup=False,
)
