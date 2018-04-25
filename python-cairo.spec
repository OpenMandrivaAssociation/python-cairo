%define debug_package %{nil}
%define oname pycairo
%define py2_build CFLAGS="%{optflags}" %{__python2} setup.py build --executable="%{__python2} -s"
%define py3_build CFLAGS="%{optflags}" %{__python3} setup.py build --executable="%{__python3} -s"
%define py2_install CFLAGS="%{optflags}" %{__python2} setup.py install --root="%{buildroot}"
%define py3_install CFLAGS="%{optflags}" %{__python3} setup.py install --root="%{buildroot}"

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.17.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
Url:		http://cairographics.org/pycairo
Source0:	https://github.com/pygobject/pycairo/archive/v%{version}.tar.gz
Source1:	python-cairo.rpmlintrc
Patch0:		pycairo-1.10.0-link.patch
Patch1:		pycairo-1.10.0-fix-waf-build.patch
Patch2:		cairo-waf-use-python-config-as-shell-script.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python3)

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

%package -n python2-cairo
Summary:	A python wrapper for the Cairo libraries
Group:		Development/Python
Provides:	python2-cairo = %{version}-%{release}
Provides:	py2cairo = %{version}-%{release}
BuildRequires:	pkgconfig(python)

%description -n python2-cairo
A set of Python3 bindings for the cairo graphics library.

%package -n python2-cairo-devel
Summary:	Development files for python3-cairo
Group:		Development/Python
Requires:	python2-cairo = %{version}-%{release}
Provides:	python2-cairo-devel = %{version}-%{release}

%description -n python2-cairo-devel
Development files for python2-cairo.

%prep
%setup -qn %{oname}-%{version}
sed -i -e 's,\(libdir.*\)"lib",\1"%{_lib}",g' setup.py
cp -a . %{py3dir}

%build
%py2_build

pushd %{py3dir}
  %py3_build
popd



%install
%py2_install

pushd %{py3dir}
  %py3_install
popd

%files
%{py3_platsitedir}/*cairo*

%files -n python2-cairo
%{py2_platsitedir}/*cairo*

%files devel
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc

%files -n python2-cairo-devel
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc
