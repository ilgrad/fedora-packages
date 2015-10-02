# Generated from unicorn-4.9.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicorn

Name: rubygem-%{gem_name}
Version: 4.9.0
Release: 1%{?dist}
Summary: Rack HTTP server for fast clients and Unix
Group: Development/Languages
License: GPLv2+ and Ruby 1.8
URL: http://unicorn.bogomips.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(kgio)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(raindrops)
BuildRequires: rubygem(minitest)

%description
\Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between \Unicorn and slow clients.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/unicorn
%{_bindir}/unicorn_rails
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Application_Timeouts
%license %{gem_instdir}/COPYING
%{gem_instdir}/DESIGN
%{gem_instdir}/Documentation
%{gem_instdir}/FAQ
%{gem_instdir}/GIT-VERSION-FILE
%{gem_instdir}/GIT-VERSION-GEN
%{gem_instdir}/GNUmakefile
%{gem_instdir}/HACKING
%{gem_instdir}/ISSUES
%{gem_instdir}/KNOWN_ISSUES
%{gem_instdir}/LATEST
%license %{gem_instdir}/LICENSE
%{gem_instdir}/Links
%{gem_instdir}/PHILOSOPHY
%{gem_instdir}/SIGNALS
%{gem_instdir}/Sandbox
%{gem_instdir}/TODO
%{gem_instdir}/TUNING
%{gem_instdir}/archive
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/man
%{gem_instdir}/setup.rb
%{gem_instdir}/t
%{gem_instdir}/unicorn_1
%{gem_instdir}/unicorn_rails_1
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %doc %{gem_instdir}/.*
%doc %{gem_instdir}/CONTRIBUTORS
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/test
%exclude %{gem_instdir}/unicorn.gemspec

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.9.0-1
- Initial package
