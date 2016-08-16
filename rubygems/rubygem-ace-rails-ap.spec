# Generated from ace-rails-ap-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ace-rails-ap

Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 1%{?dist}
Summary: The Ajax.org Cloud9 Editor (Ace) for the Rails 3.1 asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/codykrieger/ace-rails-ap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

%description
The Ajax.org Cloud9 Editor (Ace) for the Rails 3.1 asset pipeline.


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
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/update.sh
%exclude %{gem_instdir}/vendor
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Aug 16 2016 Ilya Gradina <ilya.gradina@gmail.com> - 4.1.0-1
- update to new version 4.1.0

* Fri Sep 18 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.0.0-1
- Initial package
