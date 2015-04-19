%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		libkcddb
Summary:	KDE4 library for retrieving and sending CDDB information
Version:	15.04.0
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://projects.kde.org/projects/kde/kdemultimedia/libkcddb
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:14.12.0-1
- New version 14.12.0

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Tue Jul 10 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.95-1
+ Revision: 808786
- imported package libkcddb

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Follow upstream and move libcdddb from kdemultimedia4 to own packageset
