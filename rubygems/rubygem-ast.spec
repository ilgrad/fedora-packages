%global gem_name ast

Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 2%{?dist}
Summary: A library for working with Abstract Syntax Trees
License: MIT
URL: https://github.com/whitequark/ast
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bacon)
BuildRequires: rubygem(json_pure)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(rest-client)
BuildRequires: rubygem(kramdown)
BuildArch: noarch

%description
A library for working with Abstract Syntax Trees.


%package doc
Summary: Documentation for %{name}
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
  sed -i  '/colored_output/ s/^/#/' test/helper.rb
  sed -i '/simplecov/, /coveralls/ s/^/#/' test/helper.rb
  sed -i '/SimpleCov\.formatter/ s/^/#/' test/helper.rb
  sed -i '/SimpleCov\.start/,/end/ s/^/#/' test/helper.rb
  cat test/helper.rb
  bacon -Itest -a test/test_*.rb
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.YARD.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%license %{gem_instdir}/LICENSE.MIT
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/ast.gemspec
%exclude %{gem_instdir}/test

%changelog
* Thu Dec 07 2017 Ilya Gradina <ilya.gradina@gmail.com> - 2.3.0-2
- remove  dependencies for tests

* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.3.0-1
- update to 2.3.0

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.0-1
- Initial package
