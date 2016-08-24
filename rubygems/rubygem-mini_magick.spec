# Generated from mini_magick-4.3.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mini_magick

Name: rubygem-%{gem_name}
Version: 4.5.1
Release: 1%{?dist}
Summary: Manipulate images with minimal use of memory via ImageMagick / GraphicsMagick
Group: Development/Languages
License: MIT
URL: https://github.com/minimagick/minimagick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/minimagick/minimagick.git && cd minimagick
# git checkout v4.5.1 && tar czvf mini_magick-4.5.1-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(pry)
BuildRequires: rubygem(posix-spawn)
BuildRequires: ImageMagick
BuildRequires: GraphicsMagick
BuildArch: noarch

%description
Manipulate images with minimal use of memory via ImageMagick / GraphicsMagick.


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
  tar xzf %{SOURCE1}
  sed -i '/bundler/ s/^/#/' spec/spec_helper.rb
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Rakefile

%changelog
* Wed Aug 24 2016 Ilya Gradina <ilya.gradina@gmail.com> - 4.5.1-1
- update to 4.5.1

* Fri Sep 18 2015 Ilya Gradina <ilya.gradina@gmail.com> - 4.3.3-1
- Initial package
