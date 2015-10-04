# Generated from jquery-atwho-rails-1.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-atwho-rails

Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 1%{?dist}
Summary: jquery plugin: @mentions
Group: Development/Languages
License: MIT
URL: http://ichord.github.com/jquery-atwho-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(generator_spec)
BuildArch: noarch

%description
This is a jQuery plugin
that implement Github-like mentions.


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
  ruby -Ilib -e 'Dir.glob "./spec/spec_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Appraisals
%license %{gem_instdir}/LICENSE-MIT
%{gem_instdir}/bower.json
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.md
%exclude %{gem_instdir}/jquery-atwho-rails.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.3.2-1
- Initial package
