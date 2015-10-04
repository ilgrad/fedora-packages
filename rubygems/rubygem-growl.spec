# Generated from growl-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name growl

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 1%{?dist}
Summary: growlnotify bindings
Group: Development/Languages
License: MIT
URL: http://github.com/visionmedia/growl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/tj/growl/blob/master/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.2
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
growlnotify bindings.


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
cp -p %{SOURCE1} .
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
  ruby -Ilib -e 'Dir.glob "./spec/spec_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_instdir}/Manifest
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%exclude %{gem_instdir}/growl.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.3-1
- Initial package
