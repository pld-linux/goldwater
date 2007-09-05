Summary:	Messaging Middleware
Summary(pl.UTF-8):	Oprogramowanie pośredniczące w komunikacji
Name:		goldwater
Version:	1.4.0
Release:	4
License:	GPL
Group:		Applications
Source0:	http://www.nfluid.com/download/src/%{name}-%{version}.tgz
# Source0-md5:	c9b80c0983603782f4d2f0d352c0520c
Patch0:		%{name}-no_termcap.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-soname.patch
Patch3:		%{name}-pic.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libuuid-devel
BuildRequires:	phlib-devel >= 1.17
BuildRequires:	readline-devel >= 4.2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An inherently distributed middleware natively supporting clustering
and automatic fail-over, Goldwater provides high-availability,
connection pooling, resource control, load balancing, process
management, sandboxing and various security layers.

%description -l pl.UTF-8
Jako nieodłącznie dystrybuowane oprogramowanie pośredniczące natywnie
wspierające klastrowanie i automatyczne odtwarzanie po awarii,
Goldwater zapewnia wysoką dostępność, gospodarowanie połączeniami,
kontrolę zasobów, rozkładanie obciążenia, zarządzanie procesami,
uruchamianie w odizolowanym środowisku (sandboxing) oraz różne warstwy
bezpieczeństwa.

%package libs
Summary:	Goldwater Messaging Middleware - libraries
Summary(pl.UTF-8):	Goldwater Messaging Middleware - biblioteki
Group:		Libraries

%description libs
Goldwater Messaging Middleware - Libraries.

%description libs -l pl.UTF-8
Goldwater Messaging Middleware - Biblioteki.

%package devel
Summary:	Goldwater Messaging Middleware - development files
Summary(pl.UTF-8):	Goldwater Messaging Middleware - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	phlib-devel >= 1.17

%description devel
Goldwater Messaging Middleware - development files.

%description devel -l pl.UTF-8
Goldwater Messaging Middleware - pliki dla programistów.

%package static
Summary:	Goldwater Messaging Middleware - static libraries
Summary(pl.UTF-8):	Goldwater Messaging Middleware - statyczne biblioteki
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	phlib-static >= 1.17

%description static
Goldwater Messaging Middleware - static libraries.

%description static -l pl.UTF-8
Goldwater Messaging Middleware - statyczne biblioteki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal} -I .
%{__autoconf}
%configure \
	cflags=our
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/Goldwater.dll

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
