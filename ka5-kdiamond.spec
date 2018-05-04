%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		kdiamond
Summary:	kdiamond
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5ebdc3e8c67ecaa96e45c4ef8697e293
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kdiamond.

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
