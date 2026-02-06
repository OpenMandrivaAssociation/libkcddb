#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		libkcddb
Summary:	KDE library for retrieving and sending CDDB information
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcddb
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/libkcddb/-/archive/%{gitbranch}/libkcddb-%{gitbranchd}.tar.bz2#/libkcddb-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:  cmake(ECM)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6KCMUtils)
%rename	libkcddb5
Obsoletes:	%{mklibname KF5CddbWidgets 5} < %{EVRD}
Obsoletes:	%{mklibname KF5Cddb 5} < %{EVRD}

%description
KDE library for retrieving and sending CDDB information.

%files -f %{name}.lang
%{_datadir}/applications/kcm_cddb.desktop
%{_datadir}/config.kcfg/libkcddb5.kcfg

%package plasma6
Summary:	Plasma 6.x integration for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{name}-plasma5 < %{EVRD}

%description plasma6
Plasma 6.x integration for %{name}

%files plasma6
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_datadir}/qlogging-categories6/libkcddb.categories

#------------------------------------------------------------------------------

%define libkcddb6 %mklibname KCddb6
%libpackage KCddb6 5

%define devel5 %mklibname KF5Cddb -d
%define devel %mklibname KCddb6 -d

#------------------------------------------------------------------------------

%package -n %{devel}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb6} = %{EVRD}
Obsoletes:	%{devel5} < %{EVRD}

%description -n %{devel}
KDE library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%files -n %{devel}
%{_libdir}/libKCddb6.so
%{_libdir}/cmake/KCddb6
%{_includedir}/KCddb6
%{_libdir}/qt6/mkspecs/modules/qt_KCddb.pri
