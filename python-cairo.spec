%define oname pycairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.4.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Python
Url:		http://cairographics.org/pycairo
Source:		http://cairographics.org/releases/%{oname}-%{version}.tar.bz2
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	libpython-devel
BuildRequires:	python-numeric-devel
Requires:	cairo >= 1.4
Provides:	%{oname}

%description
Aset of Python bindings for the cairo graphics library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	libcairo-devel => 1.4
Requires:	%{name} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{py_platsitedir}/cairo

%files devel
%defattr(-,root,root)
%doc examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc
