%global package_speccommit 57f3353a57d48d612374f3daee98e236afc273af
%global package_srccommit v1.4.0
%define debug_package %{nil}

Name:           rrd-client-lib
Version:        1.4.0
Release:        2%{?xsrel}%{?dist}
Summary:        C library for writing RRDD plugins
License:        MIT
URL:            https://github.com/xapi-project/rrd-client-lib/
Source0: rrd-client-lib.tar.gz
BuildRequires:  zlib-devel
BuildRequires:  gcc
%{?_cov_buildrequires}

%description
Library for writing RRDD plugins in C. This package contains just the
dynamic library but no header files or static libraries.

%package devel
Summary:        Libraries and header files for rrd development
Requires:       rrd-client-lib = %{version}-%{release}

%description devel
C library for writing RRDD plugins - including header files

%prep
%autosetup -p1
%{?_cov_prepare}

%build
%{?_cov_wrap} make

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install librrd.so  %{buildroot}%{_libdir}
install librrd.h   %{buildroot}%{_includedir}
install librrd.a   %{buildroot}%{_libdir}
%{?_cov_install}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE parson/README.md
%{_libdir}/librrd.so

%files devel
%{_includedir}/librrd.h
%{_libdir}/librrd.a

%{?_cov_results_package}

%changelog
* Fri Dec 17 2021 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- Add --disable-fb flag for Coverity

* Mon Sep 27 2021 Mark Syms <mark.syms@citrix.com> - 1.3.0-2
- Rebuild
* Wed Sep 28 2016 Christian Lindig <christian.lindig@citrix.com> - 1.2.1-1
- New upstream release, fixes meta data format for VM and SR data soruces
* Tue Sep 20 2016 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- New upstream release, fixes compatibility issue with xcp-rrdd
* Thu Sep 01 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- New upstream release, compatible with xcp-rrdd plugin mechanism
* Mon Aug 15 2016 Christian Lindig <christian.lindig@citrix.com> - 1.0.1
- New upstream release that adds more tests
* Wed Aug 10 2016 Christian Lindig <christian.lindig@citrix.com> - 1.0.0
- Initial package
