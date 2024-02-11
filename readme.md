
# Table of Contents

1.  [About](#orge360d49)
    1.  [Representative Build Systems](#org1a69497)
    2.  [Advanced Benchmarking Demonstrations](#org5f76d35)
2.  [Contributing](#org69422d7)
    1.  [General Contributions and Fixes](#orgdfa26d0)
    2.  [Adding a New Build System](#orgf508e92)
    3.  [Documentation](#org0f638ed)
        1.  [Readme](#org41ba9e7)
3.  [License](#org4093b43)
    1.  [Logo](#org3c861f6)


<a id="orge360d49"></a>

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


<a id="org1a69497"></a>

## Representative Build Systems

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left"><b>Branch</b></td>
<td class="org-left"><b>Configuration</b></td>
<td class="org-left"><b>CI Status</b></td>
</tr>


<tr>
<td class="org-left"><code>main</code></td>
<td class="org-left">Source, not to be run</td>
<td class="org-left">N/A</td>
</tr>


<tr>
<td class="org-left"><code>setup.py-build</code></td>
<td class="org-left">Setuptools with <code>setup.py</code></td>
<td class="org-left"><a href="https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=setup.py-build">Status</a></td>
</tr>


<tr>
<td class="org-left"><code>pyproject-setuptools-build</code></td>
<td class="org-left">Setuptools with <code>pyproject.toml</code></td>
<td class="org-left"><a href="https://github.com/HaoZeke/asv_samples/actions/workflows/build_test.yml/badge.svg?branch=pyproject-setuptools-build">Status</a></td>
</tr>
</tbody>
</table>

Note that in all cases users can always modify the `build_command` variable
within their `asv` configuration file.


<a id="org5f76d35"></a>

## Advanced Benchmarking Demonstrations

-   **Parametrization Techniques:** Showcases how to use decorators for parameterized
    benchmarks, under `decorator-params` branch.
-   **ASV Plugins:** Demonstrates the use of ASV plugins to extend benchmarking
    capabilities, found in the `$PLUGIN_NAME-plugins` branches.
    -   Currently `memray-plugin` showcases the use of `asv_bench_memray`


<a id="org69422d7"></a>

# Contributing

Given the exploding number of build systems and varying configurations, this
repository is necessarily a community effort. We value collaborative efforts
and encourage the use of co-commits for joint contributions.


<a id="orgdfa26d0"></a>

## General Contributions and Fixes

For general enhancements or fixes to existing branches:

-   Fork the repository, apply your changes, and submit a pull request.
-   For collaborative work, please include co-commits. Add `Co-authored-by: name <name@example.com>` at the end of your commit message for each contributor,
    ensuring the email is linked to their GitHub accounts, or use `Co-authored-by: username <username@users.noreply.github.com>`.


<a id="orgf508e92"></a>

## Adding a New Build System

To introduce support for a new build system not currently represented in the
repository:

1.  **Open an Issue**: Start by opening an issue to discuss the new build system,
    providing details and any specific considerations.
2.  **Branch Creation**: Once the issue is approved, a new branch following the
    naming convention `<buildsystem>-build` (e.g., `poetry-build`, `pdm-build`)
    will be created off the default branch.
3.  **Submit a Pull Request**: Fork the repository, implement your changes in the
    corresponding branch, and then submit a pull request targeting the newly
    created branch for the build system.

Remember to follow the collaborative work guidelines laid out in the [previous
section](#orgdfa26d0).


<a id="org0f638ed"></a>

## Documentation


<a id="org41ba9e7"></a>

### Readme

The `readme` can be constructed via:

    ./scripts/org_to_md.sh readme_src.org readme.md


<a id="org4093b43"></a>

# License

MIT.


<a id="org3c861f6"></a>

## Logo

The logo was generated via prompts for ChatGPT4.

