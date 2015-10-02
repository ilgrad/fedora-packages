# Generated from sidekiq-3.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sidekiq

Name: rubygem-%{gem_name}
Version: 3.5.0
Release: 1%{?dist}
Summary: Simple, efficient background processing for Ruby
Group: Development/Languages
License: LGPL-3.0
URL: http://sidekiq.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(celluloid)
BuildRequires: rubygem(redis)
BuildArch: noarch

%description
Simple, efficient background processing for Ruby.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}
  sed -i "/require 'celluloid\/current/ s/^/#/" test/helper.rb
  ruby -Ilib -e 'Dir.glob "./test/test_sidekiq.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sidekiq
%{_bindir}/sidekiqctl
%exclude %{gem_instdir}/.*
%{gem_instdir}/3.0-Upgrade.md
%license %{gem_instdir}/COMM-LICENSE
%{gem_instdir}/Changes.md
%{gem_instdir}/Ent-Changes.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/Pro-2.0-Upgrade.md
%{gem_instdir}/Pro-Changes.md
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/web
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributing.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/sidekiq.gemspec
%exclude %{gem_instdir}/test

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 3.5.0-1
- Initial package
