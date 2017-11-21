%global do_mem_tests 0
%global do_perf_tests 0
%define api 1.2

Summary:	A collection of multi-dimensional data structures and indexing algorithms
Name:		mdds
Version:	1.3.1
Release:	1
Group:		Development/C++
License:	MIT
Url:		http://gitlab.com/mdds/mdds/
Source0:	https://gitlab.com/mdds/mdds/repository/%{version}/archive.tar.bz2
Patch0:		mdds-c++17.patch
BuildArch:	noarch

BuildRequires:	boost-devel
%if %{do_mem_tests}
BuildRequires:	valgrind
%endif

%description
A collection of multi-dimensional data structures and indexing algorithms.

It implements the following data structures:
* segment tree
* flat segment tree
* rectangle set
* point quad tree
* mixed type matrix

%package devel
Group:		Development/C++
Summary:	Headers for %{name}
Requires:	boost-devel

%description devel
Headers for %{name}.

%prep
%setup -qn mdds-%{version}-8db40b310ff739f259c52764e4d8c63350ab334d
%apply_patches
# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall -Os/-Wall %{optflags}/' Makefile* configure*

%build
%configure
%make

%install
%makeinstall_std

%check
make check

%files devel
%doc AUTHORS CHANGELOG README.md
%{_docdir}/mdds
%{_includedir}/mdds-%{api}
%{_datadir}/pkgconfig/mdds-%{api}.pc

