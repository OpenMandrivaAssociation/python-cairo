%define debug_package %{nil}
%define oname py2cairo
%define oname3 pycairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.10.0
Release:	8
License:	LGPLv2+
Group:		Development/Python
Url:		http://cairographics.org/pycairo
Source0:	http://cairographics.org/releases/%{oname}-%{version}.tar.bz2
Source1:	http://cairographics.org/releases/%{oname3}-%{version}.tar.bz2
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

%description devel
Development files for python2-cairo.

%prep
%setup -qn %{oname}-%{version} -c -a 0
%setup -qn %{oname3}-%{version} -c -a 1

# Ensure that ./waf has created the cached unpacked version
# of the wafadmin source tree.
# This will be created to a subdirectory like
#    .waf3-1.5.18-a7b91e2a913ce55fa6ecdf310df95752
python3 %{oname3}-%{version}/waf --version

%patch0 -p0
%patch1 -p0
%patch2 -p0

mv %{oname}-%{version} python2
mv %{oname3}-%{version} python3
touch python2/ChangeLog
#touch python3/ChangeLog

%build
pushd python2
autoreconf -fi
%configure PYTHON=python2
%make
popd

pushd python3
python waf configure --prefix=%{_prefix} --libdir=%{_libdir} || exit 0
python waf build
popd

%install
pushd python2
%makeinstall_std
popd

pushd python3
python waf install --destdir="%{buildroot}" || exit 0
popd

%files 
%doc python3/AUTHORS
%{py3_platsitedir}/cairo

%files -n python2-cairo
%attr(755, root, root) %doc python2/AUTHORS
%{py2_platsitedir}/cairo

%files devel
%attr(755, root, root) %doc python2/examples
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc

%files -n python2-cairo-devel
%attr(755, root, root) %doc python3/examples
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc

