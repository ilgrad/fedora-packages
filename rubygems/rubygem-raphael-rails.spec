# Generated from raphael-rails-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name raphael-rails

Name: rubygem-%{gem_name}
Version: 2.1.2
Release: 1%{?dist}
Summary: Raphael JS as a Rubygem
Group: Development/Languages
License: MIT
URL: https://github.com/mockdeep/raphael-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Raphael JS as a Rubygem for use in the Rails asset pipeline.


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
%{gem_libdir}
%license %{gem_instdir}/license.txt
%exclude %{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Sat Oct 03 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.2-1
- Initial package
