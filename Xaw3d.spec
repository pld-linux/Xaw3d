Summary:	A version of the MIT Athena widget set for X
Summary(de):	3D-Version des MIT Athena-Widgetsatzes fuer X
Summary(es):	Widgets X athena en 3D
Summary(fr):	Widgets X Athena en 3D
Summary(pl):	Biblioteka X athena widgets (wersja 3D)
Summary(pt_BR):	Widgets X athena em 3d
Summary(ru):	Версия MIT Athena widget set для X
Summary(tr):	3D X Athena arayЭz elemanlarЩ (widgets)
Summary(uk):	Верс╕я MIT Athena widget set для X
Name:		Xaw3d
Version:	1.5E
Release:	4
License:	MIT
Group:		X11/Libraries
Source0:	ftp://ftp.visi.com/users/hawkeyd/X/%{name}-%{version}.tar.gz
# Source0-md5:	29ecfdcd6bcf47f62ecfd672d31269a1
Patch0:		%{name}-glibc.patch
Patch1:		%{name}.patch
Patch2:		%{name}-static.patch
Patch3:		%{name}-ia64.patch
Patch4:		%{name}-i18n.patch
Patch5:		%{name}-arrowscroll.patch
URL:		http://www.visi.com/~hawkeyd/xaw3d.html
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xorg-lib-libXmu
BuildRequires:	xorg-lib-libXpm
BuildRequires:	xorg-util-imake
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libXaw3d7

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Window that adds a 3-dimensional look to the applications with
minimal or no source code changes.

%description -l de
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set fЭr X
Window, das die Anwendung dreidimensional erscheinen lДъt, ohne daъ
umfangreiche дnderungen am Quellcode notwendig sind.

%description -l es
Xaw3d es una versiСn incrementada del conjunto MIT Athena Widget para
X Window que adiciona una apariencia tridimensional a las aplicaciones
con cambios mМnimos, o ninguno, en los cСdigos fuente.

%description -l fr
Xaw3d est une version amИliorИe de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code.

%description -l pl
Xaw3d jest ulepszon╠ wersj╠ biblioteki X Athena Widget, ktСra dodaje
trСjwymiarowy wygl╠d aplikacjom przy minimalnych (lub ©adnych)
zmianach kodu ╪rСdЁowego.

%description -l pt_BR
Xaw3d И uma versЦo incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma aparЙncia tri-dimensional Юs aplicaГУes com
mudanГas mМnimas ou nenhuma nos cСdigos fonte.

%description -l ru
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений).

%description -l tr
Xaw3d, MIT Athena kitaplЩПЩna, uygulamalara herhangi bir kod
deПiЧikliПi yapЩlmasЩnЩ gerektirmeden (ya da ufak deПiЧiklikler
yaparak), ЭГ boyutlu bir gЖrЭntЭ kazandЩran bir geliЧtirmedir.

%description -l uk
Xaw3d - це покращена верс╕я набору екранних прим╕тив╕в MIT Athena
Widget для X Window, яка нада╓ програмам "трьохвим╕рного" вигляду з
м╕н╕мальними зм╕нами вих╕дного коду (у б╕льшост╕ випадк╕в без зм╕н).

%package devel
Summary:	Files for developing programs that use Xaw3d
Summary(de):	Header und statische Libraries fuer Xaw3d-Entwicklung
Summary(es):	Archivos para desarrollo de programas que usan Xaw3d
Summary(fr):	Fichiers pour dИvelopper des programmes utilisant Xaw3d
Summary(pl):	Pliki potrzebne przy kompilacji programСw u©ywaj╠cych Xaw3d
Summary(pt_BR):	Arquivos para desenvolvimento de programas que usam Xaw3d
Summary(ru):	Файлы для разработки программ, использующих Xaw3d
Summary(tr):	Xaw3d kitaplЩПЩnЩ kullanan programlar geliЧtirmek iГin gerekli dosyalar
Summary(uk):	Файли для розробки програм, як╕ використовують Xaw3d
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Obsoletes:	libXaw3d7-devel

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Window that adds a 3-dimensional look to the applications with
minimal or no source code changes.

This package includes the header files developing programs that take
full advantage of Xaw3d's features.

%description devel -l de
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets fЭr
X-Window, das einer Applikationen mit minimalen oder keinen
дnderungen am Quellcode einen 3D-Look verleiht. Das Paket enthДlt die
Headerdateien zur Entwicklung von Programmen, die die Vorteile von
Xaw3d voll nutzen.

