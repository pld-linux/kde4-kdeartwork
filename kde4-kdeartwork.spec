%define		_state		stable
%define		orgname		kdeartwork
%define		qtver		4.8.0

Summary:	K Desktop Environment - artwork
Summary(pl.UTF-8):	K Desktop Environment - grafiki itp.
Name:		kde4-kdeartwork
Version:	4.8.1
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	be817818f3e1971a31a8606e49f522a1
Patch0:		%{name}-findxscreensaver.patch
Patch1:		%{name}-crystalsvg-hicolor.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eigen >= 1:2.0.12-3
# for kscreensaver.h
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
# rotating images
BuildRequires:	kde4-libkexiv2-devel >= %{version}
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	strigi-devel >= 0.7.2
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

%package -n kde4-icons-mono
Summary:	KDE Icons Theme - mono
Summary(pl.UTF-8):	Motyw ikon dla KDE - mono
Group:		X11/Amusements

%description -n kde4-icons-mono
KDE Icons Theme - mono.

%description -n kde4-icons-mono -l pl.UTF-8
Motyw ikon dla KDE - mono.

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

%package -n kde4-decoration-aurorae-themes
Summary:	Aurorae window decoration themes
Summary(pl.UTF-8):	Motywy dekoracji okien dla aurorae
Group:		X11/Amusements
Requires:	kde4-decoration-aurorae >= %{version}

%description -n kde4-decoration-aurorae-themes
Several window decoration themes for aurorae.

%description -n kde4-decoration-aurorae-themes -l pl.UTF-8
Różne motywy dekoracji okien dla aurorae.

%package -n kde4-decoration-kde2
Summary:	KDE Window Decoration - kde2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - kde2
Group:		X11/Amusements

%description -n kde4-decoration-kde2
KDE Window Decoration - kde2.

%description -n kde4-decoration-kde2 -l pl.UTF-8
Dekoracja okna dla KDE - kde2.

%package -n kde4-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl.UTF-8):	Dekoracja okna dla KDE - keramik
Group:		X11/Amusements

%description -n kde4-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde4-decoration-keramik -l pl.UTF-8
Dekoracja okna dla KDE - keramik.

%package -n kde4-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl.UTF-8):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements

%description -n kde4-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde4-decoration-modernsys -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde4-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements

%description -n kde4-decoration-quartz
A window decoration with solid borders. The window caption consists of
a lighter area for the window title and a darker area for window
buttons. Between the two area there is a stylish transition.

%description -n kde4-decoration-quartz -l pl.UTF-8
Dekoracja okna z pełnymi krawędziami. Nagłówek okna składa się z
jasnego obszaru dla tytułu okna i ciemniejszego dla przycisków. Między
obszarami jest stylowy przejście.

%package -n kde4-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements

%description -n kde4-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde4-decoration-redmond -l pl.UTF-8
Dekoracja okna przypominająca tę z Windows 98.

%package -n kde4-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements

%description -n kde4-decoration-web
A completely flat window decoration with rounded corners and visible,
thin borders.

%description -n kde4-decoration-web -l pl.UTF-8
Zupełnie płaska dekoracja okna z zaokrąglonymi brzegami oraz
widocznymi, cienkimi krawędziami.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p0
#%patch1 -p0

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-ColorSchemes
%defattr(644,root,root,755)
%{_datadir}/apps/color-schemes/*.colors

%files -n kde4-emoticons
%defattr(644,root,root,755)
%{_datadir}/emoticons

%files -n kde4-icons-nuvola
%defattr(644,root,root,755)
%{_iconsdir}/nuvola

%files -n kde4-icons-mono
%defattr(644,root,root,755)
%{_iconsdir}/mono

%files -n kde4-style-phase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kstyle_phase_config.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/phasestyle.so
%{_datadir}/apps/kstyle/themes/phase.themerc

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
%{_datadir}/apps/desktoptheme/Androbit
%{_datadir}/apps/desktoptheme/Aya
%{_datadir}/apps/desktoptheme/Produkt
%{_datadir}/apps/desktoptheme/Tibanna
%{_datadir}/apps/desktoptheme/slim-glow

%files -n kde4-decoration-aurorae-themes
%defattr(644,root,root,755)
%dir %{_datadir}/apps/aurorae
%dir %{_datadir}/apps/aurorae/themes
%{_datadir}/apps/aurorae/themes/Air-Oxygen
%{_datadir}/apps/aurorae/themes/Oxygen

%files -n kde4-decoration-kde2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_kde2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_kde2_config.so
%{_datadir}/apps/kwin/kde2.desktop

%files -n kde4-decoration-keramik
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_keramik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_keramik_config.so
%{_datadir}/apps/kwin/keramik.desktop

%files -n kde4-decoration-modernsys
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_modernsys.so
%attr(755,root,root) %{_libdir}/kde4/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde4-decoration-quartz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_quartz.so
%attr(755,root,root) %{_libdir}/kde4/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde4-decoration-redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde4-decoration-web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop
