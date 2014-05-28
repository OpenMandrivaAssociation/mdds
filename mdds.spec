%global do_mem_tests 0
%global do_perf_tests 0

Summary:	A collection of multi-dimensional data structures and indexing algorithms
Name:		mdds
Version:	0.10.3
Release:	1
Group:		Development/C++
License:	MIT
Url:		http://code.google.com/p/multidimalgorithm/
Source0:	http://kohei.us/files/%{name}/src/%{name}_%{version}.tar.bz2
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
%setup -qn %{name}_%{version}
# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall -Os/-Wall %{optflags}/' Makefile* configure*

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_datadir}/pkgconfig
mkdir %{buildroot}/%{_includedir}/mdds
cp -pr include/mdds/* %{buildroot}/%{_includedir}/mdds
cp misc/mdds.pc %{buildroot}/%{_datadir}/pkgconfig

%check
for t in fst pqt recset st; do
    make test.$t
done
%if %{do_perf_tests}
    for t in recset st; do
        make test.$t.perf
    done
    make test.stl
%endif
%if %{do_mem_tests}
    for t in fst pqt recset st; do
        make test.$t.mem
    done
%endif

%files devel
%doc AUTHORS NEWS README
%{_includedir}/mdds
%{_datadir}/pkgconfig/mdds.pc

