%define oname py2cairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.10.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
URL:		http://cairographics.org/pycairo
Source:		http://cairographics.org/releases/%{oname}-%{version}.tar.gz
Patch0:		pycairo-1.10.0-link.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python)

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
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%doc AUTHORS
%{py_platsitedir}/cairo

%files devel
%doc examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc

