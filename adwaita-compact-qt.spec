Name:           adwaita-compact-qt
Version:        0.97
Release:        1%{?dist}
License:        LGPLv2+
Summary:        Adwaita Compact theme for Qt-based applications

Url:            https://github.com/polter-rnd/adwaita-compact-qt
Source0:        https://github.com/polter-rnd/adwaita-compact-qt/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

Requires:       adwaita-compact-qt4

%description
Theme to let Qt applications fit nicely into Fedora Workstation


%package -n adwaita-compact-qt4
Summary:        Adwaita Compact Qt4 theme
Requires:       qt4

%description -n adwaita-compact-qt4
Adwaita Compact theme variant for applications utilizing Qt4


%package -n adwaita-compact-qt5
Summary:        Adwaita Compact Qt5 theme
Requires:       qt5-qtbase


%description -n adwaita-compact-qt5
Adwaita Compact theme variant for applications utilizing Qt5


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p "%{_target_platform}-qt4"
pushd "%{_target_platform}-qt4"
%{cmake} -DUSE_QT4=true ..
popd

mkdir -p "%{_target_platform}-qt5"
pushd "%{_target_platform}-qt5"
%{cmake} ..
popd

make %{?_smp_mflags} -C "%{_target_platform}-qt4"
make %{?_smp_mflags} -C "%{_target_platform}-qt5"


%install
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt4"
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt5"


%files -n adwaita-compact-qt4
%doc LICENSE.LGPL2 README.md
%{_qt4_plugindir}/styles/adwaita-compact.so

%files -n adwaita-compact-qt5
%doc LICENSE.LGPL2 README.md
%{_qt5_plugindir}/styles/adwaita-compact.so

%files

%changelog
* Mon Jan 2 2017 Paul Artsishevsky <polter.rnd@gmail.com> - 0.97-1
- Adwaita Compact fork

* Wed Dec 14 2016 Martin Briza <mbriza@redhat.com> - 0.97-1
- Update to 0.97

* Tue Dec 13 2016 Martin Briza <mbriza@redhat.com> - 0.95-1
- Update to 0.95

* Thu Jun 30 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-3
- Properly fix missing menubar in QtCreator

* Wed Jun 22 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-2
- Attempt to fix missing menubar issue in QtCreator

* Thu Apr 21 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-1
- Update to version 0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Martin Briza <mbriza@redhat.com> - 0.3-1
- Updated to the latest release
- Added a Qt5 build

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20141216git024b00bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.6.20141216git024b00bf
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Martin Briza <mbriza@redhat.com> - 0-0.5
- Package review cleanup
- Split into a base and a subpackage
- Fedora import

* Tue Dec 16 2014 Martin Briza <mbriza@redhat.com> - 0-0.4.copr
- Update to latest commit

* Fri Dec 05 2014 Martin Briza <mbriza@redhat.com> - 0-0.3.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.2.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.1.copr
- Initial build
