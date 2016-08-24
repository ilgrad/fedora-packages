%global gem_name enumerize

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Summary: Enumerated attributes with I18n and ActiveRecord/Mongoid/MongoMapper support
Group: Development/Languages
License: MIT
URL: https://github.com/brainspec/enumerize
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Enumerated attributes with I18n and ActiveRecord/Mongoid/MongoMapper support.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/Gemfile*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/enumerize.gemspec
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/spec

%changelog
* Wed Aug 24 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.0-1
- update to 2.0.0

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.0-1
- Initial package
