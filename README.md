# IntXeger

[![Build Status](https://img.shields.io/github/workflow/status/k15z/IntXeger/Build%20Main?style=flat-square)](https://github.com/k15z/IntXeger/actions)
[![Documentation](https://img.shields.io/github/workflow/status/k15z/IntXeger/Documentation?label=docs&style=flat-square)](https://k15z.github.io/IntXeger)
[![Code Coverage](https://img.shields.io/codecov/c/github/k15z/IntXeger?style=flat-square)](https://codecov.io/gh/k15z/IntXeger)
[![PyPI](https://img.shields.io/pypi/pyversions/intxeger?style=flat-square)](https://pypi.org/project/intxeger/)
![MIT](https://img.shields.io/github/license/k15z/IntXeger?style=flat-square)

IntXeger (pronounced "integer") is a Python library for generating strings from regular
expressions. It was inspired by the [xeger](https://github.com/crdoconnor/xeger) library but 
provides additional functionality such as:

* Array-like indexing for mapping integers to strings which match the regex.
* Sampling-without-replacement for generating a set of unique strings which match the regex.

These features make IntXeger more suitable than xeger for applications such as generating 
unique identifiers, enumerating all strings which match the regex, and more!

## Installation
You can install the latest stable release of IntXeger by running:

```bash
pip install intxeger
```

## Quick Start

Let's start with a simple example where our regex specifies a two-character strnig
that only contains lowercase letters.

```python
import intxeger
x = intxeger.build("[a-z]{2}")
```

You can check the number of strings that can be generated with this string using 
the `length()` method and generate the `i`th string which matches using the `get(i)`
method.

```python
assert x.length == 26**2 # there are 676 unique strings which match this regex
assert x.get(15) == 'ap' # the 15th unique string is 'ap'
```

Furthermore, you can generate `N` unique strings which match this regex using the
`sample(N)` method. Note that `N` must be less than or equal to the length.

```python
print(x.sample(N=10))
# ['xt', 'rd', 'jm', 'pj', 'jy', 'sp', 'cm', 'ag', 'cb', 'yt']
```

Here's a more complicated regex which specifies a 16-digit hexadecimal string, 
delimited between every group of 4 digits by a dash.

```python
x = intxeger.build("[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}")
print(x.sample(N=1))
# ['F64C-F593-5E4A-E634']
```

To learn more about the functionality provided by `IntXeger`, check out our 
[documentation](https://k15z.github.io/IntXeger)!
