# Generated from seed-fu-2.3.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name seed-fu

Name: rubygem-%{gem_name}
Version: 2.3.5
Release: 1%{?dist}
Summary: Easily manage seed data in your Active Record application
Group: Development/Languages
License: MIT
URL: http://github.com/mbleigh/seed-fu
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Seed Fu is an attempt to once and for all solve the problem of inserting and
maintaining seed data in a database. It uses a variety of techniques gathered
from various places around the web and combines them to create what is
hopefully the most robust seed data system around.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.3.5-1
- Initial package
