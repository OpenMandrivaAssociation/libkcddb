#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

%bcond_without qt5

Name:		libkcddb
Summary:	KDE library for retrieving and sending CDDB information
Version:	24.05.0
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/libkcddb/-/archive/%{gitbranch}/libkcddb-%{gitbranchd}.tar.bz2#/libkcddb-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:  cmake
BuildRequires:  cmake(ECM)
%if %{with qt5}
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
%endif
BuildRequires:	pkgconfig(libmusicbrainz5)
%rename	libkcddb5
Obsoletes:	%{mklibname KF5CddbWidgets 5} < %{EVRD}
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

%description
KDE library for retrieving and sending CDDB information.

%files -f libkcddb.lang -f kcmcddb.lang -f kcontrol.lang
%{_datadir}/applications/kcm_cddb.desktop
%{_datadir}/config.kcfg/libkcddb5.kcfg

%package plasma5
Summary:	Plasma 5.x integration for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plasma5
Plasma 5.x integration for %{name}

%if %{with qt5}
%files plasma5
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_datadir}/qlogging-categories5/libkcddb.categories
%endif

%package plasma6
Summary:	Plasma 6.x integration for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plasma6
Plasma 6.x integration for %{name}

%files plasma6
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_datadir}/qlogging-categories6/libkcddb.categories

#------------------------------------------------------------------------------

%define kcddb_major 5
%define libkcddb %mklibname KF5Cddb

%libpackage KF5Cddb %{kcddb_major}

%define libkcddb6 %mklibname KCddb6
%libpackage KCddb6 5

%define devel %mklibname KF5Cddb -d
%define devel6 %mklibname KCddb6 -d

#------------------------------------------------------------------------------

%package -n %{devel}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb} = %{EVRD}
Obsoletes:	%{name}-devel < 3:%{version}

%description -n %{devel}
KDE library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%if %{with qt5}
%files -n %{devel}
%{_libdir}/libKF5Cddb.so
%{_libdir}/cmake/KF5Cddb
%{_includedir}/KF5/KCddb
%{_includedir}/KCddb5
%{_libdir}/qt5/mkspecs/modules/qt_KCddb.pri
%endif
                   
#------------------------------------------------------------------------------

%package -n %{devel6}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb6} = %{EVRD}

%description -n %{devel6}
KDE library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%files -n %{devel6}
%{_libdir}/libKCddb6.so
%{_libdir}/cmake/KCddb6
%{_includedir}/KCddb6
%{_libdir}/qt6/mkspecs/modules/qt_KCddb.pri
#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkcddb-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=6 \
        -G Ninja

%if %{with qt5}
cd ..
export CMAKE_BUILD_DIR=build-qt5
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=5 \
        -G Ninja
%endif

%build
%ninja_build -C build
%if %{with qt5}
%ninja_build -C build-qt5
%endif

%install
%if %{with qt5}
%ninja_install -C build-qt5
%endif
%ninja_install -C build

%find_lang libkcddb
%find_lang kcmcddb
%find_lang kcontrol --with-html
