%define oname	ETL

%define devname	%mklibname %{name} -d

Name:		etl
Summary:	Template library for synfig
Version:	0.04.14
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/synfig/%{oname}-%{version}.tar.gz
URL:		http://www.synfig.org
License:	GPLv2+
Group:		Development/C++
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Voria ETL is a multi-platform class and template library designed to
add new datatypes and functions which combine well with the existing
types and functions from the C++ Standard Template Library (STL). 

%package -n %{devname}
Summary:	Template library for synfig
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{devname}
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_bindir}/%{oname}-config
%{_includedir}/%{oname}
%{_libdir}/pkgconfig/%{oname}.pc

