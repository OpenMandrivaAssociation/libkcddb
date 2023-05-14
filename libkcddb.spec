%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		libkcddb
Summary:	KF5 library for retrieving and sending CDDB information
Version:	23.04.1
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:	pkgconfig(libmusicbrainz5)
%rename	libkcddb5
Obsoletes:	%{mklibname KF5CddbWidgets 5} < %{EVRD}

%description
KF5 library for retrieving and sending CDDB information.

%files -f libkcddb.lang -f kcmcddb.lang -f kcontrol.lang
%{_datadir}/applications/kcm_cddb.desktop
%{_datadir}/config.kcfg/libkcddb5.kcfg
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_datadir}/qlogging-categories5/libkcddb.categories

#------------------------------------------------------------------------------

%define kcddb_major 5
%define libkcddb %mklibname KF5Cddb

%libpackage KF5Cddb %{kcddb_major}

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.95

%description devel
KF5 library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%files devel
%{_libdir}/libKF5Cddb.so
%{_libdir}/cmake/KF5Cddb
%{_includedir}/*                                                                                       
%{_libdir}/qt5/mkspecs/modules/qt_KCddb.pri
                   
#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang libkcddb
%find_lang kcmcddb
%find_lang kcontrol --with-html
