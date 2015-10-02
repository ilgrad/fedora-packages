# Generated from tinder-1.10.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tinder

Name: rubygem-%{gem_name}
Version: 1.10.1
Release: 1%{?dist}
Summary: Ruby wrapper for the Campfire API
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/tinder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(faraday)
BuildRequires: rubygem(faraday_middleware)
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(hashie)
BuildRequires: rubygem(json)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(multi_json)
BuildRequires: rubygem(twitter-stream)
BuildRequires: rubygem(fakeweb)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
A Ruby API for interfacing with Campfire, the 37Signals chat application.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/init.rb
%{gem_libdir}
%{gem_instdir}/site
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.txt
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/tinder.gemspec

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.10.1-1
- Initial package
