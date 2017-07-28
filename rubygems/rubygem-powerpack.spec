%global gem_name powerpack

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 3%{?dist}
Summary: A few useful extensions to core Ruby classes
License: MIT
URL: https://github.com/bbatsov/powerpack
# git clone git@github.com:bbatsov/powerpack.git
# cd powerpack && git checkout 649d4553f5752928c7c2ae36c42ff176c93b2940
# gem build powerpack.gemspec
Source0: %{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(yard)
BuildArch: noarch

%description
A few useful extensions to core Ruby classes.


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
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/powerpack.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Fri Jul 28 2017 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-3
- new version from commit(Fixing the tests and the definition of sum)

* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-2
- changes in files

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-1
- Initial package
