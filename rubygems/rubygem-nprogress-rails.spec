# Generated from nprogress-rails-0.1.6.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name nprogress-rails

Name: rubygem-%{gem_name}
Version: 0.1.6.7
Release: 1%{?dist}
Summary: Slim progress bars for Ajax'y applications. Inspired by Google, YouTube, and Medium
Group: Development/Languages
License: MIT
URL: https://github.com/caarlos0/nprogress-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(sass-rails)
# BuildRequires: rubygem(sass)
BuildArch: noarch

%description
This is a gem for the rstacruz' nprogress implementation. It's based on
version nprogress 0.1.6.


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
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%%exclude %{gem_instdir}/nprogress-rails.gemspec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.6.7-1
- Initial package
