%define libname pycairo

%define build_bootstrap 0

%{expand: %{?_without_bootstrap: %%global build_bootstrap 0}}
%{expand: %{?_with_bootstrap:        %%global build_bootstrap 1}}

Summary: A python wrapper for the Cairo libraries
Name: python-cairo
Version: 1.2.6
Release: %mkrel 1
Source: http://cairographics.org/releases/%{libname}-%{version}.tar.bz2
Patch2: pycairo-1.0.0-pygtk.patch
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: automake1.8
BuildRequires: cairo-devel >= %{version}
BuildRequires: libpython-devel python-numeric-devel
%if !%{build_bootstrap}
BuildRequires: pygtk2.0-devel 
%endif
Requires:	cairo >= %{version}
Url: http://cairographics.org/pycairo
Provides: pycairo

%description
Python wrapper for the Cairo libraries

%prep
%setup -q -n %{libname}-%{version}
%patch2 -p1 -b .pygtk

#needed by patch2
aclocal-1.8
automake-1.8
autoheader
autoconf

%build
%configure2_5x \
%if !%{build_bootstrap}
--with-pygtk
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog examples
%{_libdir}/python%{pyver}/site-packages/cairo
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc


