%define pkgname locale
Summary:	Ruby-Locale is the pure ruby library which provides basic APIs for localization
Name:		ruby-%{pkgname}
Version:	2.1.5
Release:	2
License:	Ruby or LGPL v3+
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	f0c4967ac00bd5975df35c57ab059d6b
URL:		https://github.com/ruby-gettext/locale
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-fiddle
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby-Locale is the pure ruby library which provides basic APIs for
localization.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc ChangeLog COPYING
%{ruby_vendorlibdir}/locale.rb
%{ruby_vendorlibdir}/locale
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