%description devel -l es
Xaw3d es una versiСn incrementada del conjunto MIT Athena Widget para
X Window que adiciona una visiСn tridimensional a las aplicaciones con
cambios mМnimos, o ninguno, en los cСdigos fuente. Este paquete
incluye los archivos principales y las bibliotecas para programas de
desarrollo que utilizan total ventaja de las caracterМsticas de Xaw3d.

%description devel -l fr
Xaw3d est une version amИliorИe de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code. Ce paquetage contient les
en-tЙtes pour dИvelopper des programmes tirant plein avantage des
caractИristiques de Xaw3d.

%description devel -l pl
Xaw3d jest ulepszon╠ wersj╠ biblioteki X Athena Widget, ktСra dodaje
trСjwymiarowy wygl╠d aplikacjom przy minimalnych (lub ©adnych)
zmianach kodu ╪rСdЁowego.

Ten pakiet zawiera pliki nagЁСwkowe potrzebne do kompilacji programСw
wykorzystuj╠cych Xaw3d.

%description devel -l pt_BR
Xaw3d И uma versЦo incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma visЦo tri-dimensional Юs aplicaГУes com
mudanГas mМnimas ou nenhuma nos cСdigos fonte. Este pacote inclui os
arquivos principais e as bibliotecas para programas de desenvolvimento
que utilizam total vantagem das caracterМsticas de Xaw3d.

%description devel -l uk
Xaw3d - це покращена верс╕я набору екранних прим╕тив╕в MIT Athena
Widget для X Window, яка нада╓ програмам "трьохвим╕рного" вигляду з
м╕н╕мальними зм╕нами вих╕дного коду (у б╕льшост╕ випадк╕в без зм╕н).
Цей пакет м╕стить хедери та б╕бл╕отеки програм╕ста, необх╕дн╕ для
розробки програм, як╕ використовують Xaw3d.

%description devel -l ru
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений). Этот пакет содержит хедеры и библиотеки разработчика,
необходимые для разработки программ, использующих Xaw3d.

%package static
Summary:	Xaw3d static library
Summary(es):	Bibliotecas estАticas para el desarrollo con Xaw3d
Summary(pl):	Biblioteki statyczne Xaw3d
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com Xaw3d
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм, як╕ використовують Xaw3d
Summary(ru):	Статические библиотеки для разработки программ, использующих Xaw3d
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Window that adds a 3-dimensional look to the applications with
minimal or no source code changes.

This package includes the static library for developing programs that
take full advantage of Xaw3d's features.

%description static -l de
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets fЭr
X-Window, das einer Applikationen mit minimalen oder keinen
дnderungen am Quellcode einen 3D-Look verleiht. Das Paket enthДlt die
statischen Library zur Entwicklung von Programmen, die die Vorteile
von Xaw3d voll nutzen.

%description static -l pl
Xaw3d jest ulepszon╠ wersj╠ biblioteki X Athena Widget, ktСra dodaje
trСjwymiarowy wygl╠d aplikacjom przy minimalnych (lub ©adnych)
zmianach kodu ╪rСdЁowego.

Ten pakiet zawiera biblioteki statyczne dla Xaw3d.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com Xaw3d.

%description static -l uk
Xaw3d - це покращена верс╕я набору екранних прим╕тив╕в MIT Athena
Widget для X Window, яка нада╓ програмам "трьохвим╕рного" вигляду з
м╕н╕мальними зм╕нами вих╕дного коду (у б╕льшост╕ випадк╕в без зм╕н).
Цей пакет м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки програм,
як╕ використовують Xaw3d.

%description static -l ru
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений). Этот пакет содержит статические библиотеки, необходимые
для разработки программ, использующих Xaw3d.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5

%build
export PATH=%{_bindir}:$PATH
cd xc/lib/Xaw3d
xmkmf
mkdir X11; ln -s `pwd` X11/Xaw3d
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	EXTRA_INCLUDES=-I.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/X11

cd xc/lib/Xaw3d
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d \
	$RPM_BUILD_ROOT%{_includedir}/Xaw3d
ln -s ../Xaw3d $RPM_BUILD_ROOT%{_includedir}/X11/Xaw3d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xc/lib/Xaw3d/README.XAW3D
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/Xaw3d
%{_includedir}/X11/Xaw3d

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
