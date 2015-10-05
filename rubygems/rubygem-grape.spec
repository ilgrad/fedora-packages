# Generated from grape-0.13.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name grape

Name: rubygem-%{gem_name}
Version: 0.13.0
Release: 1%{?dist}
Summary: A simple Ruby framework for building REST-like APIs
Group: Development/Languages
License: MIT
URL: https://github.com/ruby-grape/grape
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rack-mount)
BuildArch: noarch

%description
A Ruby framework for rapid API development with great conventions.


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
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Appraisals
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE
%{gem_instdir}/RELEASING.md
%{gem_instdir}/UPGRADING.md
%{gem_instdir}/gemfiles
%{gem_instdir}/grape.png
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/grape.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.13.0-1
- Initial package
