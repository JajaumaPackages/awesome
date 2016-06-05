%global commit 7830cf0
%global vermagic 3.5.2
%global gitdescribe %{vermagic}-1808-g%{commit}
%global snapshot .git20160605.%{commit}

Name:           awesome
Version:        %{vermagic}
Release:        10%{snapshot}%{?dist}
Summary:        Highly configurable, framework window manager for X

License:        GPLv2+ and BSD
URL:            http://awesome.naquadah.org

# git clone https://github.com/awesomeWM/awesome
# cd awesome
# make dist
Source0:        awesome-%{gitdescribe}.tar.bz2
Source1:        awesome.desktop
Source2:        awesome-noargb.desktop
Patch0:         awesome-ci-tests-force-using-theme-hack.patch

BuildRequires:  cmake >= 3.0.0
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  lua-devel
BuildRequires:  lua-ldoc
BuildRequires:  lua-lgi
BuildRequires:  cairo-gobject
BuildRequires:  luacheck
BuildRequires:  busted
# needed by the CI tests ('make check')
BuildRequires:  xorg-x11-utils
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-server-utils
BuildRequires:  dbus-x11
BuildRequires:  xterm
BuildRequires:  gtk3

BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util) >= 0.3.8
BuildRequires:  pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:  pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:  pkgconfig(xproto) >= 7.0.15
BuildRequires:  pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires:  pkgconfig(dbus-1)

Requires:       lua-lgi
Requires:       cairo-gobject
Requires:       xterm
Requires:       rlwrap
Requires:       nano

Provides:       desktop-notification-daemon

%description
awesome is a highly configurable, next generation framework window manager for
X. It is very fast, extensible and licensed under the GNU GPLv2 license.

It is primarly targeted at power users, developers and any people dealing with
every day computing tasks and who want to have fine-grained control on theirs
graphical environment.


%package session
Summary:        AwesomeWM default session
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description session
This package contains default AwesomeWM session startup files for using with
display managers.


%package doc
Summary:        AwesomeWM API documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package contains the AwesomeWM API documentation in HTML format.


%prep
%setup -q -n awesome-%{gitdescribe}
%patch0 -p1


%build
mkdir build
pushd build
%cmake -DSYSCONFDIR=%{_sysconfdir} ..
make VERBOSE=1 %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/xsessions/ \
    %{SOURCE1} %{SOURCE2}
desktop-file-validate %{buildroot}%{_datadir}/xsessions/*.desktop


%check
export CI=true
make -C build check


%files
%dir %{_sysconfdir}/xdg/%{name}
%config %{_sysconfdir}/xdg/%{name}/rc.lua
%{_bindir}/awesome
%{_bindir}/awesome-client
%{_datadir}/awesome/
%{_mandir}/man?/*
%{_mandir}/*/man1/*
%{_mandir}/*/man5/*

%files session
%{_datadir}/xsessions/*.desktop

%files doc
%{_defaultdocdir}/awesome/


%changelog
* Sun Jun 05 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-10.git20160605.7830cf0
- Update source to 7830cf0

* Sat Jun 04 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-9.git20160604.4e35d1f
- Update source to 4e35d1f

* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-8.git20160519.e8da309
- Update source to e8da309
- Run all of the available tests

* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-7.git20160519.f228257
- Update source to f228257

* Tue May 17 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-6.git20160517.32eeaa9
- Update source to 32eeaa9

* Mon May 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-5.git20160516.cc8e10e
- Update source to cc8e10e

* Fri May 13 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-4.git20160513.63dad3f
- Update source to 63dad3f
- Add the check step which just calls 'make luacheck' for now

* Sun May 08 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-3.git20160508.58209cd
- Update source to 58209cd

* Sun May 01 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-2.git20160501.6b6cbf4
- Update source to 6b6cbf4

* Sat Apr 30 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.5.2-1.git20160430.a1e340d
- Public release
