%define	orgname	libXaw3d
Summary:	A version of the MIT Athena widget set for X
Summary(de.UTF-8):	3D-Version des MIT Athena-Widgetsatzes fuer X
Summary(es.UTF-8):	Widgets X athena en 3D
Summary(fr.UTF-8):	Widgets X Athena en 3D
Summary(pl.UTF-8):	Biblioteka X athena widgets (wersja 3D)
Summary(pt_BR.UTF-8):	Widgets X athena em 3d
Summary(ru.UTF-8):	Версия MIT Athena widget set для X
Summary(tr.UTF-8):	3D X Athena arayüz elemanları (widgets)
Summary(uk.UTF-8):	Версія MIT Athena widget set для X
Name:		Xaw3d
Version:	1.6.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/lib%{name}-%{version}.tar.xz
# Source0-md5:	ef452fd155740f879430945e8e7d93e7
URL:		https://xorg.freedesktop.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	fileutils
Obsoletes:	libXaw3d7 < 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X Window
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

%description -l de.UTF-8
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set für X
Window, das die Anwendung dreidimensional erscheinen läßt, ohne daß
umfangreiche Änderungen am Quellcode notwendig sind.

%description -l es.UTF-8
Xaw3d es una versión incrementada del conjunto MIT Athena Widget para
X Window que adiciona una apariencia tridimensional a las aplicaciones
con cambios mínimos, o ninguno, en los códigos fuente.

%description -l fr.UTF-8
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code.

%description -l pl.UTF-8
Xaw3d jest ulepszoną wersją biblioteki X Athena Widget, która dodaje
trójwymiarowy wygląd aplikacjom przy minimalnych (lub żadnych)
zmianach kodu źródłowego.

%description -l pt_BR.UTF-8
Xaw3d é uma versão incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma aparência tri-dimensional às aplicações com
mudanças mínimas ou nenhuma nos códigos fonte.

%description -l ru.UTF-8
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений).

%description -l tr.UTF-8
Xaw3d, MIT Athena kitaplığına, uygulamalara herhangi bir kod
değişikliği yapılmasını gerektirmeden (ya da ufak değişiklikler
yaparak), üç boyutlu bir görüntü kazandıran bir geliştirmedir.

%description -l uk.UTF-8
Xaw3d - це покращена версія набору екранних примітивів MIT Athena
Widget для X Window, яка надає програмам "трьохвимірного" вигляду з
мінімальними змінами вихідного коду (у більшості випадків без змін).

%package devel
Summary:	Files for developing programs that use Xaw3d
Summary(de.UTF-8):	Header und statische Libraries fuer Xaw3d-Entwicklung
Summary(es.UTF-8):	Archivos para desarrollo de programas que usan Xaw3d
Summary(fr.UTF-8):	Fichiers pour développer des programmes utilisant Xaw3d
Summary(pl.UTF-8):	Pliki potrzebne przy kompilacji programów używających Xaw3d
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento de programas que usam Xaw3d
Summary(ru.UTF-8):	Файлы для разработки программ, использующих Xaw3d
Summary(tr.UTF-8):	Xaw3d kitaplığını kullanan programlar geliştirmek için gerekli dosyalar
Summary(uk.UTF-8):	Файли для розробки програм, які використовують Xaw3d
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	libXaw3d7-devel < 1.6

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X Window
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

This package includes the header files developing programs that take
full advantage of Xaw3d's features.

%description devel -l de.UTF-8
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für
X-Window, das einer Applikationen mit minimalen oder keinen Änderungen
am Quellcode einen 3D-Look verleiht. Das Paket enthält die
Headerdateien zur Entwicklung von Programmen, die die Vorteile von
Xaw3d voll nutzen.

%description devel -l es.UTF-8
Xaw3d es una versión incrementada del conjunto MIT Athena Widget para
X Window que adiciona una visión tridimensional a las aplicaciones con
cambios mínimos, o ninguno, en los códigos fuente. Este paquete
incluye los archivos principales y las bibliotecas para programas de
desarrollo que utilizan total ventaja de las características de Xaw3d.

%description devel -l fr.UTF-8
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code. Ce paquetage contient les
en-têtes pour développer des programmes tirant plein avantage des
caractéristiques de Xaw3d.

