from setuptools import setup
setup(
    name = "flamegraph",
    version = "0.1",
    packages = ['flamegraph'],

    author = 'Evan Hempel',
    author_email = 'evanhempel@evanhempel.com',
    description = 'Statistical profiler which outputs in format suitable for FlameGraph',
    long_description = open('README.rst').read(),
    license = 'UNLICENSE',
    keywords = 'profiler flamegraph',
    url = 'https://github.com/evanhempel/python-flamegraph',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: Public Domain',
      'Programming Language :: Python',
      'Topic :: Software Development :: Debuggers',
      ]
    )


