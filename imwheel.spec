Summary:	An utility to make wheel mice work under X
Summary(pl):	Narzêdzie pozwalaj±ce wykorzystaæ rolki myszy w X
Name:		imwheel
Version:	0.9.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://jonatkins.org/imwheel/files/%{name}-%{version}.tar.gz
# Source0-md5:	1010dadb54a38a20f7fec430e6e5d262
Source1:	%{name}-xinitrc
Patch0:		%{name}-etc_X11.patch.bz2
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-%{name}rc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://solaris1.mysolution.com/~jcatki/imwheel/

%define         _sysconfdir     /etc/X11

%description
Imwheel helps enable the "wheel" found on many newer mice such as the
Microsoft IntelliMouse, the Genius NetMouse, several varieties of mice
from Logitech and other.

It does it by emulating key sequences, which are configurable on
per-program basis.

%description -l pl
Imwheel pomaga wykorzystaæ "kó³ka" dostêpne w wielu nowych myszkach,
takich jak Microsoft IntelliMouse, Genius NetMouse, myszkach Logitecha
oraz innych.

Imwheel pozwala powi±zaæ sekwencje klawiszy z obrotami kó³ek myszy,
przy czym dla ka¿dego programy mog± one byæ inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x \
	--disable-gpm

%{__make} \
	DESTDIR="$RPM_BUILD_ROOT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xinit/xinitrc.d

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xinit/xinitrc.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README EMACS NEWS TODO
%config %{_sysconfdir}/imwheelrc
%attr(755,root,root) %{_sysconfdir}/xinit/xinitrc.d/imwheel
%attr(755,root,root) %{_bindir}/imwheel
%{_mandir}/man?/imwheel*
