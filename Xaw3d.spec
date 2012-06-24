Summary:	X athena widgets in 3d
Summary(de):	X-Athena-Widgets in 3D 
Summary(fr):	Widgets X Athena en 3D
Summary(pl):	Biblioteka X athena widgets (wersja 3D)
Summary(tr):	3D X Athena aray�z elemanlar� (widgets)
Name:		Xaw3d
Version:	1.5
Release:	4
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	MIT
Source:		ftp://ftp.x.org/contrib/widgets/Xaw3d/R6.3/%{name}-%{version}.tar.gz
Patch:		Xaw3d-glibc.patch
Prereq:		fileutils
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

%description -l de
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set f�r X Windows,
das die Anwendung dreidimensional erscheinen l��t, ohne da� umfangreiche 
�nderungen am Quellcode notwendig sind.

%description -l fr
Xaw3d est une version am�lior�e de l'ensemble Athena Widget du MIT pour
X Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout,
de modification du code.

%description -l pl
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych) zmianach
kodu �r�d�owego.

%description -l tr
Xaw3d, MIT Athena kitapl���na, uygulamalara herhangi bir kod de�i�ikli�i
yap�lmas�n� gerektirmeden (ya da ufak de�i�iklikler yaparak), �� boyutlu
bir g�r�nt� kazand�ran bir geli�tirmedir.

%package devel
Summary:	Files for developing programs that use Xaw3d
Summary(de):	Dateien zur Entwicklung von Programmen, die Xaw3d benutzen 
Summary(fr):	Fichiers pour d�velopper des programmes utilisant Xaw3d
Summary(pl):	Pliki potrzebne przy kompilacji program�w u�ywaj�cych Xaw3d
Summary(tr):	Xaw3d kitapl���n� kullanan programlar geli�tirmek i�in gerekli dosyalar
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

This package includes the header files developing programs that take full
advantage of Xaw3d's features.

%description -l de devel
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets f�r X-Windows,
das einer Applikationen mit minimalen oder keinen �nderungen am Quellcode
einen 3D-Look verleiht. Das Paket enth�lt die Headerdateien zur Entwicklung
von Programmen, die die Vorteile von Xaw3d voll nutzen.

%description -l fr devel
Xaw3d est une version am�lior�e de l'ensemble Athena Widget du MIT pour X
Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout,
de modification du code. Ce paquetage contient les en-t�tes pour
d�velopper des programmes tirant plein avantage des caract�ristiques de
Xaw3d.

%description -l pl devel
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych) zmianach
kodu �r�d�owego.

Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilacji program�w
wykorzystuj�cych Xaw3d.

%package static
Summary:	Xaw3d static library
Summary(pl):	Biblioteki statyczne Xaw3d
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

This package includes the static library for developing programs that take
full advantage of Xaw3d's features.

%description -l de static
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets f�r X-Windows, 
das einer Applikationen mit minimalen oder keinen �nderungen am Quellcode
einen 3D-Look verleiht. Das Paket enth�lt die statischen Library zur
Entwicklung von Programmen, die die Vorteile von Xaw3d voll nutzen.

%description -l pl static
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych) zmianach
kodu �r�d�owego.

Ten pakiet zawiera biblioteki statyczne dla Xaw3d.

%prep
%setup -q -c
%patch -p1

%build
export PATH=/usr/X11R6/bin:$PATH
cd xc/lib/Xaw3d
xmkmf
mkdir X11; ln -s `pwd` X11/Xaw3d
make	CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="-s" \
	EXTRA_INCLUDES=-I.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/X11

cd xc/lib/Xaw3d
make install DESTDIR=$RPM_BUILD_ROOT

mv    $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d \
      $RPM_BUILD_ROOT%{_includedir}/Xaw3d
ln -s ../Xaw3d $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/Xaw3d
%{_includedir}/X11/Xaw3d

%files static
%attr(644,root,root) %{_libdir}/lib*.a
