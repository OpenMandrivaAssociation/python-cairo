%define debug_package %{nil}
%define oname py2cairo
%define oname3 pycairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.10.0
Release:	7
License:	LGPLv2+
Group:		Development/Python
Url:		http://cairographics.org/pycairo
Source0:	http://cairographics.org/releases/%{oname}-%{version}.tar.bz2
Source1:	http://cairographics.org/releases/%{oname3}-%{version}.tar.bz2
Patch0:		pycairo-1.10.0-link.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python)

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

%package -n python3-cairo
Summary:	A python wrapper for the Cairo libraries
Group:		Development/Python
Provides:	python3-cairo = %{version}-%{release}
Provides:	py3cairo = %{version}-%{release}
BuildRequires:	pkgconfig(python3)

%description -n python3-cairo
A set of Python3 bindings for the cairo graphics library.

%package -n python3-cairo-devel
Summary:	Development files for python3-cairo
Group:		Development/Python
Requires:	python3-cairo = %{version}-%{release}
Provides:	python3-cairo-devel = %{version}-%{release}

%description devel
Development files for python3-cairo.

%prep
%setup -qn %{oname}-%{version} -c -a 0
%setup -qn %{oname3}-%{version} -c -a 1

%patch0 -p0

mv %{oname}-%{version} python2
mv %{oname3}-%{version} python3
touch python2/ChangeLog
#touch python3/ChangeLog

%build
pushd python2
autoreconf -fi
%configure2_5x
%make
popd

pushd python3
PYTHON=%__python3 %__python3 waf configure
PYTHON=%__python3 %__python3 waf build
popd

%install
pushd python2
%makeinstall_std
popd

pushd python3
PYTHON=%__python3 %__python3 waf install --destdir="%{buildroot}"
popd

mkdir -p %{buildroot}%{py3_platsitedir}
mv %{buildroot}/usr/local/lib/python%{py3_ver}/site-packages/* %{buildroot}%{py3_platsitedir}

#rm -rf %{buildroot}/usr/local/*
mv %{buildroot}/usr/local/include/pycairo/* %{buildroot}%{_includedir}/pycairo/
mv %{buildroot}/usr/local/lib/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/


%files 
%doc python2/AUTHORS
%{py_platsitedir}/cairo

%files -n python3-cairo
%attr(755, root, root) %doc python3/AUTHORS
%{py3_platsitedir}/cairo

%files devel
%attr(755, root, root) %doc python2/examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc

%files -n python3-cairo-devel
%attr(755, root, root) %doc python3/examples
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc

