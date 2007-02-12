#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Server-IRC
Summary:	POE::Component::Server::IRC - Perl extension for making a subclassable POE session 
Summary(pl.UTF-8):   POE::Component::Server::IRC - rozszerzenie do tworzenia dziedziczonych sesji POE
Name:		perl-POE-Component-Server-IRC
Version:	0.0001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a89dc71e568737a6940743b1fbcf4d8d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General framework for creating an IRC daemon. Very very alpha code,
structures are not fully designed, bugs do exist. That said, have fun
with it, I hope to upload new versions often enough.

%description -l pl.UTF-8
Ogólny szkielet do tworzenia demonów IRC. Kod zdecydowanie w stadium
alpha, nie ma jeszcze w pełni opracowanych struktur, zawiera błędy. To
oznacza, że można się z tym pobawić, autor ma nadzieję na
opublikowanie wkrótce nowych wersji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*/*/*
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
