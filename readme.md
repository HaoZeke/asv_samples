
# Table of Contents

1.  [About](#org187e7ac)
    1.  [Representative Build Systems](#org5db63c9)
    2.  [Advanced Benchmarking Demonstrations](#org75b7943)
2.  [Contributing](#org5e65f4f)
    1.  [General Contributions and Fixes](#org4afa6a7)
    2.  [Adding a New Build System](#orgcbae17a)
    3.  [Documentation](#orgfef8845)
        1.  [Readme](#org7e12a06)
3.  [License](#org462f9f6)
    1.  [Logo](#org3aa817c)


<a id="org187e7ac"></a>

# About

[ASV Samples Logo](./branding/logo/asv_samples_logo.png)

This repository repository serves as a comprehensive showcase for integrating
ASV (Air Speed Velocity) with a wide array of Python project configurations,
including various build systems and advanced benchmarking features like custom
parameterizations and ASV plugins. This initiative aims to benchmark Python
code performance across diverse setups, offering insights into the impacts of
different build systems and ASV's extensible features on performance metrics.
The repository is structured with dedicated branches for each build system and
feature demonstration.


<a id="org5db63c9"></a>

## Representative Build Systems

-   **Setuptools:** Still a reasonable default.
-   **Poetry:** Uses `poetry-core` as the build system.
-   **PDM:** With the `pdm-backend` build system.
-   **Hatch:** With `hatchling`.

Note that in all cases users can always modify the `build_command` variable
within their `asv` configuration file.


<a id="org75b7943"></a>

## Advanced Benchmarking Demonstrations

-   **Parametrization Techniques:** Showcases how to use decorators for parameterized
    benchmarks, under `decorator-params` branch.
-   **ASV Plugins:** Demonstrates the use of ASV plugins to extend benchmarking
    capabilities, found in the `$PLUGIN_NAME-plugins` branches.
    -   Currently `memray-plugin` showcases the use of `asv_bench_memray`


<a id="org5e65f4f"></a>

# Contributing

Given the exploding number of build systems and varying configurations, this
repository is necessarily a community effort. We value collaborative efforts
and encourage the use of co-commits for joint contributions.


<a id="org4afa6a7"></a>

## General Contributions and Fixes

For general enhancements or fixes to existing branches:

-   Fork the repository, apply your changes, and submit a pull request.
-   For collaborative work, please include co-commits. Add `Co-authored-by: name <name@example.com>` at the end of your commit message for each contributor,
    ensuring the email is linked to their GitHub accounts, or use `Co-authored-by: username <username@users.noreply.github.com>`.


<a id="orgcbae17a"></a>

## Adding a New Build System

To introduce support for a new build system not currently represented in the
repository:

1.  ****Open an Issue****: Start by opening an issue to discuss the new build system,
    providing details and any specific considerations.
2.  ****Branch Creation****: Once the issue is approved, a new branch following the
    naming convention `<buildsystem>-build` (e.g., `poetry-build`, `pdm-build`)
    will be created off the default branch.
3.  ****Submit a Pull Request****: Fork the repository, implement your changes in the
    corresponding branch, and then submit a pull request targeting the newly
    created branch for the build system.

Remember to follow the collaborative work guidelines laid out in the [previous
section](#org4afa6a7).


<a id="orgfef8845"></a>

## Documentation


<a id="org7e12a06"></a>

### Readme

The `readme` can be constructed via:

    ./scripts/org_to_md.sh readme_src.org readme.md


<a id="org462f9f6"></a>

# License

MIT.


<a id="org3aa817c"></a>

## Logo

The logo was generated via prompts for ChatGPT4.

