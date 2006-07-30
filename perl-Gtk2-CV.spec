#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	CV
Summary:	perl(Gtk2::CV) - 
Name:		perl-Gtk2-CV
Version:	1.2
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94fa4d991704f5ff038650ec2eeab0cd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl module Gtk2::CV which implements image viewer, but unfortunatelly
there is no documentation for base module. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%dir %{perl_vendorarch}/auto/Gtk2/CV
%{perl_vendorarch}/auto/Gtk2/CV/CV.*
%{perl_vendorarch}/Gtk2/CV.pm
%{perl_vendorarch}/Gtk2/CV/Plugin/*.pm
%{perl_vendorarch}/Gtk2/CV/*.pm
%dir %{perl_vendorarch}/Gtk2/CV
%dir %{perl_vendorarch}/Gtk2/CV/Plugin
%dir %{perl_vendorarch}/Gtk2/CV/images
%{perl_vendorarch}/Gtk2/CV/images/*.png
%{perl_vendorarch}/Gtk2/CV/gtkrc
%{_mandir}/man3/*
%{_mandir}/man1/*
