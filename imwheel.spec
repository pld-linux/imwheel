Summary:	An utility to make wheel mice work under X
Summary(pl):	Narzêdzie pozwalaj±ce wykorzystaæ rolki myszy w X
Name:		imwheel
Version:	0.9.9pre3
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	http://jonatkins.org/imwheel/files/%{name}-%{version}.tar.gz
Source1:	imwheelrc
#Source2:	wheel.pl.bz2
Patch0:		%{name}-etc_X11.patch.bz2
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-WinAction-SIGSEGV.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://solaris1.mysolution.com/~jcatki/imwheel/

%define         _prefix         /usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11

%description 
Imwheel helps enable the "wheel" found on many newer mice such as the
Microsoft IntelliMouse, the Genius NetMouse, several varieties of
mice from Logitech and other.

It does it by emulating key sequences, which are configurable on
per-program basis.

%description -l pl
Imwheel pomaga wykorzystaæ "kó³ka" dostêpne w wielu nowych myszkach, takich
jak Microsoft IntelliMousem, Genius NetMouse, myszkach Logitecha oraz innych.

Imwheel pozwala powi±zaæ sekwencje klawiszy z obrotami kó³ek myszy, przy czym
dla ka¿dego programy mog± one byæ inne.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1

%build
%configure \
	--with-x \
	--disable-gpm

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/Xsession.d

gzip -9nf AUTHORS BUGS ChangeLog README EMACS NEWS TODO \
    $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,README,EMACS,NEWS,TODO}.gz
%config %{_sysconfdir}/imwheelrc
#%attr(755,root,root) %{_sysconfdir}/Xsession.d/imwheel
%attr(1755,root,root) %{_bindir}/imwheel
%{_mandir}/man1/imwheel*
