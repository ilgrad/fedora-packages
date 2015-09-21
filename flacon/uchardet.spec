%global debug_package %{nil}

Name:          uchardet
Version:       0.0.0
Release:       2%{?dist}
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
Summary:        uchardet development package

%description	libs
This package provides the libraries and binaries that are shared amongst
the various components of uchardet.


%package	libs-devel
Summary:        uchardet development package
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	libs-devel
This package provides the development files for the libraries that are
shared amongst the various components of uchardet.


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

%post -p /sbin/ldconfig

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
* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.0-2
- fix version on 0.0.0
- fix license path
- remove static lib
- fix description
- fix number packages

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.0-1
- Initial package	
