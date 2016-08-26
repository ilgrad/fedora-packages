%global gem_name rash

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: simple extension to Hashie::Mash for rubyified keys
Group: Development/Languages
License: MIT 
URL: http://github.com/tcocca/rash
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec2)
BuildRequires: rubygem(hashie)
BuildArch: noarch

%description
simple extension to Hashie::Mash for rubyified keys, all keys are converted to
underscore to eliminate horrible camelCasing.


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
  rspec2 -Ilib spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %doc %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/rash.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Fri Aug 26 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.0-1
- Initial package
