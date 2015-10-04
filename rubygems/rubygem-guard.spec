# Generated from guard-2.13.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name guard

Name: rubygem-%{gem_name}
Version: 2.13.0
Release: 1%{?dist}
Summary: Guard keeps an eye on your file modifications
Group: Development/Languages
License: MIT
URL: http://guardgem.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Guard is a command line tool to easily handle events on file system
modifications.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/guard
%{_bindir}/_guard-core
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_instdir}/images
%{gem_libdir}
%{gem_instdir}/man
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.13.0-1
- Initial package
