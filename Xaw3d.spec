Summary:	A version of the MIT Athena widget set for X
Summary(de):	3D-Version des MIT Athena-Widgetsatzes fuer X
Summary(es):	Widgets X athena en 3D
Summary(fr):	Widgets X Athena en 3D
Summary(pl):	Biblioteka X athena widgets (wersja 3D)
Summary(pt_BR):	Widgets X athena em 3d
Summary(ru):	������ MIT Athena widget set ��� X
Summary(tr):	3D X Athena aray�z elemanlar� (widgets)
Summary(uk):	���Ӧ� MIT Athena widget set ��� X
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
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set f�r X
Window, das die Anwendung dreidimensional erscheinen l��t, ohne da�
umfangreiche �nderungen am Quellcode notwendig sind.

%description -l es
Xaw3d es una versi�n incrementada del conjunto MIT Athena Widget para
X Window que adiciona una apariencia tridimensional a las aplicaciones
con cambios m�nimos, o ninguno, en los c�digos fuente.

%description -l fr
Xaw3d est une version am�lior�e de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code.

%description -l pl
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych)
zmianach kodu �r�d�owego.

%description -l pt_BR
Xaw3d � uma vers�o incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma apar�ncia tri-dimensional �s aplica��es com
mudan�as m�nimas ou nenhuma nos c�digos fonte.

%description -l ru
Xaw3d - ��� ���������� ������ ������ �������� ���������� MIT Athena
Widget ��� X Window, ��������� ����������� "����������" ��� �
������������ ����������� ��������� ������ (� ����������� ������� ���
���������).

%description -l tr
Xaw3d, MIT Athena kitapl���na, uygulamalara herhangi bir kod
de�i�ikli�i yap�lmas�n� gerektirmeden (ya da ufak de�i�iklikler
yaparak), �� boyutlu bir g�r�nt� kazand�ran bir geli�tirmedir.

%description -l uk
Xaw3d - �� ��������� ���Ӧ� ������ �������� ���ͦ��צ� MIT Athena
Widget ��� X Window, ��� ����� ��������� "�������ͦ�����" ������� �
ͦΦ�������� �ͦ���� ��Ȧ����� ���� (� ¦�����Ԧ �����˦� ��� �ͦ�).

%package devel
Summary:	Files for developing programs that use Xaw3d
Summary(de):	Header und statische Libraries fuer Xaw3d-Entwicklung
Summary(es):	Archivos para desarrollo de programas que usan Xaw3d
Summary(fr):	Fichiers pour d�velopper des programmes utilisant Xaw3d
Summary(pl):	Pliki potrzebne przy kompilacji program�w u�ywaj�cych Xaw3d
Summary(pt_BR):	Arquivos para desenvolvimento de programas que usam Xaw3d
Summary(ru):	����� ��� ���������� ��������, ������������ Xaw3d
Summary(tr):	Xaw3d kitapl���n� kullanan programlar geli�tirmek i�in gerekli dosyalar
Summary(uk):	����� ��� �������� �������, �˦ �������������� Xaw3d
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
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets f�r
X-Window, das einer Applikationen mit minimalen oder keinen
�nderungen am Quellcode einen 3D-Look verleiht. Das Paket enth�lt die
Headerdateien zur Entwicklung von Programmen, die die Vorteile von
Xaw3d voll nutzen.

%description devel -l es
Xaw3d es una versi�n incrementada del conjunto MIT Athena Widget para
X Window que adiciona una visi�n tridimensional a las aplicaciones con
cambios m�nimos, o ninguno, en los c�digos fuente. Este paquete
incluye los archivos principales y las bibliotecas para programas de
desarrollo que utilizan total ventaja de las caracter�sticas de Xaw3d.

%description devel -l fr
Xaw3d est une version am�lior�e de l'ensemble Athena Widget du MIT
pour X Window qui ajoute un aspect 3D aux applications avec peu, ou
pas du tout, de modification du code. Ce paquetage contient les
en-t�tes pour d�velopper des programmes tirant plein avantage des
caract�ristiques de Xaw3d.

%description devel -l pl
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych)
zmianach kodu �r�d�owego.

Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilacji program�w
wykorzystuj�cych Xaw3d.

%description devel -l pt_BR
Xaw3d � uma vers�o incrementada do conjunto MIT Athena Widget para X
Window que adiciona uma vis�o tri-dimensional �s aplica��es com
mudan�as m�nimas ou nenhuma nos c�digos fonte. Este pacote inclui os
arquivos principais e as bibliotecas para programas de desenvolvimento
que utilizam total vantagem das caracter�sticas de Xaw3d.

%description devel -l uk
Xaw3d - �� ��������� ���Ӧ� ������ �������� ���ͦ��צ� MIT Athena
Widget ��� X Window, ��� ����� ��������� "�������ͦ�����" ������� �
ͦΦ�������� �ͦ���� ��Ȧ����� ���� (� ¦�����Ԧ �����˦� ��� �ͦ�).
��� ����� ͦ����� ������ �� ¦�̦����� ������ͦ���, ����Ȧ�Φ ���
�������� �������, �˦ �������������� Xaw3d.

%description devel -l ru
Xaw3d - ��� ���������� ������ ������ �������� ���������� MIT Athena
Widget ��� X Window, ��������� ����������� "����������" ��� �
������������ ����������� ��������� ������ (� ����������� ������� ���
���������). ���� ����� �������� ������ � ���������� ������������,
����������� ��� ���������� ��������, ������������ Xaw3d.

%package static
Summary:	Xaw3d static library
Summary(es):	Bibliotecas est�ticas para el desarrollo con Xaw3d
Summary(pl):	Biblioteki statyczne Xaw3d
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com Xaw3d
Summary(uk):	������Φ ¦�̦����� ��� �������� �������, �˦ �������������� Xaw3d
Summary(ru):	����������� ���������� ��� ���������� ��������, ������������ Xaw3d
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xaw3d is an enhanced version of the MIT Athena Widget set for X
Window that adds a 3-dimensional look to the applications with
minimal or no source code changes.

This package includes the static library for developing programs that
take full advantage of Xaw3d's features.

%description static -l de
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets f�r
X-Window, das einer Applikationen mit minimalen oder keinen
�nderungen am Quellcode einen 3D-Look verleiht. Das Paket enth�lt die
statischen Library zur Entwicklung von Programmen, die die Vorteile
von Xaw3d voll nutzen.

%description static -l pl
Xaw3d jest ulepszon� wersj� biblioteki X Athena Widget, kt�ra dodaje
tr�jwymiarowy wygl�d aplikacjom przy minimalnych (lub �adnych)
zmianach kodu �r�d�owego.

Ten pakiet zawiera biblioteki statyczne dla Xaw3d.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com Xaw3d.

%description static -l uk
Xaw3d - �� ��������� ���Ӧ� ������ �������� ���ͦ��צ� MIT Athena
Widget ��� X Window, ��� ����� ��������� "�������ͦ�����" ������� �
ͦΦ�������� �ͦ���� ��Ȧ����� ���� (� ¦�����Ԧ �����˦� ��� �ͦ�).
��� ����� ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� �������� �������,
�˦ �������������� Xaw3d.

%description static -l ru
Xaw3d - ��� ���������� ������ ������ �������� ���������� MIT Athena
Widget ��� X Window, ��������� ����������� "����������" ��� �
������������ ����������� ��������� ������ (� ����������� ������� ���
���������). ���� ����� �������� ����������� ����������, �����������
��� ���������� ��������, ������������ Xaw3d.

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
