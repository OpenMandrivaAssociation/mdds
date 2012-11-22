%global do_mem_tests 0
%global do_perf_tests 0

Name:		mdds
Version:	0.5.3
Release:	1
Summary:	A collection of multi-dimensional data structures and indexing algorithms
Group:		Development/C++
License:	MIT
URL:		http://code.google.com/p/multidimalgorithm/
Source0:	http://multidimalgorithm.googlecode.com/files/%{name}_%{version}.tar.bz2

BuildRequires:	boost-devel
%if %{do_mem_tests}
BuildRequires:	valgrind
%endif

BuildArch:	noarch


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
%setup -q -n %{name}_%{version}
# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall.*-std/%{optflags} -std/' Makefile.in

%build
%configure2_5x

%install
mkdir -p %{buildroot}/%{_includedir}
mkdir %{buildroot}/%{_includedir}/mdds
cp -pr include/mdds/* %{buildroot}/%{_includedir}/mdds

%check
%make
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

