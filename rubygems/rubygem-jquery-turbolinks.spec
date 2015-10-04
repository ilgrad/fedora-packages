# Generated from jquery-turbolinks-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-turbolinks

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: jQuery plugin for drop-in fix binded events problem caused by Turbolinks
Group: Development/Languages
License: MIT
URL: https://github.com/kossnocorp/jquery.turbolinks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
jQuery plugin for drop-in fix binded events problem caused by Turbolinks.


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
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/NOTES.md
%{gem_libdir}
%{gem_instdir}/package.json
%{gem_instdir}/src
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/jquery-turbolinks.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.0-1
- Initial package
