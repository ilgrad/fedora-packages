%global gem_name email_validator

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 2%{?dist}
Summary: An email validator for Rails 3+
Group: Development/Languages
License: MIT
URL: https://github.com/balexand/email_validator
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(activemodel)
BuildArch: noarch

%description
An email validator for Rails 3+. See homepage for details:
http://github.com/balexand/email_validator.


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
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/Changes.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %doc %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/email_validator.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Fri Aug 26 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.6.0-2
- small changes in files section

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.6.0-1
- Initial package
