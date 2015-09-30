# Generated from html-pipeline-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name html-pipeline

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: 1%{?dist}
Summary: Helpers for processing content through a chain of filters
Group: Development/Languages
License: MIT
URL: https://github.com/jch/html-pipeline
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(activesupport)
BuildArch: noarch

%description
GitHub HTML processing filters and utilities.


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
  sed -i "/require 'bundler/ s/^/#/" test/test_helper.rb
  ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/script
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/html-pipeline.gemspec
%exclude %{gem_instdir}/test

%changelog
* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.2.0-1
- Initial package
