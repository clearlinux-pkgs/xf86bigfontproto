#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86bigfontproto
Version  : 1.2.0
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-1.2.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-1.2.0.tar.gz
Summary  : XF86BigFont extension headers
Group    : Development/Tools
License  : MIT-feh

%description
No detailed description available

%package dev
Summary: dev components for the xf86bigfontproto package.
Group: Development
Provides: xf86bigfontproto-devel

%description dev
dev components for the xf86bigfontproto package.


%prep
%setup -q -n xf86bigfontproto-1.2.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xf86bigfont.h
/usr/include/X11/extensions/xf86bigfproto.h
/usr/include/X11/extensions/xf86bigfstr.h
/usr/lib64/pkgconfig/xf86bigfontproto.pc
