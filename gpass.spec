%define name gpass
%define version 0.5.1
%define release %mkrel 9

Name:          %name
Summary:       A password manager for the GNOME desktop
Version:       %version
Release:       %release
License:       GPL
Group:         Databases
Source0:        http://projects.netlab.jp/gpass/release/%{name}-%{version}.tar.bz2
Patch0: gpass-0.5.1-fix-str-fmt.patch
Patch1: gpass-0.5.1-link.patch
Patch2:	gpass-0.5.1-glibh.patch
BuildRequires: libmhash-devel
BuildRequires: pkgconfig(libglade-2.0) 
BuildRequires: libmcrypt-devel
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: perl(XML::Parser)

%description
The GNOME Password Manager - GPass for short - is a simple application,
written for the GNOME 2 desktop, that lets you manage a collection of
passwords. The password collection is stored in an encrypted file,
protected by a master-password.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p2 -b .glibh

%build
%configure2_5x
%make 

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%find_lang %name

%files -f %{name}.lang
%doc AUTHORS COPYING INSTALL README NEWS TODO
%{_bindir}/*
%{_datadir}/gpass/*
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/gconf/schemas/gpass.schemas
%{_mandir}/man1/gpass*
%{_datadir}/pixmaps/gpass-icon.png





%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.5.1-9mdv2011.0
+ Revision: 677724
- rebuild to add gconftool as req

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-8mdv2011.0
+ Revision: 610973
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 0.5.1-7mdv2010.1
+ Revision: 507387
- fix linkage
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - normalize call to ldconfig in %%post/%%postun

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-4mdv2008.1
+ Revision: 136460
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Emmanuel Andry <eandry@mandriva.org> 0.5.1-4mdv2007.0
+ Revision: 93897
- add buildrequires libGConf2-devel libgnomeui2-devel

* Thu Aug 17 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.1-3mdv2007.0
+ Revision: 56442
- Rebuild for new dbus
- import gpass-0.5.1-2mdk

