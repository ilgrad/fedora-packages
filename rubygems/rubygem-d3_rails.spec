%global gem_name d3_rails

Name: rubygem-%{gem_name}
Version: 4.1.1
Release: 1%{?dist}
Summary: D3 automated install for Rails 3.1+
Group: Development/Languages
License: MIT
URL: https://github.com/logical42/d3_rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rails)
BuildRequires: rubygem(pry)
BuildArch: noarch

%description
Gem installation of javascript framework for data visualization, D3.


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



%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE                                                                                                                   
%license %{gem_instdir}/MIT_LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/app
%exclude %{gem_instdir}/tasks
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/d3_rails.gemspec

%changelog
* Tue Aug 30 2016 Ilya Gradina <ilya.gradina@gmail.com> - 4.1.1-1
- Initial package
