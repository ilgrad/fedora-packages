# Generated from rack-attack-4.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack-attack

Name: rubygem-%{gem_name}
Version: 4.3.0
Release: 1%{?dist}
Summary: Block & throttle abusive requests
Group: Development/Languages
License: MIT
URL: http://github.com/kickstarter/rack-attack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(activesupport)
BuildArch: noarch

%description
A rack middleware for throttling and blocking abusive requests.


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
  sed -i "/require \"bundler/ s/^/#/" spec/spec_helper.rb
  ruby -Ilib -e 'Dir.glob "./spec/spec_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%changelog
* Sat Oct 03 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.3.0-1
- Initial package
