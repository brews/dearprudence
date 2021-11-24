from setuptools import setup, find_packages


with open("README.md") as readme_file:
    readme = readme_file.read()

history=""
# with open("HISTORY.md") as history_file:
#     history = history_file.read()

setup(
    name="dearprudence",
    version="0.0.1a1",
    description="Internal Python library filled with sugar for swallowing downscalingCMIP6 parameter files.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="Brewster Malevich",
    author_email="bmalevich@rhg.com",
    url="https://github.com/brews/dearprudence",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    keywords="dearprudence",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    extras_require={
        "test": ["pytest"],
        "dev": ["pytest", "pytest-cov", "wheel", "flake8", "pytest", "black", "twine"],
        "doc": ["sphinx", "sphinx_rtd_theme", "numpydoc", "ipython"],
    },
)