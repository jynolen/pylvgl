import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = HERE.joinpath("README.md").read_text()

# This call to setup() does all the work
setup(
    name="pylvgl",
    version="1.0",
    description="Convert and Retreive Image for LVGL",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jynolen/pylvgl",
    author="Jean-Yves NOLEN",
    author_email="jynolen+github@gmail.com",
    license="MIT",
    keywords=['image', 'lvgl', "em"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["lvgl", "lvgl.converter", "lvgl.deconverter"],
    include_package_data=True,
    install_requires=["Pillow", "jinja2", "numpy"],
    extras_require={
        'svg': ['cairosvg']
    },
    entry_points={
        "console_scripts": [
            "converter=lvgl.converter.__main__:main",
            "deconverter=lvgl.deconverter.__main__:main",
        ]
    },
)