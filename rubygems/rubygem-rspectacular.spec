%global gem_name rspectacular

Name: rubygem-%{gem_name}
Version: 0.70.7
Release: 1%{?dist}
Summary: RSpec Support And Matchers
Group: Development/Languages
License: MIT
URL: https://github.com/jfelchner/rspectacular
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/thekompanee/rspectacular/blob/master/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(fuubar)
BuildArch: noarch

%description
We rock some RSpec configurations and matchers like it ain't nobody's bidnezz.


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
cp  -p %{SOURCE1} .
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
%doc %{gem_instdir}/README.md
%license LICENSE
%exclude %{_bindir}/deploy
%exclude %{_bindir}/rspectacular_test_bootstrap
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Rakefile

%changelog
* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.70.7-1
- Initial package
