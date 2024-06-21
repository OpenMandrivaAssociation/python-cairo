#define debug_package %{nil}
%define _empty_manifest_terminate_build 0
%define oname pycairo
%define py3_build CFLAGS="%{optflags}" %{__python3} setup.py build --executable="%{__python3} -s"
%define py3_install CFLAGS="%{optflags}" %{__python3} setup.py install --root="%{buildroot}"

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.26.1
Release:	1
License:	LGPLv2+
Group:		Development/Python
Url:		http://cairographics.org/pycairo
Source0:	https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz
Source1:	python-cairo.rpmlintrc
#Patch0:		pycairo-1.10.0-link.patch
#Patch1:		pycairo-1.10.0-fix-waf-build.patch
#Patch2:		cairo-waf-use-python-config-as-shell-script.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  meson

%description
A set of Python bindings for the cairo graphics library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%description
Aset of Python bindings for the cairo graphics library.

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{py3_platsitedir}/*cairo*

%files devel
#{_includedir}/pycairo/py3cairo.h
#{_libdir}/pkgconfig/py3cairo.pc
