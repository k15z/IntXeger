# IntXeger

[![Build Status](https://github.com/k15z/intxeger/workflows/Build%20Master/badge.svg)](https://github.com/k15z/intxeger/actions)
[![Documentation](https://github.com/k15z/intxeger/workflows/Documentation/badge.svg)](https://k15z.github.io/intxeger)
[![Code Coverage](https://codecov.io/gh/k15z/intxeger/branch/master/graph/badge.svg)](https://codecov.io/gh/k15z/intxeger)

Generate unique strings from regular expressions.

---

## Features
* ... coming soon ...

## Quick Start
```python
import intxeger
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

### Additional Steps
To take advantage of the other features - continuous integration, documentation, etc. - you will need to perform some additional steps:

  1. Add your repository to GitHub:
  2. Register your project with Codecov:
      * Make an account on [codecov.io](https://codecov.io) and click `Add new repository`
      * Copy the token provided, go to your GitHub repository's settings and under the
    `Secrets` tab, add a secret called `CODECOV_TOKEN` with the token you just copied.
  3. Generate an access token for documentation generation:
      * Go to your [GitHub account's Personal Access Tokens page](https://github.com/settings/tokens)
      * Click: `Generate new token`
      * Give the token access to: `repo:status`, `repo_deployment`, and `public_repo`.
      * Go to your GitHub repository's settings and under the `Secrets` tab, add a secret
    called `ACCESS_TOKEN` with the personal access token you just created.
  4. Register your project with PyPI:
      * Go to your GitHub repository's settings and under the `Secrets` tab, add a secret
        called `PYPI_TOKEN` with your password for your PyPI account.
      * Next time you push to the branch: `stable`, GitHub actions will build and deploy
        your Python package to PyPI.
