%define oname py2cairo

Summary:	A python wrapper for the Cairo libraries
Name:		python-cairo
Version:	1.10.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
URL:		http://cairographics.org/pycairo
Source:		http://cairographics.org/releases/%{oname}-%{version}.tar.bz2
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
touch ChangeLog

%build
autoreconf -fi
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



%changelog
* Sun Apr 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.0-1
+ Revision: 794485
- new version 1.10.0
- patch rediff (mga)
- cleaned up spec

* Sat Dec 03 2011 Zé <ze@mandriva.org> 1.8.10-4
+ Revision: 737361
- clean defattr, BR and clean section
- remove explicite requires since already exist by default
- clean useless provides
- clean mkrel

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.8.10-3
+ Revision: 722027
- Rebuild with newer libpng.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.10-2
+ Revision: 667914
- mass rebuild

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 1.8.10-1
+ Revision: 648272
- new version 1.8.10

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1.8.8-2mdv2011.0
+ Revision: 589933
- rebuild for python 2.7

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 1.8.8-1mdv2010.1
+ Revision: 487780
- New version 1.8.8

* Thu Jun 25 2009 Frederic Crozat <fcrozat@mandriva.com> 1.8.6-1mdv2010.0
+ Revision: 389064
- Remove obsolete buildrequires
- Fix dependencies
- Release 1.8.6

* Sun May 10 2009 Götz Waschk <waschk@mandriva.org> 1.8.4-1mdv2010.0
+ Revision: 374076
- update to new version 1.8.4

* Thu Jan 15 2009 Frederic Crozat <fcrozat@mandriva.com> 1.8.2-1mdv2009.1
+ Revision: 329720
- Release 1.8.2

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.12-3mdv2009.1
+ Revision: 318656
- rebuild for python 2.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.12-2mdv2009.0
+ Revision: 225128
- rebuild

* Mon Feb 25 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.12-1mdv2008.1
+ Revision: 174515
- new release 1.4.12

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Fri Oct 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.0-1mdv2008.1
+ Revision: 100383
- new version
- new license policy
- remove patch 2, as it is not needed anymore
- move development files to its own package
- use macros wherever it is possible
- spec file clean


* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2007.0
+ Revision: 91720
- new version

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdv2007.1
+ Revision: 88002
- Import python-cairo

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdv2007.1
- Rebuild

* Wed Aug 30 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.0
- fix deps
- drop patch 3
- New release 1.2.2

* Wed Jun 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-3mdv2007.0
- patch 3: fix broken symbols (#23226)

* Wed Jun 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-2mdv2007.0
- rebuild b/c of broken symbols on x86_64 (thus preventing avahi to rebuild)

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.6-1mdv2007.0
- Release 1.1.6
- Remove patch1 (merged upstream)

* Tue Feb 28 2006 Stefan van der Eijk <stefan@eijk.nu> 1.0.2-2mdk
- BuildRequires: automake1.8

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-1mdk
- Release 1.0.2
- use mkrel
- allow bootstrapping to build pygtk before pycairo

* Sun Oct 09 2005 Tigrux <tigrux@ximian.com> 1.0.0-1mdk
- new version
- modified autoconf.ac to enable pygtk support

* Fri Aug 12 2005 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdk
- new version
- fix URLs

* Sat Jul 09 2005 Tigrux <tigrux@ximian.com> 0.5.1-1mdk
- New release 0.5.1

* Tue May 24 2005 Tigrux <tigrux@ximian.com> 0.5.0-1mdk
- New version 0.5.0
- Patched for compiling with gcc4
- Added /usr/include/pycairo/pycairo.h and /usr/lib64/pkgconfig/pycairo.pc 
  to the spec.
- Added Requires cairo >= 1.2.6 since this version does not work with prior versions.

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 0.4.0-2mdk
- remove requires on cairo ( autodetected )
- from Tigrux <tigrux@ximian.com>
  - Do not require python = 2.5

* Wed Apr 27 2005 Michael Scherer <misc@mandriva.org> 0.4.0-1mdk
- from Tigrux <tigrux@ximian.com>
  - New version

* Mon Dec 06 2004 Tigrux <tigrux@ximian.com> 0.1.3-1mdk
- New version

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.1-0.20040914.2mdk
- Rebuild for new python

* Sat Sep 18 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1-0.20040914.1mdk
- from Tigrux <tigrux@ximian.com> : 
	- First RPM for Mandrake

