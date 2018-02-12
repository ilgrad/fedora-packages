%global gem_name bacon-colored_output

Name:           rubygem-%{gem_name}
Version:        1.1.1
Release:        3%{?dist}
Summary:        Colored output for Bacon test framework! http://i.imgur.com/EpTpw.png

License:        MIT
URL:            https://github.com/whitequark/bacon-colored_output 
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel

BuildArch:      noarch

%description
Colored output for Bacon test framework! http://i.imgur.com/EpTpw.png.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/bacon-colored_output.gemspec

%changelog
* Tue Feb 13 2018 Ilya Gradina <ilya.graidna@gmail.com> - 1.1.1-3
- small change in spec file 

* Tue Dec 05 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.1.1-2
- remove bacon from BR
- remove Group part in spec

* Fri Jul 28 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.1.1-1
- update to 1.1.1

* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.1-2
- changes in files

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.1-1
- Initial package
