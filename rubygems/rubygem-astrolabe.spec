# Generated from astrolabe-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name astrolabe

Name: rubygem-%{gem_name}
Version: 1.3.1
Release: 1%{?dist}
Summary: An object-oriented AST extension for Parser
Group: Development/Languages
License: MIT
URL: https://github.com/yujinakayama/astrolabe
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(parser)
BuildArch: noarch

%description
An object-oriented AST extension for Parser.


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
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/benchmark
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/astrolabe.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.3.1-1
- Initial package
