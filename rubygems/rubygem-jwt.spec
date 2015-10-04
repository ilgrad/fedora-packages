# Generated from jwt-1.5.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jwt

Name: rubygem-%{gem_name}
Version: 1.5.1
Release: 1%{?dist}
Summary: JSON Web Token implementation in Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/progrium/ruby-jwt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/jwt/ruby-jwt/blob/master/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.2
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(simplecov-json)
BuildRequires: rubygem(codeclimate-test-reporter)
BuildArch: noarch

%description
JSON Web Token implementation in Ruby.


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
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_instdir}/Manifest
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/jwt.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.5.1-1
- Initial package
