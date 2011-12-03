%define oname py2cairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.8.10
Release:	4
License:	LGPLv2+
Group:		Development/Python
URL:		http://cairographics.org/pycairo
Source:		http://cairographics.org/releases/%{oname}-%{version}.tar.gz
Patch0:		pycairo-1.8.10-link.patch
BuildRequires:	cairo-devel >= 1.8.10
BuildRequires:	python-devel

%description
Aset of Python bindings for the cairo graphics library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n pycairo-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%files 
%doc AUTHORS
%{py_platsitedir}/cairo

%files devel
%doc examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc
