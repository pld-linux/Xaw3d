Summary:     X athena widgets in 3d
Summary(de): X-Athena-Widgets in 3D 
Summary(fr): Widgets X Athena en 3D
Summary(pl): Biblioteka X athena widgets (wersja 3D)
Summary(tr): 3D X Athena arayüz elemanlarý (widgets)
Name:        Xaw3d
Version:     1.5
Release:     2
Group:       X11/Libraries
Copyright:   MIT
Source:      ftp://ftp.x.org/contrib/widgets/Xaw3d/R6.3/%{name}-%{version}.tar.gz
Patch0:      Xaw3d-1.3-glibc.patch
URL:         ftp://ftp.x.org/contrib/widgets/Xaw3d/
Prereq:      fileutils
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

%description -l de
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set für X Windows,
das die Anwendung dreidimensional erscheinen läßt, ohne daß umfangreiche 
Änderungen am Quellcode notwendig sind.

%description -l fr
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT pour
X Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout,
de modification du code.

%description -l tr
Xaw3d, MIT Athena kitaplýðýna, uygulamalara herhangi bir kod deðiþikliði
yapýlmasýný gerektirmeden (ya da ufak deðiþiklikler yaparak), üç boyutlu
bir görüntü kazandýran bir geliþtirmedir.

%package devel
Summary:     Files for developing programs that use Xaw3d
Summary(de): Dateien zur Entwicklung von Programmen, die Xaw3d benutzen 
Summary(fr): Fichiers pour développer des programmes utilisant Xaw3d
Summary(tr): Xaw3d kitaplýðýný kullanan programlar geliþtirmek için gerekli dosyalar
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows that
adds a 3-dimensional look to the applications with minimal or no source code
changes. This package includes the header files developing programs that
take full advantage of Xaw3d's features.

%description -l de devel
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für X-Windows,
das einer Applikationen mit minimalen oder keinen Änderungen am Quellcode
einen 3D-Look verleiht. Das Paket enthält die Headerdateien zur Entwicklung
von Programmen, die die Vorteile von Xaw3d voll nutzen.

%description -l fr devel
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT pour X
Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout, de
modification du code. Ce paquetage contient les en-têtes pour développer des
programmes tirant plein avantage des caractéristiques de Xaw3d

%package static
Summary:     Xaw3d static library
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows that
adds a 3-dimensional look to the applications with minimal or no source code
changes. This package includes the static library for developing programs
that take full advantage of Xaw3d's features.

%description -l de static
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für X-Windows, 
das einer Applikationen mit minimalen oder keinen Änderungen am Quellcode
einen 3D-Look verleiht. Das Paket enthält die statischen Library zur
Entwicklung von Programmen, die die Vorteile von Xaw3d voll nutzen.

%prep
%setup -q -c
%patch0 -p1

%build
export PATH=/usr/X11R6/bin:$PATH
cd xc/lib/Xaw3d
xmkmf
mkdir X11; ln -s `pwd` X11/Xaw3d
make	CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	EXTRA_INCLUDES=-I.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11
cd xc/lib/Xaw3d
make install DESTDIR=$RPM_BUILD_ROOT
mv	$RPM_BUILD_ROOT/usr/X11R6/include/X11/Xaw3d \
	$RPM_BUILD_ROOT/usr/X11R6/include/Xaw3d
ln -s ../Xaw3d $RPM_BUILD_ROOT/usr/X11R6/include/X11/Xaw3d

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
/usr/X11R6/lib/lib*.so
/usr/X11R6/include/Xaw3d
/usr/X11R6/include/X11/Xaw3d

%files static
%attr(644, root, root) /usr/X11R6/lib/*.a

%changelog
* Mon Oct 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5-2]
- fixed compiling Xaw3d on system without installled Xaw3d-devel.

* Mon Aug 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
  [1.3-15]
- fixed the bad symlink
- BuildRoot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- don't lave an improper return code from %pre

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- take care of the old location of the Xaw3d includes in case that one exist
- updated Prereq: field

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com
- fixed the -devel package for the right include files path

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- minor spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- i18n widec.h patch needs to be applied on all systems

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- changed axp check to alpha

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc
