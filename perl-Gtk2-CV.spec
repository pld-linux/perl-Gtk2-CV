#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	CV
Summary:	Gtk2::CV - a fast GTK+ image viewer loosely modeled after XV
Summary(pl.UTF-8):	Gtk2::CV - szybka przeglądarka obrazków oparta na GTK+ robiona na wzór XV
Name:		perl-Gtk2-CV
Version:	1.2
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94fa4d991704f5ff038650ec2eeab0cd
URL:		http://search.cpan.org/dist/Gtk2-CV/
BuildRequires:	libjpeg-devel
BuildRequires:	libmagic-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gtk2 >= 1.08
Requires:	perl-Gtk2-GladeXML >= 0.93
Requires:	perl-IO-AIO >= 1.4
Requires:	perl(Gtk2::PodViewer) >= 0.03
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Gtk2::CV which implements image viewer, but unfortunatelly
there is no documentation for base module. 

%description -l pl.UTF-8
Moduł Perla Gtk2::CV implementuje przeglądarkę obrazków, ale niestety
nie ma dokumentacji dla głównego modułu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%attr(755,root,root) %{_bindir}/cv
%{perl_vendorarch}/Gtk2/CV.pm
%dir %{perl_vendorarch}/Gtk2/CV
%{perl_vendorarch}/Gtk2/CV/*.pm
%{perl_vendorarch}/Gtk2/CV/gtkrc
%dir %{perl_vendorarch}/Gtk2/CV/Plugin
%{perl_vendorarch}/Gtk2/CV/Plugin/*.pm
%dir %{perl_vendorarch}/Gtk2/CV/images
%{perl_vendorarch}/Gtk2/CV/images/*.png
%dir %{perl_vendorarch}/auto/Gtk2/CV
%{perl_vendorarch}/auto/Gtk2/CV/CV.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/CV/CV.so
%{_mandir}/man1/*
%{_mandir}/man3/*
