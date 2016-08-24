%global gem_name emoji

Name: rubygem-%{gem_name}
Version: 1.0.7
Release: 1%{?dist}
Summary: A Ruby gem. For emoji.
Group: Development/Languages
License: MIT
URL: http://github.com/wpeterson/emoji
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
This gem exposes the Phantom Open Emoji library unicode/image assets
and APIs for working with them. Easily lookup emoji name, unicode character,
or image assets and convert emoji representations.


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
  export LC_CTYPE=en_US.UTF-8
  sed -i "/require 'bundler/ s/^/#/" test/test_helper.rb
  ruby -Ilib -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/assets
%{gem_instdir}/config
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/emoji.gemspec
%exclude %{gem_instdir}/test

%changelog
* Wed Aug 24 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.7-1
- update to 1.0.7

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.5-1
- Initial package
