Summary:	X athena widgets in 3D
Summary(de):	X-Athena-Widgets in 3D 
Summary(fr):	Widgets X Athena en 3D
Summary(pl):	Biblioteka X athena widgets (wersja 3D)
Summary(tr):	3D X Athena arayüz elemanlarý (widgets)
Name:		Xaw3d
Version:	1.5
Release:	9
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	MIT
Source0:	ftp://ftp.x.org/contrib/widgets/Xaw3d/R6.3/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-shlib.patch
Patch2:		%{name}.patch
Patch3:		%{name}-static.patch
Patch4:		%{name}-ia64.patch
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Windows that adds a 3-dimensional look to the applications with
minimal or no source code changes.

%description -l de
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set für X
Windows, das die Anwendung dreidimensional erscheinen läßt, ohne daß
umfangreiche Änderungen am Quellcode notwendig sind.

%description -l fr
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code.

%description -l pl
Xaw3d jest ulepszon± wersj± biblioteki X Athena Widget, która dodaje
trójwymiarowy wygl±d aplikacjom przy minimalnych (lub ¿adnych)
zmianach kodu ¼ród³owego.

%description -l tr
Xaw3d, MIT Athena kitaplýðýna, uygulamalara herhangi bir kod
deðiþikliði yapýlmasýný gerektirmeden (ya da ufak deðiþiklikler
yaparak), üç boyutlu bir görüntü kazandýran bir geliþtirmedir.

%package devel
Summary:	Files for developing programs that use Xaw3d
Summary(de):	Dateien zur Entwicklung von Programmen, die Xaw3d benutzen 
Summary(fr):	Fichiers pour développer des programmes utilisant Xaw3d
Summary(pl):	Pliki potrzebne przy kompilacji programów u¿ywaj±cych Xaw3d
Summary(tr):	Xaw3d kitaplýðýný kullanan programlar geliþtirmek için gerekli dosyalar
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Windows that adds a 3-dimensional look to the applications with
minimal or no source code changes.

This package includes the header files developing programs that take
full advantage of Xaw3d's features.

%description -l de devel
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für
X-Windows, das einer Applikationen mit minimalen oder keinen
Änderungen am Quellcode einen 3D-Look verleiht. Das Paket enthält die
Headerdateien zur Entwicklung von Programmen, die die Vorteile von
Xaw3d voll nutzen.

%description -l fr devel
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code. Ce paquetage contient les
en-têtes pour développer des programmes tirant plein avantage des
caractéristiques de Xaw3d.

%description -l pl devel
Xaw3d jest ulepszon± wersj± biblioteki X Athena Widget, która dodaje
trójwymiarowy wygl±d aplikacjom przy minimalnych (lub ¿adnych)
zmianach kodu ¼ród³owego.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
wykorzystuj±cych Xaw3d.

%package static
Summary:	Xaw3d static library
Summary(pl):	Biblioteki statyczne Xaw3d
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Windows that adds a 3-dimensional look to the applications with
minimal or no source code changes.

This package includes the static library for developing programs that
take full advantage of Xaw3d's features.

%description -l de static
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für
X-Windows, das einer Applikationen mit minimalen oder keinen
Änderungen am Quellcode einen 3D-Look verleiht. Das Paket enthält die
statischen Library zur Entwicklung von Programmen, die die Vorteile
von Xaw3d voll nutzen.

%description -l pl static
Xaw3d jest ulepszon± wersj± biblioteki X Athena Widget, która dodaje
trójwymiarowy wygl±d aplikacjom przy minimalnych (lub ¿adnych)
zmianach kodu ¼ród³owego.

Ten pakiet zawiera biblioteki statyczne dla Xaw3d.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export PATH=%{_bindir}:$PATH
cd xc/lib/Xaw3d
xmkmf
mkdir X11; ln -s `pwd` X11/Xaw3d
make	CDEBUGFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
	CXXDEBUGFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
	EXTRA_INCLUDES=-I.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/X11

cd xc/lib/Xaw3d
%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f    $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d \
      $RPM_BUILD_ROOT%{_includedir}/Xaw3d
ln -s ../Xaw3d $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- Xaw3d-devel < 1.5-5
if [ -d /usr/X11R6/include/Xaw3d ]; then
	rm -rf /usr/X11R6/include/Xaw3d
	ln -sf X11/Xaw3d /usr/X11R6/include
fi                                                                                                            

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/Xaw3d
%{_includedir}/X11/Xaw3d

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
