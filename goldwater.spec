Summary:	Messaging Middleware
Summary(pl):	Oprogramowanie po¶rednicz±ce w komunikacji
Name:		goldwater
Version:	0.3.4
Release:	0.2
License:	GPL
Vendor:		netFluid Technology Limited
Group:		Applications
Source0:	http://www.nfluid.com/download/src/%{name}-%{version}.tgz
# Source0-md5:	e67198137b956e216255df4908ecc4e3
Patch0:		%{name}-no_termcap.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	expat-devel
BuildRequires:	phlib-devel >= 1.17
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An inherently distributed middleware natively supporting clustering
and automatic fail-over, Goldwater provides high-availability,
connection pooling, resource control, load balancing, process
management, sandboxing and various security layers.

%description -l pl
Jako nieod³±cznie dystrybuowane oprogramowanie po¶rednicz±ce natywnie
wspieraj±ce klastrowanie i automatyczne odtwarzanie po awarii,
Goldwater zapewnia wysok± dostêpno¶æ, gospodarowanie po³±czeniami,
kontrolê zasobów, rozk³adanie obci±¿enia, zarz±dzanie procesami,
uruchamianie w odizolowanym ¶rodowisku (sandboxing) oraz ró¿ne warstwy
bezpieczeñstwa.

%package libs
Summary:	Messaging Middleware - libraries
Summary(pl):	Messaging Middleware - biblioteki
Group:		Libraries

%description libs
Messaging Middleware - Libraries.

%description libs -l pl
Messaging Middleware - Biblioteki.

%package devel
Summary:	Goldwater Messaging Middleware - development files
Summary(pl):	Goldwater Messaging Middleware - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	phlib-devel >= 1.17

%description devel
Goldwater Messaging Middleware - development files.

%description devel -l pl
Goldwater Messaging Middleware - pliki dla programistów.

%package static
Summary:	Goldwater Messaging Middleware - static libraries
Summary(pl):	Goldwater Messaging Middleware - statyczne biblioteki
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	phlib-static >= 1.17

%description static
Goldwater Messaging Middleware - static libraries.

%description static -l pl
Goldwater Messaging Middleware - statyczne biblioteki.

%prep
%setup -q
%patch0

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a.*
