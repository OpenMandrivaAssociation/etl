%define	_enable_debug_packages	%{nil}
%define	debug_package		%{nil}

%define oname ETL
%define devname %mklibname %{name} -d

Summary:	Template library for synfig
Name:		etl
Version:	0.04.17
Release:	2
License:	GPLv2+
Group:		Development/C++
Url:		https://www.synfig.org
Source0:	http://downloads.sourceforge.net/synfig/%{oname}-%{version}.tar.gz
Patch0:		etl-0.04.15-cflags.patch

%description
Voria ETL is a multi-platform class and template library designed to add new
data types and functions which combine well with the existing types and
functions from the C++ Standard Template Library (STL).

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Template library for synfig
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Provides:	%{name} = %{EVRD}

%description -n %{devname}
Voria ETL is a multi-platform class and template library designed to add new
data types and functions which combine well with the existing types and
functions from the C++ Standard Template Library (STL).

%files -n %{devname}
%doc AUTHORS README NEWS
%{_bindir}/%{oname}-config
%{_includedir}/%{oname}
%{_libdir}/pkgconfig/%{oname}.pc

#----------------------------------------------------------------------------

%prep
%setup -q  -n %{oname}-%{version}
%patch0 -p1

%build
autoreconf -fi
%configure
%make

%install
%makeinstall_std

