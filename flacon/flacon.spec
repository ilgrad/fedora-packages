Name:          flacon
Version:       1.2.0
Release:       1%{?dist}
Summary:       Audio File Encoder

License:       LGPLv2.1
URL:           https://flacon.github.io/
Source0:       https://github.com/flacon/%{name}/archive/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: uchardet-devel
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: qt5-qttools-devel
BuildRequires: desktop-file-utils

Requires: shntool
Requires: flac
Requires: wavpack
Requires: vorbis-tools
Requires: vorbisgain
Requires: libfishsound
Requires: opus-tools


%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} --with-qt
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null ||
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null ||
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man1/%{name}.1.gz


%changelog
* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.2.0-1
- Initial package
