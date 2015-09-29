# Generated from default_value_for-3.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name default_value_for

Name: rubygem-%{gem_name}
Version: 3.0.1
Release: 1%{?dist}
Summary: Provides a way to specify default values for ActiveRecord models
Group: Development/Languages
License: MIT
URL: https://github.com/FooBarWidget/default_value_for
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(railties)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-around)
BuildRequires: rubygem(appraisal)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
The default_value_for plugin allows one to define default values for
ActiveRecord models in a declarative manner.


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
  sed -i "/require 'bundler/ s/^/#/" test.rb
  ruby -Ilib test.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.TXT
%{gem_instdir}/init.rb
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/default_value_for.gemspec
%exclude %{gem_instdir}/test.rb

%changelog
* Tue Sep 29 2015 Ilya Gradina <ilya.gradina@gmail.com> - 3.0.1-1
- Initial package
