# IntXeger

[![Build Status](https://github.com/k15z/intxeger/workflows/Build%20Main/badge.svg)](https://github.com/k15z/IntXeger/actions)
[![Documentation](https://github.com/k15z/intxeger/workflows/Documentation/badge.svg)](https://k15z.github.io/IntXeger)
[![Code Coverage](https://codecov.io/gh/k15z/intxeger/branch/main/graph/badge.svg)](https://codecov.io/gh/k15z/IntXeger)

IntXeger (pronounced "integer") is a Python library for generating strings from regular
expressions. It was inspired by the [xeger](https://github.com/crdoconnor/xeger) library but 
provides additional functionality such as:

* Array-like indexing for mapping integers to strings which match the regex.
* Sampling-without-replacement for generating a set of unique strings which match the regex.

These features make IntXeger more suitable than xeger for applications such as generating 
unique identifiers, enumerating all strings which match the regex, and more!

## Quick Start
```python
import intxeger

x = intxeger.build("[a-z]{4}-[a-z]{4}-[a-z]{4}-[a-z]{4}")
x.sample(10) # generate 10 unique UUIDs
x.length()   # get the number of unique strings
x.get(1001)  # get the 1001th unique string
```

## Installation
**Stable Release:** `pip install intxeger`<br>
**Development Head:** `pip install git+https://github.com/k15z/intxeger.git`

## Documentation
For full package documentation please visit [k15z.github.io/intxeger](https://k15z.github.io/intxeger).

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

### Make Commands
Here are the commands you will need to know for everyday development:

```bash
make install   # install the package in development mode
make test      # run type checks and tests
make view-docs # generate and view docs
make fix-lint  # automatically format and fix lint issues
```
