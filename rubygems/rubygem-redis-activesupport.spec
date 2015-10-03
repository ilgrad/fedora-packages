# Generated from redis-activesupport-4.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-activesupport

Name: rubygem-%{gem_name}
Version: 4.1.3
Release: 1%{?dist}
Summary: Redis store for ActiveSupport
Group: Development/Languages
License: MIT
URL: http://redis-store.org/redis-activesupport
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(redis-store)
BuildArch: noarch

%description
Redis store for ActiveSupport.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/redis-activesupport.gemspec
%exclude %{gem_instdir}/test

%changelog
* Sat Oct 03 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.1.3-1
- Initial package
