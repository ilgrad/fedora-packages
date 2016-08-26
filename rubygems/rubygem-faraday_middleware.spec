%global gem_name faraday_middleware

Name: rubygem-%{gem_name}
Version: 0.10.0
Release: 2%{?dist}
Summary: Various middleware for Faraday
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/lostisland/faraday_middleware.git && cd faraday_middleware
# git checkout v0.10.0 && tar czvf faraday_middleware-0.10.0-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(faraday)
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(hashie)
BuildRequires: rubygem(multi_xml)
BuildRequires: rubygem(rash)
BuildRequires: rubygem(simple_oauth)
BuildArch: noarch

%description
Various middleware for Faraday.


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
  tar xzf %{SOURCE1}
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/faraday_middleware.gemspec

%changelog
* Fri Aug 26 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.10.0-2
- small changes in files section

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.10.0-1
- Initial package
