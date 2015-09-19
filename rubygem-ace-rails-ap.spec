# Generated from ace-rails-ap-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ace-rails-ap

Name: rubygem-%{gem_name}
Version: 4.0.0
Release: 1%{?dist}
Summary: The Ajax.org Cloud9 Editor (Ace) for the Rails 3.1 asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/codykrieger/ace-rails-ap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rails)
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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.gitmodules
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/update.sh
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ace-rails-ap.gemspec

%changelog
* Fri Sep 18 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.0.0-1
- Initial package
