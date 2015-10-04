# Generated from rb-fsevent-0.9.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rb-fsevent

Name: rubygem-%{gem_name}
Version: 0.9.6
Release: 1%{?dist}
Summary: Very simple & usable FSEvents API
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/rb-fsevent
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
FSEvents API with Signals catching (without RubyCocoa).


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

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_instdir}/ext
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/rb-fsevent.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Sun Oct 04 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.9.6-1
- Initial package
