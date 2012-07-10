Name:		libkcddb
Summary:	KDE4 library for retrieving and sending CDDB information
Version:	4.8.95
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libmusicbrainz5)
Conflicts:	%{_lib}kcddb4 < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95

%description
KDE4 library for retrieving and sending CDDB information.

%files
%{_kde_datadir}/config.kcfg/libkcddb.kcfg
%{_kde_services}/libkcddb.desktop
%{_kde_docdir}/HTML/en/kcontrol/cddbretrieval
%{_kde_appsdir}/kconf_update/kcmcddb-emailsettings.upd
%{_kde_libdir}/kde4/kcm_cddb.so

#------------------------------------------------------------------------------
%define kcddb_major 4
%define libkcddb %mklibname kcddb %{kcddb_major}

%package -n %{libkcddb}
Summary:	%{name} library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libkcddb}
KDE4 library for retrieving and sending CDDB information.

%files -n %{libkcddb}
%{_kde_libdir}/libkcddb.so.%{kcddb_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcddb} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.95

%description devel
KDE4 library for retrieving and sending CDDB information.

This package contains header files needed if you wish to build applications
based on libkcddb.

%files devel
%{_kde_libdir}/libkcddb.so
%{_kde_libdir}/cmake/libkcddb
%{_kde_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

