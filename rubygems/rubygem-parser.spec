%global gem_name parser

Name: rubygem-%{gem_name}
Version: 2.3.1.2
Release: 1%{?dist}
Summary: A Ruby parser written in pure Ruby
Group: Development/Languages
License: MIT
URL: https://github.com/whitequark/parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(ast)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(coveralls)
BuildArch: noarch

%description
A Ruby parser written in pure Ruby.


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
  ruby -I test test/test_*.rb
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{_bindir}/ruby-parse
%{_bindir}/ruby-rewrite
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/parser.gemspec
%exclude %{gem_instdir}/test

%changelog
* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.3.1.2-1
- update to 2.3.1.2

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.2.2.6-1
- Initial package
