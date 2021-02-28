%define		_state		stable
%define		orgname		kdeartwork
%define		qtver		4.8.3
%define		kdeworkspacever	4.11.0

Summary:	K Desktop Environment - artwork
Summary(pl.UTF-8):	K Desktop Environment - grafiki itp.
Name:		kde4-kdeartwork
Version:	4.14.3
Release:	4
License:	LGPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	444c3fea54711a840bca705ea90c8cb2
Patch0:		%{name}-findxscreensaver.patch
Patch1:		%{name}-crystalsvg-hicolor.patch
Patch2:		cmake.patch
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
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdeworkspacever}
# rotating images
BuildRequires:	kde4-libkexiv2-devel >= %{version}
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	xscreensaver-base
BuildConflicts:	eigen3
Obsoletes:	kde4-kdeartwork-sounds < %{version}
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

%package -n kde4-ColorSchemes
Summary:	KDE ColorSchemes
Summary(pl.UTF-8):	Schematy kolorów dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
BuildArch:	noarch

%description -n kde4-ColorSchemes
KDE ColorSchemes.

%description -n kde4-ColorSchemes -l pl.UTF-8
Schematy kolorów dla KDE.

%package -n kde4-emoticons
Summary:	KDE emoticons themes
Summary(pl.UTF-8):	Motywy emotikon dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
BuildArch:	noarch

%description -n kde4-emoticons
KDE emoticons themes.

%description -n kde4-emoticons -l pl.UTF-8
Motywy emotikon dla KDE.

%package -n kde4-icons-nuvola
Summary:	KDE Icons Theme - nuvola
Summary(pl.UTF-8):	Motyw ikon dla KDE - nuvola
Group:		X11/Amusements
BuildArch:	noarch

%description -n kde4-icons-nuvola
KDE Icons Theme - nuvola.

%description -n kde4-icons-nuvola -l pl.UTF-8
Motyw ikon dla KDE - nuvola.

%package -n kde4-icons-mono
Summary:	KDE Icons Theme - mono
Summary(pl.UTF-8):	Motyw ikon dla KDE - mono
Group:		X11/Amusements
BuildArch:	noarch

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

%package screensavers
Summary:	Screen savers for KDE
Summary(pl.UTF-8):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace-screensavers >= %{kdeworkspacever}

%description screensavers
Screen savers for KDE.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl.UTF-8):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}
BuildArch:	noarch

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl.UTF-8
Tapety dla KDE.

%package -n kde4-desktopthemes
Summary:	KDE Desktop Themes
Summary(pl.UTF-8):	Motywy pulpitu dla KDE
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
BuildArch:	noarch

%description -n kde4-desktopthemes
KDE Desktop Themes.

%description -n kde4-desktopthemes -l pl.UTF-8
Motywy pulpitu dla KDE.

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
%patch2 -p1

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
