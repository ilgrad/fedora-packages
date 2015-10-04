# Generated from guard-bundler-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name guard-bundler

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: Guard gem for Bundler
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/guard-bundler
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Guard::Bundler automatically install/update your gem bundle when needed.


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
%doc %{gem_instdir}/README.md

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.0-1
- Initial package
