%define name gpass
%define version 0.5.1
%define release %mkrel 8

Name:          %name
Summary:       A password manager for the GNOME desktop
Version:       %version
Release:       %release
License:       GPL
Group:         Databases
Source:        http://projects.netlab.jp/gpass/release/%{name}-%{version}.tar.bz2
Patch0: gpass-0.5.1-fix-str-fmt.patch
Patch1: gpass-0.5.1-link.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
BuildRequires: libmhash-devel
BuildRequires: libglade2.0-devel 
BuildRequires: libmcrypt-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnomeui2-devel
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

%build
%configure2_5x
%make 

%install
rm -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL README NEWS TODO
%{_bindir}/*
%{_datadir}/gpass/*
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/gconf/schemas/gpass.schemas
%{_mandir}/man1/gpass*
%{_datadir}/pixmaps/gpass-icon.png



