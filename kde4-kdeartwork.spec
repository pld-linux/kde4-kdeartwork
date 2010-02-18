%define		_state		stable
%define		orgname		kdeartwork
%define		qtver		4.6.1

Summary:	K Desktop Environment - artwork
Summary(pl.UTF-8):	K Desktop Environment - grafiki itp.
Name:		kde4-kdeartwork
Version:	4.4.0
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	ee1a736960f47641cc65f7a1b3483445
Patch0:		%{name}-findxscreensaver.patch
Patch1:		%{name}-crystalsvg-hicolor.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ed
# for kscreensaver.h
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	libxml2-progs
BuildRequires:	phonon-devel >= 4.3.80
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	strigi-devel >= 0.7.0
BuildRequires:	xscreensaver-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various graphics and such for KDE.

%description -l es.UTF-8
kdeartwork possue temas, sonidos, wallpapers, e estilos adicionais a
KDE.

%description -l pl.UTF-8
Pakiet ten zawiera różne grafiki i tym podobne dla KDE.

%description -l pt_BR.UTF-8
kdeartwork contém temas, sons, papéis de parede e estilos de janelas
adicionais para o KDE.

%package -n kde4-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl.UTF-8):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace >= %{version}

%description -n kde4-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde4-decoration-icewm -l pl.UTF-8
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde4-ColorSchemes
Summary:	KDE ColorSchemes
Summary(pl.UTF-8):	Schematy kolorów dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace >= %{version}

%description -n kde4-ColorSchemes
KDE ColorSchemes.

%description -n kde4-ColorSchemes -l pl.UTF-8
Schematy kolorów dla KDE.

%package -n kde4-emoticons
Summary:	KDE emoticons themes
Summary(pl.UTF-8):	Motywy emotikon dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description -n kde4-emoticons
KDE emoticons themes.

%description -n kde4-emoticons -l pl.UTF-8
Motywy emotikon dla KDE.

%package -n kde4-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl.UTF-8):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements

%description -n kde4-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde4-icons-Locolor -l pl.UTF-8
Motyw ikon dla KDE - locolor.

%package -n kde4-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl.UTF-8):	Motyw ikon dla KDE - Technical
Group:		X11/Amusements

%description -n kde4-icons-Technical
KDE Icons Theme - Technical.

%description -n kde4-icons-Technical -l pl.UTF-8
Motyw ikon dla KDE - Technical.

%package -n kde4-icons-ikons
Summary:	KDE Icons Theme - ikons
Summary(pl.UTF-8):	Motyw ikon dla KDE - ikons
Group:		X11/Amusements

%description -n kde4-icons-ikons
KDE Icons Theme - ikons.

%description -n kde4-icons-ikons -l pl.UTF-8
Motyw ikon dla KDE - ikons.

%package -n kde4-icons-kdeclassic
Summary:	KDE Icons Theme - kdeclassic
Summary(pl.UTF-8):	Motyw ikon dla KDE - kdeclassic
Group:		X11/Amusements

%description -n kde4-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde4-icons-kdeclassic -l pl.UTF-8
Motyw ikon dla KDE - kdeclassic.

%package -n kde4-icons-kids
Summary:	KDE Icons Theme - kids
Summary(pl.UTF-8):	Motyw ikon dla KDE - kids
Group:		X11/Amusements

%description -n kde4-icons-kids
KDE Icons Theme - kids.

%description -n kde4-icons-kids -l pl.UTF-8
Motyw ikon dla KDE - kids.

%package -n kde4-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl.UTF-8):	Motyw ikon dla KDE - slick
Group:		X11/Amusements

%description -n kde4-icons-slick
KDE Icons Theme - slick.

%description -n kde4-icons-slick -l pl.UTF-8
Motyw ikon dla KDE - slick.

%package -n kde4-icons-crystalsvg
Summary:	KDE Icons Theme - crystalsvg
Summary(pl.UTF-8):	Motyw ikon dla KDE - crystalsvg
Group:		X11/Amusements
Requires:	hicolor-icon-theme

%description -n kde4-icons-crystalsvg
KDE Icons Theme - crystalsvg.

