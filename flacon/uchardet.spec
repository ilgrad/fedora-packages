%global commit0 84e292d1b9ef38bfa7914de12d345a48f3136c92
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:          uchardet
Version:       0.0.1
Release:       5.git%{shortcommit0}%{?dist}
Summary:       An encoding detector library ported from Mozilla

License:       MPLv1.1
URL:           https://github.com/BYVoid/%{name}
Source0:       %{url}/archive/%{commit0}/.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake

%description
Uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. Uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.


%package	libs
Summary:        Libraries for uchardet

%description	libs
The uchardet-libs package contains shared libraries.

%package	libs-devel
Summary:        Development files for uchardet-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	libs-devel
The uchardet-libs-devel package contains headers and shared libraries
for developing tools for uchardet.


%prep
%autosetup -n %{name}-%{commit0}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
make %{?_smp_mflags} V=1

%install
%make_install

# remove static library
rm -f %{buildroot}%{_libdir}/lib%{name}.a

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%doc AUTHORS
%{license} COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files libs
%{_libdir}/lib%{name}.so.*

%files libs-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Oct  1 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.1-5
- remove macros srcname and sum

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.1-4
- fix enable debug packages
- fix add flag verbose for make
- fix change in build
- fix remove in libs from files
- fix add change for libs in post/postun
- fix version on 0.0.1 from git
- added macros

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.0-3
- fix description and summary for libs and libs-devel

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.0-2
- fix version on 0.0.0
- fix license path
- remove static lib
- fix description
- fix number packages

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.0-1
- Initial package
