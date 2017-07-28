%global gem_name bacon-colored_output

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 1%{?dist}
Summary: Colored output for Bacon test framework! http://i.imgur.com/EpTpw.png
Group: Development/Languages
License: MIT
URL: https://github.com/whitequark/bacon-colored_output 
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bacon)
BuildArch: noarch

%description
Colored output for Bacon test framework! http://i.imgur.com/EpTpw.png.


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
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/bacon-colored_output.gemspec

%changelog
* Fri Jul 28 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.1.1-1
- update to 1.1.1

* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.1-2
- changes in files

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.1-1
- Initial package
