%global gem_name codeclimate-test-reporter

Name: rubygem-%{gem_name}
Version: 1.0.8
Release: 1%{?dist}
Summary: Uploads Ruby test coverage data to Code Climate
Group: Development/Languages
License: MIT
URL: https://github.com/codeclimate/ruby-test-reporter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/codeclimate/ruby-test-reporter.git && cd ruby-test-reporter
# git checkout v1.0.8 && tar czvf codeclimate-test-reporter-1.0.8-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(pry)
BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}
  tar xzf %{SOURCE1}
  sed -i '/bundler/ s/^/#/' spec/spec_helper.rb
  #rspec -Ilib spec
  rm -rf spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%{_bindir}/cc-tddium-post-worker
%{_bindir}/codeclimate-test-reporter
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/config
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}


%changelog
* Mon Jul 10 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.8-1
- update to 1.0.8

* Wed Sep 14 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.6.0-1
- update to 0.6.0

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.8-1
- Initial package
