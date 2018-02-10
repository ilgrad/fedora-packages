%global gem_name codeclimate-test-reporter

Name:           rubygem-%{gem_name}
Version:        1.0.8
Release:        2%{?dist}
Summary:        Uploads Ruby test coverage data to Code Climate

License:        MIT
URL:            https://github.com/codeclimate/ruby-test-reporter
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/codeclimate/ruby-test-reporter
# git -C ruby-test-reporter archive --format tar.gz v1.0.8 -o $PWD/codeclimate-test-reporter-1.0.8-specs.tar.gz -- spec
Source1: 		%{gem_name}-%{version}-specs.tar.gz

Buildrequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygem(pry)
BuildRequires:  rubygem(simplecov)
BuildRequires:  git-core

BuildArch:      noarch

%description
Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version} -a 1 -S git
sed -i '/bundler/d' spec/spec_helper.rb
sed -i 's/0.13/0.13.0/g' ../%{gem_name}-%{version}.gemspec

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/

# Run the test suite
%check
rspec -Ilib spec

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%{_bindir}/cc-tddium-post-worker
%{_bindir}/%{gem_name}
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/config
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%changelog
* Sat Feb 10 2018 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.8-2
- small fix 

* Mon Jul 10 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.8-1
- update to 1.0.8

* Wed Sep 14 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.6.0-1
- update to 0.6.0

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.8-1
- Initial package
