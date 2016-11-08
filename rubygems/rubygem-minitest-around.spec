%global gem_name minitest-around

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Summary: Around block for minitest
Group: Development/Languages
License: MIT
URL: https://github.com/splattael/minitest-around
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(cucumber)
BuildArch: noarch

%description
Alternative for setup/teardown dance.


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
  sed -i "/require 'bundler/ s/^/#/" test/helper.rb
  RUBYOPT=-Ilib ruby -e 'Dir.glob "./test/*_{test,spec}.rb", &method(:require)'
  RUBYOPT=-Ilib cucumber --tag ~@todo --tag ~@rspec
  RUBYOPT=-Ilib rdoc --all --markup markdown
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/config
%exclude %{gem_instdir}/features
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/examples
%exclude %{gem_instdir}/minitest-around.gemspec
%exclude %{gem_instdir}/test

%changelog
* Tue Nov 08 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.0-2
- fix tests
 
* Sat Nov 05 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.0-1
- update to 0.4.0

* Tue Aug 16 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.3.2-2
- changes in files hierarchy

* Tue Sep 29 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.3.2-1
- Initial package
