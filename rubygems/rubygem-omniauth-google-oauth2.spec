# Generated from omniauth-google-oauth2-0.2.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name omniauth-google-oauth2

Name: rubygem-%{gem_name}
Version: 0.2.8
Release: 1%{?dist}
Summary: A Google OAuth2 strategy for OmniAuth 1.x
Group: Development/Languages
License: MIT
URL: https://github.com/zquestz/omniauth-google-oauth2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(multi_json)
BuildRequires: rubygem(jwt)
BuildRequires: rubygem(omniauth-oauth2)
BuildRequires: rubygem(addressable)
BuildArch: noarch

%description
A Google OAuth2 strategy for OmniAuth 1.x.


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
  sed -i "/require File/ s/^/#/" spec/spec_helper.rb
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%exclude %{gem_instdir}/omniauth-google-oauth2.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2.8-1
- Initial package
