%define ver      	0.9.6
%define rel      	9
%define buildroot	/var/tmp/imwheel-root
%define prefix 		/usr/X11R6

Summary: A utility to make wheel mice work under X
Name: imwheel
Version: %{ver}
Release: %{rel}
Copyright: GPL
Prefix: %{prefix}
Group: User Interface/X Hardware Support
Source: %{name}-%{ver}.tar.gz
Source1: wheel.pl.bz2
Source2: imwheelrc.bz2
Source3: imwheel
Patch0: imwheel-%{ver}-etc_X11.patch.bz2
Patch1: imwheel-focus-change.patch
BuildRoot: %{buildroot}
URL: http://solaris1.mysolution.com/~jcatki/imwheel/

%description 
Imwheel, helps enable the "wheel" found on many newer mice such as 
the Microsoft IntelliMouse, the Genius NetMouse, and several varieties
of mice from Logitech.


%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%setup -q
%patch0 -p1 
%patch1 -p1

%build
rm -f gpm-imwheel
CFLAGS=$RPM_OPT_FLAGS make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin $RPM_BUILD_ROOT%{prefix}/man/man1 $RPM_BUILD_ROOT%{prefix}/etc
# imwheel proper
/usr/bin/install -c -d -o root -g root -m 0755 $RPM_BUILD_ROOT%{prefix}/bin
/usr/bin/install -c -o root -g root -m 0755 imwheel $RPM_BUILD_ROOT%{prefix}/bin/imwheel

# the manpage
/usr/bin/install -c -d -o root -g root -m 0755 $RPM_BUILD_ROOT%{prefix}/man/man1
/usr/bin/install -c -o root -g root -m 0644 imwheel.1 $RPM_BUILD_ROOT%{prefix}/man/man1/imwheel.1x

# the default configuration
/usr/bin/install -c -d -o root -g root -m 0755 $RPM_BUILD_ROOT/etc/X11
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/etc/X11/imwheelrc

# the suid helper program
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{prefix}/bin/imwheel-solo

mkdir -p $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d
install -m 0755 %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /etc/X11
%config /etc/X11/imwheelrc
%attr(1755, root ,root) %{prefix}/bin/imwheel
%attr(4755, root, root) %{prefix}/bin/imwheel-solo
/etc/X11/xinit/xinitrc.d/imwheel
%{prefix}/man/*/*

%doc BUGS CHANGES COPYING README EMACS


%Changelog
* Mon Jan 31 2000 Tim Powers <timp@redhat.com>
- added /etc/X11/xinit/xinitrc.d/imwheel for 6.2
- don't bzip man pages, letting rpm and the build system handle it

* Fri Jan 14 2000 Tim Powers <timp@redhat.com>
- added defattr
- we don't own /usr/man/man1, so don't claim it. Using /usr/man/*/* instead.
- using patch sent in by Hans de Goede <hans@highrise.nl> to fix problems with
	focus
- added clean section

* Tue Sep 21 1999 Preston Brown <pbrown@redhat.com>
- adopted for powertools

* Mon Aug 09 1999 Peter Putzer <pputzer@linux-mandrake.com>
- fixed Vendor tag
- bzip2'ed wheel.pl & imwheelrc
- don't compile gpm-imwheel anymore, it's useless
- moved configuration file from /etc/imwheelrc to /etc/X11/imwheelrc

* Sun Aug 08 1999 Peter Putzer <pputzer@linux-mandrake.com>
- made relocatable

* Sat Aug 07 1999 Peter Putzer <pputzer@linux-mandrake.com>
- fixed some typos/mis-spellings in the spec-file
- removed the %post-install script, this can be done more
  easily by patching /etc/X11/xdm/Xsession!
- added adapted /etc/imwheelrc (to work with XEmacs and konsole)
- bzip2'ed the manpage
- moved manpage to /usr/X11R6/man/man1

* Thu Aug 05 1999 Peter Putzer <pputzer@linux-mandrake.com>
- rebuilt for Mandrake 6.0 (I'm the offical maintainer of this
  package now) 
- small fix in %post script (in case some line in Xsession is
  commented out)
- bzip2'ed the source

* Thu Jul 01 1999 Peter Putzer <putzer@kde.org>
- suidperl script for always managing pidfiles

* Sun May 02 1999 Peter Putzer <putzer@kde.org>
- fixed group fro Red Hat 6.0
- added RPM_OPT_FLAGS
- imwheel installed suid root
 
* Wed Apr 27 1999 Sean P. Kane <kane@ca.metsci.com>
- Fixed changelog so that this spec file works. 
- Therefore the entries below here may be a bit inaccurate.

* Sat Apr 10 1999 Nick Koston <bdraco@darkorb.net>
- Added the man page
- Added the support programs programs
- Packaged 0.9.6
- Removed gpm since it conflicts with the gpm package
- Changed path names to be more like redhat
