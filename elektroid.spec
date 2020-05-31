Name:		elektroid
Version:	1.2
Release:	1%{?dist}
Summary:	Sample transfer application for Elektron devices

License:	GPLv3
URL:		https://github.com/dagargo/elektroid
Source0:	https://github.com/dagargo/elektroid/archive/1.2.tar.gz

BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk3-devel
BuildRequires:	libsndfile-devel
BuildRequires:	gettext-devel
BuildRequires:	libsamplerate-devel
%if 0%{?suse_version}
BuildRequires:	libpulse-devel
%else
%if 0%{?mgaversion}
BuildRequires:	libpulseaudio-devel
%else
# RHEL, CentOS and Fedora use this name:
BuildRequires:	pulseaudio-libs-devel
%endif
%endif

%description
Elektroid is a GNU/Linux sample transfer application for Elektron devices.
It includes the elektroid GUI application and the elektroid-cli CLI application.
Elektroid has been reported to work with Model:Samples, Digitakt and
Analog Rytm mk1 and mk2.


%prep
%autosetup


%build
autoreconf --install
%configure
%make_build


%install
%make_install


%files
%{_bindir}/elektroid-cli
%{_bindir}/elektroid
%{_datadir}/applications/elektroid.desktop
%{_datadir}/elektroid/res/gui.css
%{_datadir}/elektroid/res/gui.glade
%{_datadir}/icons/hicolor/scalable/apps/elektroid.svg
%{_datadir}/locale/de/LC_MESSAGES/elektroid.mo
%{_datadir}/locale/en/LC_MESSAGES/elektroid.mo
%{_datadir}/locale/es/LC_MESSAGES/elektroid.mo
%{_datadir}/locale/fr/LC_MESSAGES/elektroid.mo
%{_mandir}/man1/elektroid-cli.1.gz
%{_mandir}/man1/elektroid.1.gz
%license COPYING


%changelog
* Sun May 31 2020 Jonathan Wakely <jwakely@fedoraproject.org> - 1.2-1
- Initial RPM package for Fedora
