#
# spec file for package 
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
%global debug_package %{nil}
Name:       grub-customizer
Version:    5.2.5
Release:    0
License:    GPL-3.0
Summary:    Grub Customizer is a graphical interface to configure the GRUB2/BURG settings 
Group:      System/Management
Url:        https://launchpad.net/grub-customizer/
Source:     https://launchpad.net/grub-customizer/5.2/%{version}/+download/grub-customizer_%{version}.tar.gz
Source99:   %{name}-rpmlintrc
Patch1:     %{name}-desktop.patch
Patch2:     %{name}-grub2.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  grub2
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(libarchive) 
BuildRequires:  pkgconfig(openssl)

# If requires xdg-utils, xdgsu -c should than insert in grub-customizer.destop
# Requires:       xdg-utils
Recommends:     %{name}-lang

%description
Grub Customizer is a graphical interface to configure the GRUB2/BURG settings and menuentries

Features:
 * move, remove or rename menuentries (they stey updatable by update-grub)
 * edit the contents of menuentries or create new ones (internally it edits the 40_custom)
 * support for GRUB2 and BURG
 * reinstallation of the bootloader to MBR
 * settings like default operating system, kernel params, background image and text colors etc.
 * changing the installed operating system by running on a live cd

%package lang
Summary: Lang package for %{name}
BuildArch: noarch

%description lang
%{summary}.

%prep
%autosetup  -p1

%build
cmake -DCMAKE_CXX_FLAGS="-std=c++11" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make %{?_smp_mflags} 

%install
%make_install
%find_lang grub-customizer
#%%fdupes 

%files
%defattr(-,root,root)
/usr/lib/grub-customizer/
%{_datadir}/polkit-1/
%{_datadir}/polkit-1/actions/
/usr/bin/grub-customizer
/usr/lib/grub-customizer/grubcfg-proxy
%{_datadir}/applications/grub-customizer.desktop
%{_datadir}/icons/hicolor/*/apps/grub-customizer.svg
%{_datadir}/man/man1/grub-customizer.1.gz
%{_datadir}/polkit-1/actions/net.launchpad.danielrichter2007.pkexec.grub-customizer.policy

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog

