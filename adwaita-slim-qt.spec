Name:           adwaita-slim-qt
Version:        1.0.1
Release:        5%{?dist}
License:        LGPLv2+
Summary:        Adwaita-Slim theme for Qt-based applications

Url:            https://github.com/polter-rnd/adwaita-slim-qt
Source0:        https://github.com/polter-rnd/adwaita-slim-qt/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

Requires:       adwaita-slim-qt4

%description
Theme to let Qt applications fit nicely into Fedora Workstation


%package -n adwaita-slim-qt4
Summary:        Adwaita-Slim Qt4 theme
Requires:       qt4

%description -n adwaita-slim-qt4
Adwaita-Slim theme variant for applications utilizing Qt4


%package -n adwaita-slim-qt5
Summary:        Adwaita-Slim Qt5 theme
Requires:       qt5-qtbase


%description -n adwaita-slim-qt5
Adwaita-Slim theme variant for applications utilizing Qt5


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


%files -n adwaita-slim-qt4
%doc LICENSE.LGPL2 README.md
%{_qt4_plugindir}/styles/adwaita-slim.so

%files -n adwaita-slim-qt5
%doc LICENSE.LGPL2 README.md
%{_qt5_plugindir}/styles/adwaita-slim.so

%files

%changelog
* Fri Nov 30 2018 Paul Artsishevsky <polter.rnd@gmail.com> - 1.0-5
- Fork was renamed to Adwaita-Slim
- Merged with upstream

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Martin Bříza <mbriza@redhat.com> - 1.0-1
- Update to 1.0 * Mon Feb 27 2017 Martin Briza <mbriza@redhat.com> - 0.98-1
- Update to 0.98 - Fixes #1410597

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.97-2
- drop hardcoded Requires: qt4/qt5-qtbase

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
