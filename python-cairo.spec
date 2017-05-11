%define debug_package %{nil}
%define oname pycairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.13.1
Release:	1
License:	LGPLv2+
Group:		Development/Python
Url:		http://pycairo.readthedocs.io/
Source0:	https://github.com/pygobject/pycairo/archive/v%{version}.tar.gz
Source2:	python-cairo.rpmlintrc
Patch0:		pycairo-1.10.0-link.patch
Patch1:		pycairo-1.10.0-fix-waf-build.patch
Patch2:		cairo-waf-use-python-config-as-shell-script.patch
Patch3:		81_pickling-again.patch
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

%description devel
Development files for python2-cairo.

%prep
%setup -qn %{oname}-%{version} -c -a 0

cp -a %{oname}-%{version} python2
mv %{oname}-%{version} python3


%build
pushd python2
PYTHON=python2 python2 setup.py build
popd

pushd python3
python setup.py build
popd

%install

pushd python2
python2 setup.py install --root="%{buildroot}"
popd

pushd python3
python setup.py install --root="%{buildroot}"
popd

%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}/
%endif

%files 
%{py3_platsitedir}/cairo
%{py3_platsitedir}/*.egg-info

%files -n python2-cairo
%{py2_platsitedir}/cairo
%{py2_platsitedir}/*.egg-info

%files devel
%attr(755, root, root) %doc python2/examples
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc

%files -n python2-cairo-devel
%attr(755, root, root) %doc python3/examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc
