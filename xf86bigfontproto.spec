#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86bigfontproto
Version  : 1.2.0
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-1.2.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-1.2.0.tar.gz
Summary  : XF86BigFont extension headers
Group    : Development/Tools
License  : MIT-feh
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
No detailed description available

%package dev
Summary: dev components for the xf86bigfontproto package.
Group: Development
Provides: xf86bigfontproto-devel

%description dev
dev components for the xf86bigfontproto package.


%package dev32
Summary: dev32 components for the xf86bigfontproto package.
Group: Default
Requires: xf86bigfontproto-dev

%description dev32
dev32 components for the xf86bigfontproto package.


%prep
%setup -q -n xf86bigfontproto-1.2.0
pushd ..
cp -a xf86bigfontproto-1.2.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169909
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507169909
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xf86bigfont.h
/usr/include/X11/extensions/xf86bigfproto.h
/usr/include/X11/extensions/xf86bigfstr.h
/usr/lib64/pkgconfig/xf86bigfontproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xf86bigfontproto.pc
/usr/lib32/pkgconfig/xf86bigfontproto.pc
