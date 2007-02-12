# TODO
# - convert all plugin packages to store their plugins in this base
#   directory.
# known NPAPI compatible browsers from PLD CVS:
# - mozilla
# - mozilla-firefox
# - konqueror
# - opera (ix86 only)
# - galeon
# - skipstone
# - kazehakase
# - netscape (trigger on netscape-common)
# Extensions are for mozilla based browsers (please complete the list)
# - mozilla
# - mozilla-firefox
# Themes (none exists yet)
Summary:	Base package for web browser components
Summary(pl.UTF-8):   Podstawowy pakiet dla komponentów przeglądarek WWW
Name:		browser-common
Version:	0.9
Release:	0.5
License:	GPL
Group:		Base
URL:		http://www.mozilla.org/projects/plugins/
Provides:	%{name}(%{_target_cpu}) = %{version}-%{release}
# be compatible, so don't need to rebuild all packages depending on browser-plugins
Provides:	browser-plugins(%{_target_cpu})
Obsoletes:	browser-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides base directories for browser components like
plugins, extensions and themes.

%description -l pl.UTF-8
Ten pakiet dostarcza podstawowe katalogi dla komponentów przeglądarek
takich jak wtyczki, rozszerzenia czy motywy.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/browser-common/{themes,extensions}
install -d $RPM_BUILD_ROOT%{_libdir}/browser-common/plugins
touch $RPM_BUILD_ROOT%{_libdir}/browser-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- browser-plugins
if [ -d %{_libdir}/browser-plugins ]; then
	mv -f %{_libdir}/browser-plugins/* %{_libdir}/browser-common/plugins
	rmdir %{_libdir}/browser-plugins
	ln -snf %{_libdir}/browser-common/plugins %{_libdir}/browser-plugins
fi

%files
%defattr(644,root,root,755)
%{_libdir}/browser-common
%{_datadir}/browser-common
# we will own the compat symlink
%ghost %{_libdir}/browser-plugins
