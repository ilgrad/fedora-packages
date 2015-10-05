# Generated from rubocop-0.34.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubocop

Name: rubygem-%{gem_name}
Version: 0.34.2
Release: 1%{?dist}
Summary: Automatic Ruby code style checking tool
Group: Development/Languages
License: MIT
URL: http://github.com/bbatsov/rubocop
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(yard)
BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
Automatic Ruby code style checking tool.
Aims to enforce the community-driven Ruby Style Guide.


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

# Run the test suite
%check
pushd .%{gem_instdir}
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/rubocop
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/assets
%{gem_instdir}/bin
%{gem_instdir}/config
%{gem_libdir}
%{gem_instdir}/logo
%{gem_instdir}/relnotes
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/rubocop.gemspec

%changelog
* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.34.2-1
- Initial package
