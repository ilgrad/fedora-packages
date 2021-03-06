%global gem_name simple_oauth

Name:    rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Summary: Simply builds and verifies OAuth headers
Group:   Development/Languages
License: MIT
URL:     https://github.com/laserlemon/simple_oauth
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/laserlemon/simple_oauth.git && cd simple_oauth
# git checkout v0.3.1 && tar czvf simple_oauth-0.3.1-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch: noarch


%description
Simply builds and verifies OAuth headers.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
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
  tar xzf %{SOURCE1}
  sed -i '/simplecov/,/coveralls/ s/^/#/' spec/helper.rb
  sed -i '/SimpleCov\.formatter/ s/^/#/' spec/helper.rb
  sed -i '/SimpleCov\.start/,/end/ s/^/#/' spec/helper.rb
  rspec -Ilib spec
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Fri Oct 02 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.3.1-1
- Initial package
