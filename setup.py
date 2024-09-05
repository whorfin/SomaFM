import setuptools

with open("pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="somafm",
    version="2.7.4",
    scripts=['somafm'],
    author="Lord Whorfin",
    author_email="whorfin@gmail.com",
    description="A simple console player for SomaFM streams, with a focus on audio quality; uses mpv as audio backend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/whorfin/SomaFM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.5',
    install_requires=[
          'requests',
          'colorama',
      ],
    extras_require = {
        'Chromecast Support':  ["pychromecast"]
    }
)