%description devel -l pl.UTF-8
Xaw3d jest ulepszoną wersją biblioteki X Athena Widget, która dodaje
trójwymiarowy wygląd aplikacjom przy minimalnych (lub żadnych)
zmianach kodu źródłowego.

Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
wykorzystujących Xaw3d.

%description devel -l pt_BR.UTF-8
Xaw3d é uma versão incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma visão tri-dimensional às aplicações com
mudanças mínimas ou nenhuma nos códigos fonte. Este pacote inclui os
arquivos principais e as bibliotecas para programas de desenvolvimento
que utilizam total vantagem das características de Xaw3d.

%description devel -l uk.UTF-8
Xaw3d - це покращена версія набору екранних примітивів MIT Athena
Widget для X Window, яка надає програмам "трьохвимірного" вигляду з
мінімальними змінами вихідного коду (у більшості випадків без змін).
Цей пакет містить хедери та бібліотеки програміста, необхідні для
розробки програм, які використовують Xaw3d.

%description devel -l ru.UTF-8
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений). Этот пакет содержит хедеры и библиотеки разработчика,
необходимые для разработки программ, использующих Xaw3d.

%package static
Summary:	Xaw3d static library
Summary(es.UTF-8):	Bibliotecas estáticas para el desarrollo con Xaw3d
Summary(pl.UTF-8):	Biblioteki statyczne Xaw3d
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com Xaw3d
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм, які використовують Xaw3d
Summary(ru.UTF-8):	Статические библиотеки для разработки программ, использующих Xaw3d
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X Window
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

This package includes the static library for developing programs that
take full advantage of Xaw3d's features.

%description static -l de.UTF-8
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für
X-Window, das einer Applikationen mit minimalen oder keinen Änderungen
am Quellcode einen 3D-Look verleiht. Das Paket enthält die statischen
Library zur Entwicklung von Programmen, die die Vorteile von Xaw3d
voll nutzen.

%description static -l pl.UTF-8
Xaw3d jest ulepszoną wersją biblioteki X Athena Widget, która dodaje
trójwymiarowy wygląd aplikacjom przy minimalnych (lub żadnych)
zmianach kodu źródłowego.

Ten pakiet zawiera biblioteki statyczne dla Xaw3d.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com Xaw3d.

%description static -l uk.UTF-8
Xaw3d - це покращена версія набору екранних примітивів MIT Athena
Widget для X Window, яка надає програмам "трьохвимірного" вигляду з
мінімальними змінами вихідного коду (у більшості випадків без змін).
Цей пакет містить статичні бібліотеки, необхідні для розробки програм,
які використовують Xaw3d.

%description static -l ru.UTF-8
Xaw3d - это улучшенная версия набора экранных примитивов MIT Athena
Widget для X Window, придающая приложениям "трехмерный" вид с
минимальными изменениями исходного текста (в большинстве случаев без
изменений). Этот пакет содержит статические библиотеки, необходимые
для разработки программ, использующих Xaw3d.

%prep
%setup -q -n %{orgname}-%{version}

%build
%configure \
	--disable-silent-rules \
	--enable-arrow-scrollbars \
	--enable-gray-stipples \
	--enable-internationalization \
	--enable-multiplane-bitmaps

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf X11/Xaw3d $RPM_BUILD_ROOT%{_includedir}/Xaw3d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXaw3d.la

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXaw3d/README.XAW3D

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%pretrans devel
# migration from Xaw3d 1.5E (where X11/Xaw3d was symlink to ../Xaw3d)
if [ -d %{_includedir}/Xaw3d -a -L %{_includedir}/X11/Xaw3d ]; then
	rm -f %{_includedir}/X11/Xaw3d
	mv -f %{_includedir}/Xaw3d %{_includedir}/X11/Xaw3d
	ln -snf X11/Xaw3d %{_includedir}/Xaw3d
fi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md src/README.XAW3D
%attr(755,root,root) %{_libdir}/libXaw3d.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXaw3d.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw3d.so
%{_includedir}/Xaw3d
%{_includedir}/X11/Xaw3d
%{_pkgconfigdir}/xaw3d.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw3d.a
