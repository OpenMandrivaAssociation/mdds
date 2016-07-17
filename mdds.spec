%global do_mem_tests 0
%global do_perf_tests 0
%define api 1.2

Summary:	A collection of multi-dimensional data structures and indexing algorithms
Name:		mdds
Version:	1.2.1
Release:	1
Group:		Development/C++
License:	MIT
Url:		http://gitlab.com/mdds/mdds/
Source0:	http://kohei.us/files/%{name}/src/%{name}-%{version}.tar.bz2
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
%setup -q
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
%{_docdir}/mdds-%{api}
%{_includedir}/mdds-%{api}
%{_datadir}/pkgconfig/mdds-%{api}.pc

