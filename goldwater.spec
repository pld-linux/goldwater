Summary:	Messaging Middleware
Name:		goldwater
Version:	0.3.4
Release:	0.1
Source0:	http://www.nfluid.com/download/src/%{name}-%{version}.tgz
Patch0:		%{name}-no_termcap.patch
License:	GPL
Vendor:		netFluid Technology Limited
Group:		Applications
BuildRequires:	autoconf
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

%package libs
Summary:	Messaging Middleware - Libraries
Summary(pl):	Messaging Middleware - Biblioteki
Group:		Libraries

%description libs
Messaging Middleware - Libraries.

%description libs -l pl
Messaging Middleware - Biblioteki.

%package devel
Summary:	Messaging Middleware - development files
Summary(pl):	Messaging Middleware - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	phlib-devel >= 1.17

%description devel
Messaging Middleware - development files.

%description devel -l pl
Messaging Middleware - pliki dla programistów.

%package static
Summary:	Messaging Middleware - static development files
Summary(pl):	Messaging Middleware - statyczne pliki dla programistów
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	phlib-static >= 1.17

%description static
Messaging Middleware - static development files.

%description static -l pl
Messaging Middleware - statyczne pliki dla programistów.

%prep
%setup -q
%patch0

%build
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
