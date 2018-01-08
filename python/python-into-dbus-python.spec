%global srcname into-dbus-python
Name:          python-%{srcname}
Version:       0.06
Release:       1%{?dist}
Summary:       Transformer to dbus-python types

License:       ASL 2.0
URL:           https://github.com/stratis-storage/into-dbus-python
Source0:       %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
Generates functions that transform values in Python core types to values
in dbus-python types.

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-dbus-signature-pyparsing
BuildRequires: python3-pytest
Requires: python3-dbus
Requires: python3-dbus-signature-pyparsing


%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Generates functions that transform values in Python core types to values
in dbus-python types.

%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/into_dbus_python/
%{python3_sitelib}/into_dbus_python-*.egg-info/

%changelog
* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.06-1
- Initial package
