%global srcname hs-dbus-signature
%global sum Hypothesis strategy that generates arbitrary d-bus signatures
Name:          python-%{srcname}
Version:       0.05
Release:       1%{?dist}
Summary:       %{sum}

License:       MPLv2.0
URL:           https://github.com/stratis-storage/hs-dbus-signature
Source0:       https://github.com/stratis-storage/%{srcname}/archive/v%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-pyparsing
Requires:      python3-hypothesis

%description
A Hypothesis Strategy for Generating Arbitrary DBus Signatures

%package -n python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Hypothesis Strategy for Generating Arbitrary DBus Signatures

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%{python3_sitelib}/*


%changelog
* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.05-1
- Initial package
