# TODO:
# - SECURITY: http://securitytracker.com/alerts/2004/Aug/1011049.html
Summary:	An utility to make wheel mice work under X
Summary(pl.UTF-8):	Narzędzie pozwalające wykorzystać rolki myszy w X
Name:		imwheel
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/imwheel/%{name}-%{version}pre12.tar.gz
# Source0-md5:	21d81db739ae95d96f9b650f7b826a14
Source1:	%{name}-xinitrc
Patch0:		%{name}-Makefile.patch
URL:		http://imwheel.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/X11

%description
Imwheel helps enable the "wheel" found on many newer mice such as the
Microsoft IntelliMouse, the Genius NetMouse, several varieties of mice
from Logitech and other.

It does it by emulating key sequences, which are configurable on
per-program basis.

%description -l pl.UTF-8
Imwheel pomaga wykorzystać "kółka" dostępne w wielu nowych myszkach,
takich jak Microsoft IntelliMouse, Genius NetMouse, myszkach Logitecha
oraz innych.

Imwheel pozwala powiązać sekwencje klawiszy z obrotami kółek myszy,
przy czym dla każdego programu mogą one być inne.

%prep
%setup -q -n %{name}-%{version}pre12
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x \
	--disable-gpm \
	--enable-mdetect \
	--enable-mdump \
	--enable-extras 
#	--with-pid-dir=dir

%{__make} \
	DESTDIR="$RPM_BUILD_ROOT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xinit/xinitrc.d

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xinit/xinitrc.d/%{name}
install imwheelrc $RPM_BUILD_ROOT%{_sysconfdir}/imwheelrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README EMACS NEWS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imwheelrc
%attr(755,root,root) %{_sysconfdir}/xinit/xinitrc.d/imwheel
%attr(755,root,root) %{_bindir}/imwheel
%{_mandir}/man?/imwheel*
