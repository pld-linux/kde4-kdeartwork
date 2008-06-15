%define		_state		unstable
%define		orgname		kdeartwork
Summary:	K Desktop Environment - artwork
Summary(es.UTF-8):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko.UTF-8):	KDE용
Summary(pl.UTF-8):	K Desktop Environment - grafiki itp.
Summary(pt_BR.UTF-8):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeartwork
Version:	4.0.82
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	d1d15673f1314d9258074ede27c9e8ec
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	ed
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	libxml2-progs
BuildRequires:	sed >= 4.0
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

%package -n kde-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl.UTF-8):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-desktop >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm -l pl.UTF-8
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-ColorSchemes
Summary:	KDE ColorSchemes
Summary(pl.UTF-8):	Schematy kolorów dla kde
Group:		X11/Amusements
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-ColorSchemes
KDE ColorSchemes.

%description -n kde-ColorSchemes -l pl.UTF-8
Schematy kolorów dla kde.


%package -n kde-emoticons
Summary:	KDE emoticons themes
Summary(pl.UTF-8):	Motywy emotikon dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-icons-locolor
Obsoletes:	kdeartwork-locolor
Obsoletes:	kdeartwork-themes

%description -n kde-emoticons
KDE emoticons themes.

%description -n kde-emoticons -l pl.UTF-8
Motywy emotikon dla KDE.

%package -n kde-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl.UTF-8):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-icons-locolor
Obsoletes:	kdeartwork-locolor
Obsoletes:	kdeartwork-themes

%description -n kde-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde-icons-Locolor -l pl.UTF-8
Motyw ikon dla KDE - locolor.

%package -n kde-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl.UTF-8):	Motyw ikon dla KDE - Technical
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-Technical
KDE Icons Theme - Technical.

%description -n kde-icons-Technical -l pl.UTF-8
Motyw ikon dla KDE - Technical.

%package -n kde-icons-ikons
Summary:	KDE Icons Theme - ikons
Summary(pl.UTF-8):	Motyw ikon dla KDE - ikons
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-ikons
KDE Icons Theme - ikons.

%description -n kde-icons-ikons -l pl.UTF-8
Motyw ikon dla KDE - ikons.

%package -n kde-icons-kdeclassic
Summary:	KDE Icons Theme - kdeclassic
Summary(pl.UTF-8):	Motyw ikon dla KDE - kdeclassic
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl.UTF-8
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-kids
Summary:	KDE Icons Theme - kids
Summary(pl.UTF-8):	Motyw ikon dla KDE - kids
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description -n kde-icons-kids
KDE Icons Theme - kids.

%description -n kde-icons-kids -l pl.UTF-8
Motyw ikon dla KDE - kids.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl.UTF-8):	Motyw ikon dla KDE - slick
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-slick
KDE Icons Theme - slick.

%description -n kde-icons-slick -l pl.UTF-8
Motyw ikon dla KDE - slick.

%package -n kde-icons-crystalsvg
Summary:	KDE Icons Theme - crystalsvg
Summary(pl.UTF-8):	Motyw ikon dla KDE - crystalsvg
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-crystalsvg
KDE Icons Theme - crystalsvg.

%description -n kde-icons-crystalsvg -l pl.UTF-8
Motyw ikon dla KDE - crystalsvg.

%package -n kde-style-phase
Summary:	KDE Style - Phase
Summary(pl.UTF-8):	Styl dla KDE - Phase
Group:		X11/Amusements
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-style-phase
KDE Style - Phase.

%description -n kde-style-phase -l pl.UTF-8
Styl dla KDE - Phase.

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl.UTF-8):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes-kworldclock

%description kworldclock
Themes for kworldclock.

%description kworldclock -l pl.UTF-8
Motywy dla kworldclock.

%package screensavers
Summary:	Screen savers for KDE
Summary(pl.UTF-8):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace-screensavers >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description screensavers
Screen savers for KDE.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl.UTF-8):	Dźwięki dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description sounds
KDE Sounds.

%description sounds -l pl.UTF-8
Dźwięki dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl.UTF-8):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl.UTF-8
Tapety dla KDE.

%prep
%setup -q

%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-icewm
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes

%files -n kde-ColorSchemes
%defattr(644,root,root,755)
%{_datadir}/apps/color-schemes/*.colors

%files -n kde-emoticons
%defattr(644,root,root,755)
%{_datadir}/emoticons

%files -n kde-icons-Locolor
%defattr(644,root,root,755)
%{_iconsdir}/Locolor

%files -n kde-icons-ikons
%defattr(644,root,root,755)
%{_iconsdir}/ikons

%files -n kde-icons-kdeclassic
%defattr(644,root,root,755)
%{_iconsdir}/kdeclassic

%files -n kde-icons-kids
%defattr(644,root,root,755)
%{_iconsdir}/kids

%files -n kde-icons-slick
%defattr(644,root,root,755)
%{_iconsdir}/slick

%files -n kde-icons-crystalsvg
%defattr(644,root,root,755)
%{_iconsdir}/crystalsvg

%files -n kde-style-phase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kstyle_phase_config.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/phasestyle.so
%{_datadir}/apps/kstyle/themes/phase.themerc

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps

%files screensavers
%defattr(644,root,root,755)
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
