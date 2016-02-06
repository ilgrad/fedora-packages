Name:          uchardet
Version:       0.0.5
Release:       1%{?dist}
Summary:       An encoding detector library ported from Mozilla

License:       MPLv1.1
URL:           https://github.com/BYVoid/%{name}
Source0:       https://github.com/BYVoid/uchardet/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. Uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package	devel
Summary:        Development files for ${name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains headers and shared libraries
for developing tools for uchardet.

%prep
%autosetup
mkdir build

%build
pushd build
  %cmake .. -DCMAKE_INSTALL_LIBDIR=%{_libdir}
  %make_build
popd

%install
pushd build
  %make_install
popd

# remove static library
rm -f %{buildroot}%{_libdir}/lib%{name}.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
pushd build
  ctest -VV
popd

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Feb 6  2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.5-1
- update version to 0.0.5

* Fri Nov 20 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.3-1
- update version to 0.0.3
- add tests

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
