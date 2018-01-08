%global srcname hs-dbus-signature
Name:          python-%{srcname}
Version:       0.05
Release:       2%{?dist}
Summary:       Hypothesis strategy that generates arbitrary d-bus signatures

License:       MPLv2.0
URL:           https://github.com/stratis-storage/hs-dbus-signature
Source0:       %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
A Hypothesis Strategy for Generating Arbitrary DBus Signatures.

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Hypothesis Strategy for Generating Arbitrary DBus Signatures.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/hs_dbus_signature/
%{python3_sitelib}/hs_dbus_signature-*.egg-info/


%changelog
* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.05-2
- minor changes

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.05-1
- Initial package
