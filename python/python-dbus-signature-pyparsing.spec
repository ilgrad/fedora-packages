%global srcname dbus-signature-pyparsing
%global sum A parser for a dbus signature
Name:          python-%{srcname}
Version:       0.03
Release:       1%{?dist}
Summary:       %{sum}

License:       ASL 2.0
URL:           https://github.com/stratis-storage/dbus-signature-pyparsing
Source0:       https://github.com/stratis-storage/%{srcname}/archive/v%{version}.tar.gz

BuildArch: noarch

BuildRequires: python2-devel python3-devel
BuildRequires: python2-pyparsing python3-pyparsing
Requires:      python2-hypothesis python3-hypothesis
Requires:      python2-hs_dbus_signature python3-hs_dbus_signature

%description
A D-Bus signature parser generated using the pyparsing library


%package -n python2-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Generates functions that transform values in Python core types to values
 in dbus-python types

%package -n python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Generates functions that transform values in Python core types to values
 in dbus-python types

%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files  -n python2-%{srcname}
%{python2_sitelib}/*

%files -n python3-%{srcname}
%{python3_sitelib}/*

%changelog
* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.03-1
- Initial package
