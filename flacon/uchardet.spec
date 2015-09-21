%global debug_package %{nil}

Name:          uchardet
Version:       0.0.0
Release:       3%{?dist}
Summary:       An encoding detector library ported from Mozilla

License:       MPLv1.1
URL:           https://code.google.com/p/uchardet/
#  git clone git@github.com:BYVoid/uchardet.git uchardet-0.0.0
#  tar -cJvf uchardet-0.0.0.tar.xz uchardet-0.0.0
Source0:       uchardet-0.0.0.tar.xz

BuildRequires: cmake

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.


%package	libs
Summary:        Libraries for %{name}

%description	libs
The %{name}-libs package contains shared libraries.

%package	libs-devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	libs-devel
The %{name}-libs-devel package contains headers and shared libraries
for developing tools for %{name}.


%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

# remove static library
rm -f %{buildroot}%{_libdir}/lib%{name}.a

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS
%{license} COPYING
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files libs
%{_libdir}/lib%{name}.so.*

%files libs-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
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
