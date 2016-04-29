Name:          flacon
Version:       2.0.1
Release:       2%{?dist}
Summary:       Audio File Encoder

License:       LGPLv2+
URL:           https://flacon.github.io/
Source0:       https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: uchardet-devel

Requires: flac
Requires: libfishsound
Requires: opus-tools
Requires: vorbisgain
Requires: vorbis-tools
Requires: shntool
Requires: wavpack


%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. 
To do this, it uses information from the appropriate CUE file. 
Besides, Flacon makes it possible to conveniently revise or specify 
tags both for all tracks at once or for each tag separately.


%prep
%autosetup


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake  \
    -DBUILD_TESTS=Yes \
    -DUSE_QT5=Yes \
    ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-qt


%post
update-desktop-database &> /dev/null ||
touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:


%postun
update-desktop-database &> /dev/null ||
if [ $1 -eq 0 ] ; then 
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
pushd %{_target_platform}
    cd tests && ./flacon_test || :
popd


%files 
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man1/%{name}.1.*


%changelog
* Sat Apr 30 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-2
- changes in the file, thx Jiri Eischmann 1264715#c3

* Wed Apr 27 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-1
- update to 2.0.1 
- few small changes

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.2.0-1
- Initial package
