# IntXeger

[![Build Status](https://img.shields.io/github/workflow/status/k15z/IntXeger/Build%20Main?style=flat-square)](https://github.com/k15z/IntXeger/actions)
[![Documentation](https://img.shields.io/github/workflow/status/k15z/IntXeger/Documentation?label=docs&style=flat-square)](https://k15z.github.io/IntXeger)
[![Code Coverage](https://img.shields.io/codecov/c/github/k15z/IntXeger?style=flat-square)](https://codecov.io/gh/k15z/IntXeger)
[![PyPI](https://img.shields.io/pypi/pyversions/intxeger?style=flat-square)](https://pypi.org/project/intxeger/)
[![MIT](https://img.shields.io/github/license/k15z/IntXeger?style=flat-square)](https://github.com/k15z/IntXeger/blob/main/LICENSE)

IntXeger (pronounced "integer") is a Python library for generating strings from regular
expressions. Some of its core features include:

* Support for most common regular expression operations.
* Array-like indexing for mapping integers to matching strings.
* Generator interface for sequentially sampling matching strings.
* Sampling-without-replacement for generating a set of unique strings.

Compared to popular alternatives such as [xeger](https://github.com/crdoconnor/xeger) and 
[exrex](https://github.com/asciimoo/exrex), `IntXeger` is an order of magnitude faster at
generating strings and offers unique functionality such as array-like indexing and 
sampling-without-replacement.

## Installation
You can install the latest stable release of IntXeger by running:

```bash
pip install intxeger
```

## Quick Start

Let's start with a simple example where our regex specifies a two-character string
that only contains lowercase letters.

```python
import intxeger
x = intxeger.build("[a-z]{2}")
```

You can check the number of strings that can be generated from this regex using 
the `length` attribute and generate the `i`th matching string using the `get(i)`
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

Here's a more complicated regex which specifies a timestamp.

```python
x = intxeger.build(r"(1[0-2]|0[1-9])(:[0-5]\d){2} (A|P)M")
print(x.sample(N=2))
# ['11:57:12 AM', '01:16:01 AM']
```

You can also print matches on the command line.

```console
$ intxeger --order=desc "[a-c]"
c
b
a
$ python3 -m intxeger -0 'base/[ab]/[12]' | xargs -0 mkdir -p
$ tree base/
base
├── a
│   ├── 1
│   └── 2
└── b
    ├── 1
    └── 2
```

To learn more about the functionality provided by `IntXeger`, check out our 
[documentation](https://k15z.github.io/IntXeger)!

## Benchmark
This table, generated by `benchmark.py`, shows the amount of time in 
milliseconds required to generate `N` examples of each regular expression
using `xeger` and `intxeger`.

| regex                                           |    N |   xeger |   exrex |   intxeger |
|:------------------------------------------------|-----:|--------:|--------:|-----------:|
| [a-zA-Z]+                                       |  100 |    7.36 |    3.17 |       1.09 |
| [0-9]{3}-[0-9]{3}-[0-9]{4}                      |  100 |   11.59 |    6.25 |       0.8  |
| [0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4} | 1000 |  208.62 |   91.3  |      18.28 |
| /json/([0-9]{4})/([a-z]{4})                     | 1000 |  133.36 |  107.01 |      12.18 |

Have a regular expression that isn't represented here? Check out our 
[Contributing Guide](https://k15z.github.io/IntXeger/contributing.html) and
submit a pull request!
