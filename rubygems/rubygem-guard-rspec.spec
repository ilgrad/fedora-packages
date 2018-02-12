%global gem_name guard-rspec

Name:           rubygem-%{gem_name}
Version:        4.7.3
Release:        3%{?dist}
Summary:        Guard gem for RSpec

License:        MIT
URL:            https://rubygems.org/gems/guard-rspec
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(launchy)
BuildRequires:  rubygem(guard-compat)

BuildArch:      noarch

%description
Guard::RSpec automatically run your specs (much like autotest).


%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

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


%check
mv spec/acceptance/formatter_spec.rb{,.disabled}
rspec --exclude-pattern '**/guard/*_formatter_spec.rb, **/rspec/*_process_spec.rb' -f d


%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}
%{gem_instdir}/Guardfile
%{gem_instdir}/gemfiles
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/guard-rspec.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Mon Feb 12 2018 Ilya Gradina <ilya.gradina@gmail.com> - 4.7.3-3
- excluded few tests group 

* Sun Feb 11 2018 Ilya Gradina <ilya.gradina@gmail.com> - 4.7.3-2
- small fix 

* Tue Dec 05 2017 Ilya Gradina <ilya.gradina@gmail.com> - 4.7.3-1
- update to 4.7.3

* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.6.4-1
- Initial package
