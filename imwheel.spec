Summary:	A utility to make wheel mice work under X
Name:		imwheel
Version:	0.9.6
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Source1:	wheel.pl.bz2
Source2:	imwheelrc.bz2
Source3:	imwheel
Patch0:		%{name}-%{version}-etc_X11.patch.bz2
Patch1:		%{name}-focus-change.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://solaris1.mysolution.com/~jcatki/imwheel/

%define         _prefix         /usr/X11R6
%define         _sysconfdir     /etc/X11

%description 
Imwheel, helps enable the "wheel" found on many newer mice such as the
Microsoft IntelliMouse, the Genius NetMouse, and several varieties of
mice from Logitech.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1

%build
rm -f gpm-imwheel
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/Xsession.d}

install imwheel		$RPM_BUILD_ROOT%{_bindir}/imwheel
install imwheel.1	$RPM_BUILD_ROOT%{_mandir}/man1/imwheel.1x

bzcat %{SOURCE2} > 	$RPM_BUILD_ROOT%{_sysconfdir}/imwheelrc
bzcat %{SOURCE1} > 	$RPM_BUILD_ROOT%{_bindir}/imwheel-solo
install %{SOURCE3} 	$RPM_BUILD_ROOT%{_sysconfdir}/Xsession.d

gzip -9nf BUGS CHANGES COPYING README EMACS \
    $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,COPYING,README,EMACS}.gz
%config %{_sysconfdir}/imwheelrc
%attr(755,root,root) %{_sysconfdir}/Xsession.d/imwheel
%attr(1755,root,root) %{_bindir}/imwheel
%attr(4755,root,root) %{_bindir}/imwheel-solo
%{_mandir}/*/*
