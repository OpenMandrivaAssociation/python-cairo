%define _disable_ld_no_undefined 1
%define _empty_manifest_terminate_build 0
%define oname pycairo
%define py3_build CFLAGS="%{optflags}" %{__python3} setup.py build --executable="%{__python3} -s"
%define py3_install CFLAGS="%{optflags}" %{__python3} setup.py install --root="%{buildroot}"

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.29.2
Release:	3
License:	LGPLv2+
Group:		Development/Python
Url:		https://cairographics.org/pycairo
Source0:	https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	meson

%description
A set of Python bindings for the cairo graphics library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	%{name} = %{EVRD}
Provides:	%{oname}-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%meson \
        -Dno-x11=false
%meson_build

%install
%meson_install

%files
%{py3_platsitedir}/*cairo*

%files devel
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc
