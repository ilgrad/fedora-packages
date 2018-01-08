%global srcname dbus-signature-pyparsing
Name:          python-%{srcname}
Version:       0.03
Release:       1%{?dist}
Summary:       Parser for a dbus signature

License:       ASL 2.0
URL:           https://github.com/stratis-storage/dbus-signature-pyparsing
Source0:       %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
D-Bus signature parser generated using the pyparsing library.

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pyparsing
BuildRequires: python3-hypothesis
BuildRequires: python3-hs-dbus-signature
BuildRequires: python3-pytest

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
D-Bus signature parser generated using the pyparsing library.

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
%{python3_sitelib}/dbus_signature_pyparsing/
%{python3_sitelib}/dbus_signature_pyparsing-*.egg-info/

%changelog
* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.03-1
- Initial package
