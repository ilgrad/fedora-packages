%global gem_name guard-rspec

Name: rubygem-%{gem_name}
Version: 4.7.3
Release: 1%{?dist}
Summary: Guard gem for RSpec
License: MIT
URL: https://rubygems.org/gems/guard-rspec
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(launchy)
#BuildRequires: rubygem(gem_isolator)
BuildRequires: rubygem(guard-compat)
BuildArch: noarch

%description
Guard::RSpec automatically run your specs (much like autotest).


%package doc
Summary: Documentation for %{name}
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
  rspec -Ilib spec :|| 
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%exclude %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/guard-rspec.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Tue Dec 05 2018 Ilya Gradina <ilya.gradina@gmail.com> - 4.7.3-1
- update to 4.7.3

* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.6.4-1
- Initial package
