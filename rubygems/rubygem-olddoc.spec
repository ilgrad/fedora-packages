# Generated from olddoc-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name olddoc

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: old-fashioned Ruby documentation generator
Group: Development/Languages
License: GPLv3+
URL: http://80x24.org/olddoc/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
olddoc contains old-fashioned document generators for those who do not
wish to impose bloated, new-fangled web cruft on their readers.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
%dir %{gem_instdir}
%{_bindir}/olddoc
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_instdir}/Documentation
%{gem_instdir}/GNUmakefile
%{gem_instdir}/INSTALL
%{gem_instdir}/TODO
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/man
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %doc %{gem_instdir}/.*
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%exclude %doc %{gem_instdir}/olddoc.gemspec

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.1-1
- Initial package
