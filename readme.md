![Logo](./branding/logo/asv_samples_logo.png)

# About

This repository repository serves as a comprehensive showcase for
integrating ASV (Air Speed Velocity) with a wide array of Python project
configurations, including various build systems and advanced
benchmarking features like custom parameterizations and ASV plugins.
This initiative aims to benchmark Python code performance across diverse
setups, offering insights into the impacts of different build systems
and ASV's extensible features on performance metrics. The repository is
structured with dedicated branches for each build system and feature
demonstration.

## Usage

Prepare an environment for `asv`:

``` bash
git clone https://github.com/airspeed-velocity/asv_samples/
cd asv_samples
micromamba create -p $(pwd)/.tmp  -c conda-forge python pip "libmambapy<2.0" conda-build
micromamba activate -p $(pwd)/.tmp
pip install asv
```

Checkout any of the branches, prepare them using the `gen_asv_conf.py`
script, and run `asv`:

``` bash
git checkout memray-plugin
python scripts/gen_asv_conf.py asv.conf.base.json
asv run
```

## Representative Build Systems

+CAPTION: Where not specified, `pyproject.toml` is coupled with `hatch`
and `hatchling`

| **Branch**                   | **Configuration**                          | **CI Status**                                                                                                                                                                                                                                       |
|------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `main`                       | Source, not to be run                      | N/A                                                                                                                                                                                                                                                 |
| `setup.py-build`             | Setuptools with `setup.py`                 | [![Status](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=setup.py-build)](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml?query=branch%3Asetup.py-build)                         |
| `pyproject-setuptools-build` | Setuptools with `pyproject.toml`           | [![Status](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=pyproject-setuptools-build)](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml?query=branch%3Apyproject-setuptools-build) |
| `memray-plugin`              | `memray` usage for peak memory             | [![Status](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=memray-plugin)](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml?query=branch%3Amemray-plugin)                           |
| `decorator-params`           | Decorators for simpler parametrization     | [![Status](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=decorator-params)](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml?query=branch%3Adecorator-params)                     |
| `skip-params`                | Various benchmark / parameter skip methods | [![Status](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=skip-params)](https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml?query=branch%3Askip-params)                               |

Note that in all cases users can always modify the `build_command`
variable within their `asv` configuration file.

# Contributing

Given the exploding number of build systems and varying configurations,
this repository is necessarily a community effort. We value
collaborative efforts and encourage the use of co-commits for joint
contributions.

## General Contributions and Fixes

The default branch serves as a common staging area (e.g. common
benchmarks, documentation) for every demonstration branch. Changes which
ought to be propagated to every other branch should be directed towards
`main`.

For general enhancements or fixes to existing branches:

- Fork the repository, apply your changes, and submit a pull request.
- For collaborative work, please include co-commits. Add
  `Co-authored-by: name <name@example.com>` at the end of your commit
  message for each contributor, ensuring the email is linked to their
  GitHub accounts, or use
  `Co-authored-by: username <username@users.noreply.github.com>`.

## Adding a New Build System

To introduce support for a new build system not currently represented in
the repository:

1.  **Open an Issue**: Start by opening an issue to discuss the new
    build system, providing details and any specific considerations.
2.  **Branch Creation**: Once the issue is approved, a new branch
    following the naming convention `<buildsystem>-build` (e.g.,
    `poetry-build`, `pdm-build`) will be created off the default branch.
3.  **Submit a Pull Request**: Fork the repository, implement your
    changes in the corresponding branch, and then submit a pull request
    targeting the newly created branch for the build system.

Remember to follow the collaborative work guidelines laid out in the
<span class="spurious-link"
target="General Contributions and Fixes">*previous section*</span>.

## Documentation

### Readme

The `readme` can be constructed via:

``` bash
./scripts/org_to_md.sh readme_src.org readme.md
```

# License

MIT.

## Logo

The logo was generated via prompts for ChatGPT4.
