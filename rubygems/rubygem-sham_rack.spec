# Generated from sham_rack-1.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sham_rack

Name: rubygem-%{gem_name}
Version: 1.3.6
Release: 1%{?dist}
Summary: Net::HTTP-to-Rack plumbing
Group: Development/Languages
License: MIT
URL: http://github.com/mdub/sham_rack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rack)
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
ShamRack plumbs Net::HTTP directly into Rack, for quick and easy HTTP testing.


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
  ruby -Ilib -e 'Dir.glob "./spec/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/CHANGES.markdown
%{gem_instdir}/benchmark
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Sep 18 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.3.6-1
- Initial package
