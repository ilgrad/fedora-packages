# Generated from minitest-around-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name minitest-around

Name: rubygem-%{gem_name}
Version: 0.3.2
Release: 1%{?dist}
Summary: Around block for minitest
Group: Development/Languages
License: MIT
URL: https://github.com/splattael/minitest-around
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Alternative for setup/teardown dance.


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
  sed -i "/require 'bundler/ s/^/#/" test/helper.rb
  ruby -Ilib -e 'Dir.glob "./test/*test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/config
%{gem_instdir}/features
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/examples
%exclude %{gem_instdir}/minitest-around.gemspec
%exclude %{gem_instdir}/test

%changelog
* Tue Sep 29 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.3.2-1
- Initial package
