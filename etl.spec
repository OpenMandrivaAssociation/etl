%define oname	ETL

Name:		etl
Summary:	Template library for synfig
Version:	0.04.12
Release:	%mkrel 2
Source0:	http://downloads.sourceforge.net/synfig/%{oname}-%{version}.tar.gz
URL:		http://www.synfig.org
License:	GPLv2+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
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

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_bindir}/%{oname}-config
%{_includedir}/%{oname}
%{_libdir}/pkgconfig/%{oname}.pc

