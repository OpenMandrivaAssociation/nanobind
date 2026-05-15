%undefine _debugsource_packages

Name:		nanobind
Version:	2.12.0
Release:	2
Summary:	Tiny and efficient C++/Python bindings
License:	BSD-3-Clause
Group:		Development/Tools
URL:		https://github.com/wjakob/nanobind
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(tsl-robin-map)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build-core)
# Also needs this for runtime, packages requiring nanobind also need tsl-robin-map package.
Requires:	cmake(tsl-robin-map)

%description
nanobind is a small binding library that exposes C++ types in Python and vice
versa. It is reminiscent of Boost.Python and pybind11 and uses near-identical
syntax.
In contrast to these existing tools, nanobind is more efficient: bindings
compile in a shorter amount of time, produce smaller binaries, and have
better runtime performance.

More concretely, benchmarks show up to ~4× faster compile time, ~5× smaller
binaries, and ~10× lower runtime overheads compared to pybind11. nanobind also
outperforms Cython in important metrics (3-12× binary size reduction, 1.6-4×
compilation time reduction, similar runtime performance).

%build
pip wheel --wheel-dir ../RPMBUILD_wheels --no-deps --no-build-isolation --verbose . \
	-C"cmake.define.NB_USE_SUBMODULE_DEPS:BOOL=OFF" \
	-C"cmake.build-type=RelWithDebInfo"

%files
%{python_sitelib}/nanobind
%{python_sitelib}/nanobind-%{version}.dist-info
