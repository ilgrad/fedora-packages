# Generated from simplecov-json-0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name simplecov-json

Name: rubygem-%{gem_name}
Version: 0.2
Release: 1%{?dist}
Summary: JSON formatter for SimpleCov code coverage tool for ruby 1.9+
Group: Development/Languages
License: MIT
URL: https://github.com/vicentllongo/simplecov-json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/vicentllongo/simplecov-json/blob/master/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(mocha)
BuildArch: noarch

%description
JSON formatter for SimpleCov code coverage tool for ruby 1.9+.


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
cp  -p %{SOURCE1} .
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
  sed -i "/require 'bundler/ s/^/#/" test/helper.rb
  ruby -Ilib -e 'Dir.glob "./test/helper.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/test

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2-1
- Initial package
