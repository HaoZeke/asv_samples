
# Table of Contents

1.  [About](#orgc45fe12)
    1.  [Representative Build Systems](#orgc27e1ca)
    2.  [Advanced Benchmarking Demonstrations](#org4580441)
2.  [Contributing](#org0e3af78)
    1.  [General Contributions and Fixes](#orga841ba1)
    2.  [Adding a New Build System](#org6f5b5a2)
    3.  [Documentation](#org91d798e)
        1.  [Readme](#orgfd15688)
3.  [License](#org58819ed)
    1.  [Logo](#orgb9abe78)


<a id="orgc45fe12"></a>

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


<a id="orgc27e1ca"></a>

## Representative Build Systems

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left"><b>Branch</b></td>
<td class="org-left"><b>Configuration</b></td>
</tr>


<tr>
<td class="org-left"><code>main</code></td>
<td class="org-left">Source, not to be run</td>
</tr>


<tr>
<td class="org-left"><code>setup.py-build</code></td>
<td class="org-left">Setuptools with <code>setup.py</code></td>
</tr>


<tr>
<td class="org-left"><code>pyproject-setuptools-build</code></td>
<td class="org-left">Setuptools with <code>pyproject.toml</code></td>
</tr>
</tbody>
</table>

Note that in all cases users can always modify the `build_command` variable
within their `asv` configuration file.


<a id="org4580441"></a>

## Advanced Benchmarking Demonstrations

-   **Parametrization Techniques:** Showcases how to use decorators for parameterized
    benchmarks, under `decorator-params` branch.
-   **ASV Plugins:** Demonstrates the use of ASV plugins to extend benchmarking
    capabilities, found in the `$PLUGIN_NAME-plugins` branches.
    -   Currently `memray-plugin` showcases the use of `asv_bench_memray`


<a id="org0e3af78"></a>

# Contributing

Given the exploding number of build systems and varying configurations, this
repository is necessarily a community effort. We value collaborative efforts
and encourage the use of co-commits for joint contributions.


<a id="orga841ba1"></a>

## General Contributions and Fixes

For general enhancements or fixes to existing branches:

-   Fork the repository, apply your changes, and submit a pull request.
-   For collaborative work, please include co-commits. Add `Co-authored-by: name <name@example.com>` at the end of your commit message for each contributor,
    ensuring the email is linked to their GitHub accounts, or use `Co-authored-by: username <username@users.noreply.github.com>`.


<a id="org6f5b5a2"></a>

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
section](#orga841ba1).


<a id="org91d798e"></a>

## Documentation


<a id="orgfd15688"></a>

### Readme

The `readme` can be constructed via:

    ./scripts/org_to_md.sh readme_src.org readme.md


<a id="org58819ed"></a>

# License

MIT.


<a id="orgb9abe78"></a>

## Logo

The logo was generated via prompts for ChatGPT4.

