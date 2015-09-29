# Generated from carrierwave-0.10.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name carrierwave

Name: rubygem-%{gem_name}
Version: 0.10.0
Release: 1%{?dist}
Summary: Ruby file upload library
Group: Development/Languages
License: MIT
URL: https://github.com/carrierwaveuploader/carrierwave
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(fog)
BuildRequires: rubygem(generator_spec)
BuildRequires: rubygem(mini_magick)
BuildRequires: rubygem(mysql2)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rmagick)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sham_rack)
BuildRequires: rubygem(timecop)
BuildArch: noarch

%description
Upload files in your Ruby applications, map them to a range of ORMs, store
them on different backends.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Sep 29 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.10.0-1
- Initial package
