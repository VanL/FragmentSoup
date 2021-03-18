
# The MIT License (MIT)
#
# Copyright (c) Van Lindberg 2021
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from setuptools import setup
import fragmentsoup

fragmentsoup_classifiers = ['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Software Development :: Libraries',
                     ]

with open('README.rst', 'r') as f:
    readme = f.read()

with open('CHANGELOG.rst', 'r') as f:
    changes = f.read()

version = fragmentsoup.__version__

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')


if __name__ == '__main__':
    setup(
        name='fragmentsoup',
        description='A wrapper for BeautifulSoup4 that restores the ability to work with HTML fragments',
        long_description='\n\n'.join([readme, changes]),
        license='MIT license',
        url='https://github.com/VanL/FragmentSoup',
        version=version,
        author='VanL',
        author_email='van.lindberg+fragmentsoup@gmail.com',
        maintainer='VanL',
        maintainer_email='van.lindberg+fragmentsoup@gmail.com',
        py_modules=['fragmentsoup'],
        install_requires=requirements,
        keywords=['fragmentsoup', 'beautifulsoup', 'beautifulsoup4'],
        classifiers=fragmentsoup_classifiers,
        zip_safe=True,
    )
