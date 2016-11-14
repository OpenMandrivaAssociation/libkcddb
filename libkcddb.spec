%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		libkcddb
Summary:	KDE4 library for retrieving and sending CDDB information
Version:	16.08.3
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libmusicbrainz5)
Conflicts:	%{_lib}kcddb4 < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95

%description
KDE4 library for retrieving and sending CDDB information.

%files
%{_datadir}/config.kcfg/libkcddb.kcfg                                                                  
%{_datadir}/kde4/services/libkcddb.desktop                                                            
%doc %{_docdir}/HTML/en/kcontrol/cddbretrieval4
%{_libdir}/kde4/kcm_cddb.so  

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
%{_libdir}/libkcddb.so.%{kcddb_major}*

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
%{_libdir}/libkcddb.so                                                                                 
%{_libdir}/cmake/libkcddb                                                                              
%{_includedir}/*                                                                                       
                   
#------------------------------------------------------------------------------

%prep
%setup -q
# fix doc clash with kcddb5
sed -i 's/cddbretrieval/cddbretrieval4/' kcmcddb/libkcddb.desktop kcmcddb/doc/CMakeLists.txt

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

