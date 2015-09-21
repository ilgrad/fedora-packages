Name:          uchardet
Version:       0.0.1
Release:       1%{?dist}
Summary:       An encoding detector library ported from Mozilla

License:       MPLv1.1
URL:           https://code.google.com/p/uchardet/
#  git clone git@github.com:BYVoid/uchardet.git uchardet-0.0.1
#  tar -cJvf uchardet-0.0.1.tar.xz uchardet-0.0.1
Source0:       uchardet-0.0.1.tar.xz

BuildRequires: cmake

%description
is an encoding detector library, which takes a sequence of bytes
in an unknown character encoding without any additional information,
and attempts to determine the encoding of the text.

%package       devel
Summary:       Development files from uchardet
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
Development libraries and header files from uchardet

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.1-1
- Initial package	
