# Generated from omniauth-github-1.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name omniauth-github

Name: rubygem-%{gem_name}
Version: 1.1.2
Release: 1%{?dist}
Summary: Official OmniAuth strategy for GitHub
Group: Development/Languages
License: MIT
URL: https://github.com/intridea/omniauth-github
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/intridea/omniauth-github/blob/master/LICENSE.txt
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec2)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(omniauth-oauth2)
BuildArch: noarch

%description
Official OmniAuth strategy for GitHub.


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
  rspec2 -Ilib spec
popd

%files
%dir %{gem_instdir}
%license LICENSE.txt
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/omniauth-github.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.1.2-1
- Initial package
