%define oname	ETL
%define devname	%mklibname %{name} -d

%define	_enable_debug_packages	%{nil}
%define debug_package		%{nil}

Name:		etl
Summary:	Template library for synfig
Version:	0.04.15
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/synfig/%{oname}-%{version}.tar.gz
URL:		http://www.synfig.org
License:	GPLv2+
Group:		Development/C++

%description
Voria ETL is a multi-platform class and template library designed to
add new datatypes and functions which combine well with the existing
types and functions from the C++ Standard Template Library (STL). 

%package -n %{devname}
Summary:	Template library for synfig
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Provides:	%{name} = %{EVRD}

%description -n %{devname}
Voria ETL is a multi-platform class and template library designed to
add new datatypes and functions which combine well with the existing
types and functions from the C++ Standard Template Library (STL).

%prep
%setup -q  -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/ETL-config

%files -n %{devname}
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_bindir}/%{oname}-config
%{multiarch_bindir}/%{oname}-config
%{_includedir}/%{oname}
%{_libdir}/pkgconfig/%{oname}.pc