%description -n kde4-icons-crystalsvg -l pl.UTF-8
Motyw ikon dla KDE - crystalsvg.

%package -n kde4-icons-nuvola
Summary:	KDE Icons Theme - nuvola
Summary(pl.UTF-8):	Motyw ikon dla KDE - nuvola
Group:		X11/Amusements

%description -n kde4-icons-nuvola
KDE Icons Theme - nuvola.

%description -n kde4-icons-nuvola -l pl.UTF-8
Motyw ikon dla KDE - nuvola.

%package -n kde4-style-phase
Summary:	KDE Style - Phase
Summary(pl.UTF-8):	Styl dla KDE - Phase
Group:		X11/Amusements
Requires:	kde4-kdebase >= %{version}

%description -n kde4-style-phase
KDE Style - Phase.

%description -n kde4-style-phase -l pl.UTF-8
Styl dla KDE - Phase.

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl.UTF-8):	Motywy dla kworldclock
Group:		X11/Amusements
#Requires:	kde4-kdetoys-kworldclock >= %{version}

%description kworldclock
Themes for kworldclock.

%description kworldclock -l pl.UTF-8
Motywy dla kworldclock.

%package screensavers
Summary:	Screen savers for KDE
Summary(pl.UTF-8):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace-screensavers >= %{version}

%description screensavers
Screen savers for KDE.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl.UTF-8):	Dźwięki dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase >= %{version}

%description sounds
KDE Sounds.

%description sounds -l pl.UTF-8
Dźwięki dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl.UTF-8):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl.UTF-8
Tapety dla KDE.

%package -n kde4-desktopthemes
Summary:	KDE Desktop Themes
Summary(pl.UTF-8):	Motywy pulpitu dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace >= %{version}

%description -n kde4-desktopthemes
KDE Desktop Themes.

%description -n kde4-desktopthemes -l pl.UTF-8
Motywy pulpitu dla KDE.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p0
#%patch1 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -n kde4-decoration-icewm
#%defattr(644,root,root,755)
#%{_datadir}/apps/kwin/icewm-themes

%files -n kde4-ColorSchemes
%defattr(644,root,root,755)
%{_datadir}/apps/color-schemes/*.colors

%files -n kde4-emoticons
%defattr(644,root,root,755)
%{_datadir}/emoticons

#%files -n kde4-icons-Locolor
#%defattr(644,root,root,755)
#%{_iconsdir}/Locolor

#%files -n kde4-icons-ikons
#%defattr(644,root,root,755)
#%{_iconsdir}/ikons

#%files -n kde4-icons-kdeclassic
#%defattr(644,root,root,755)
#%{_iconsdir}/kdeclassic

#%files -n kde4-icons-kids
#%defattr(644,root,root,755)
#%{_iconsdir}/kids

#%files -n kde4-icons-slick
#%defattr(644,root,root,755)
#%{_iconsdir}/slick

#%files -n kde4-icons-crystalsvg
#%defattr(644,root,root,755)
#%{_iconsdir}/crystalsvg

%files -n kde4-icons-nuvola
%defattr(644,root,root,755)
%{_iconsdir}/nuvola

%files -n kde4-style-phase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kstyle_phase_config.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/phasestyle.so
%{_datadir}/apps/kstyle/themes/phase.themerc

#%files kworldclock
#%defattr(644,root,root,755)
#%dir %{_datadir}/apps/kworldclock
#%{_datadir}/apps/kworldclock/maps

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxsconfig
%attr(755,root,root) %{_bindir}/kxsrun
%attr(755,root,root) %{_bindir}/*.kss
%{_datadir}/kde4/services/ScreenSavers/*.desktop
%{_datadir}/apps/kfiresaver
%{_datadir}/apps/kscreensaver

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde4-desktopthemes
%defattr(644,root,root,755)
%{_datadir}/apps/desktoptheme/Aya
%{_datadir}/apps/desktoptheme/Clean-Blend
%{_datadir}/apps/desktoptheme/Elegance
%{_datadir}/apps/desktoptheme/Silicon
%{_datadir}/apps/desktoptheme/heron
%{_datadir}/apps/desktoptheme/slim-glow
