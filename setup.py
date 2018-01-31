from setuptools import setup, Extension

setup(
    name="dtw",
    ext_modules=[Extension('dtw', sources=['dtw.c'])],
    version="0.1.14",
)
