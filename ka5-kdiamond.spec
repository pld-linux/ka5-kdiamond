%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kdiamond
Summary:	kdiamond
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e92089339179355ca026d75791658de7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-knotifications-devel >= 5.30.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDiamond is a single player puzzle game. The object of the game is to
build lines of three similar diamonds.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kdiamond.knsrc
%attr(755,root,root) %{_bindir}/kdiamond
%{_desktopdir}/org.kde.kdiamond.desktop
%{_iconsdir}/hicolor/128x128/apps/kdiamond.png
%{_iconsdir}/hicolor/16x16/apps/kdiamond.png
%{_iconsdir}/hicolor/22x22/apps/kdiamond.png
%{_iconsdir}/hicolor/32x32/apps/kdiamond.png
%{_iconsdir}/hicolor/48x48/apps/kdiamond.png
%{_iconsdir}/hicolor/64x64/apps/kdiamond.png
%{_datadir}/kdiamond
%{_datadir}/knotifications5/kdiamond.notifyrc
%{_datadir}/kxmlgui5/kdiamond
%{_datadir}/sounds/KDiamond-Stone-Drop.ogg
%{_datadir}/sounds/KDiamond-Stone-Swap.ogg
%{_datadir}/sounds/KDiamond-Stone-Touch.ogg
%{_datadir}/metainfo/org.kde.kdiamond.appdata.xml
