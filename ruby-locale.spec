# TODO
# - remove win32 stuff? lib/locale/driver/win32*
Summary:	Ruby-Locale is the pure ruby library which provides basic APIs for localization
Name:		ruby-locale
Version:	0.9.0
Release:	0.1
License:	LGPL
Source0:	http://rubyforge.org/frs/download.php/47860/%{name}-%{version}.tar.gz
# Source0-md5:	4dafd0c3179fb1cd0da04458ffd90663
Group:		Development/Languages
URL:		http://www.yotabanana.com/hiki/ruby-locale.html
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Ruby-Locale is the pure ruby library which provides basic APIs for
localization.

%package rdoc
Summary:	Documentation files for MODULE_NAME
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for Locale

%prep
%setup -q

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{ruby_rubylibdir}/locale.rb
%{ruby_rubylibdir}/locale

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Locale
