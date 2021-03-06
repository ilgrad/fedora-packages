%global gem_name underscore-rails

Name: rubygem-%{gem_name}
Version: 1.8.3
Release: 2%{?dist}
Summary: underscore.js asset pipeline provider/wrapper
Group: Development/Languages
License: MIT
URL: https://github.com/rweng/underscore-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

%description
underscore.js asset pipeline provider/wrapper.


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


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/Readme.md
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/vendor
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/underscore-rails.gemspec

%changelog
* Fri Aug 26 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.8.3-2
- changes in files section

* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.8.3-1
- Initial package
