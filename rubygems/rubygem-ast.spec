# Generated from ast-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ast

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: A library for working with Abstract Syntax Trees
Group: Development/Languages
License: MIT
URL: https://whitequark.github.io/ast/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bacon)
BuildRequires: rubygem(bacon-colored_output)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(coveralls)
BuildArch: noarch

%description
A library for working with Abstract Syntax Trees.


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
  ruby -Ilib -e 'Dir.glob "./test/helper.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.MIT
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.YARD.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/ast.gemspec
%exclude %{gem_instdir}/test

%changelog
* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.0-1
- Initial package
