# Generated from twitter-stream-0.1.16.gem by gem2rpm -*- rpm-spec -*-
%global gem_name twitter-stream

Name: rubygem-%{gem_name}
Version: 0.1.16
Release: 1%{?dist}
Summary: Twitter realtime API client
Group: Development/Languages
License: MIT
URL: http://github.com/voloko/twitter-stream
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(eventmachine)
BuildRequires:rubygem(simple_oauth)
BuildRequires: rubygem(http_parser.rb)
BuildArch: noarch

%description
Simple Ruby client library for twitter streaming API. Uses EventMachine for
connection handling. Adheres to twitter's reconnection guidline. JSON format
only.


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
%license %{gem_instdir}/LICENSE
%{gem_instdir}/VERSION
%{gem_instdir}/fixtures
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/twitter-stream.gemspec

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.16-1
- Initial package
