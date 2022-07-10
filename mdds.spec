%global do_mem_tests 0
%global do_perf_tests 0
%global api 2.0

Summary:	A collection of multi-dimensional data structures and indexing algorithms
Name:		mdds
Version:	2.0.3
Release:	1
Group:		Development/C++
License:	MIT
Url:		http://gitlab.com/mdds/mdds/
Source0:	http://kohei.us/files/mdds/src/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	boost-devel >= 1.73.0
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
%autopatch -p1
# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall -Os/-Wall %{optflags}/' Makefile* configure*
%configure \
	--enable-openmp

%build
%make_build

%install
%make_install

%check
make check

%files devel
%doc AUTHORS CHANGELOG README.md
%{_docdir}/mdds
%{_includedir}/mdds-%{api}
%{_datadir}/pkgconfig/mdds-%{api}.pc
