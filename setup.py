from setuptools import setup, find_packages


readme = open('README.md').read()

setup(name="PythonPackagingDependency",
      version='0.0.1',
      packages=find_packages(),
      description="Python Packaging Demo - Dependency Package",
      long_description=readme,
      author="David Antliff",
      author_email="user@example.com",
      url="https://github.com/DavidAntliff/PythonPackagingDependency",
      install_requires=[],
      dependency_links=[],
      scripts=[],
      entry_points={},
      )
