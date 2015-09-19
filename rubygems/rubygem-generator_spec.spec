# Generated from generator_spec-0.9.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name generator_spec

Name: rubygem-%{gem_name}
Version: 0.9.3
Release: 1%{?dist}
Summary: Test Rails generators with RSpec
Group: Development/Languages
License: MIT
URL: https://github.com/stevehodgkiss/generator_spec
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Test Rails generators with RSpec.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/generator_spec.gemspec
%{gem_instdir}/spec

%changelog
* Fri Sep 18 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.9.3-1
- Initial package
