# Generated from version_sorter-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name version_sorter

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Summary: Fast sorting of version strings
Group: Development/Languages
License: MIT
URL: https://github.com/defunkt/version_sorter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/github/version_sorter.git && cd version_sorter
# git checkout v2.0.0
# tar cf rubygem-version_sorter-2.0.0-tests.xz test/
Source1: %{name}-%{version}-tests.xz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest)

%description
VersionSorter is a C extension that does fast sorting of large sets of version
strings.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -a 1 -T -n  %{gem_name}-%{version}

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}
  ruby -Ilib -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.0-1
- Initial package
