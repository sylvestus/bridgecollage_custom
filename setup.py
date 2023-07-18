from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bridgecollage_custom/__init__.py
from bridgecollage_custom import __version__ as version

setup(
	name="bridgecollage_custom",
	version=version,
	description="bridge collage custom app",
	author="silvano",
	author_email="silvanussigei1996@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
