%define upstream_name	 Email-MIME
%define upstream_version 1.926

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Easy MIME message parsing
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/Email-MIME-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(Email::MessageID)
BuildRequires:	perl(Email::MIME::ContentType)
BuildRequires:	perl(Email::MIME::Encodings)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Email::Simple::Creator)
BuildRequires:	perl(MIME::Types)

BuildArch:	noarch

Obsoletes:	perl-Email-MIME-Creator <= 1.456.0
Provides:	perl-Email-MIME-Creator  = 1.456.0
Obsoletes:	perl-Email-MIME-Modifier <= 1.444.0
Provides:	perl-Email-MIME-Modifier  = 1.444.0

Requires:	perl(Email::Simple)

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its constituent
parts, and allows you access to various parts of the message. Headers are
decoded from MIME encoding.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.908.0-1mdv2011.0
+ Revision: 684742
- update to new version 1.908

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.907.0-1
+ Revision: 635506
- update to new version 1.907

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.906.0-1mdv2011.0
+ Revision: 587625
- new version

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.904.0-1mdv2011.0
+ Revision: 576297
- update to 1.904

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.903.0-2mdv2011.0
+ Revision: 561022
- email::mime::creator merged within email::mime
- email::mime::modifier merged within email::mime

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.903.0-1mdv2011.0
+ Revision: 482074
- update to 1.903

* Thu Nov 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.902.0-1mdv2010.1
+ Revision: 465209
- adding missing buildrequires:
- update to 1.902

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.901.0-1mdv2010.1
+ Revision: 460769
- adding missing buildrequires
- update to 1.901

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.863.0-2mdv2010.0
+ Revision: 378258
- use new %%perl_convert_version macro

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.863-1mdv2010.0
+ Revision: 374423
- update to new version 1.863

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new release
    - standardized version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.86.1-3mdv2009.0
+ Revision: 256754
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.86.1-1mdv2008.1
+ Revision: 109611
- new version (upstream version 1.861)

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.86.0-1mdv2008.0
+ Revision: 55629
- update to new version 1.86.0

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.9-1mdv2008.0
+ Revision: 48063
- update to new version 1.859


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.8-1mdv2007.1
+ Revision: 138829
- new version

* Sat Jan 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.7-2mdv2007.1
+ Revision: 111155
- fix dependencies

* Mon Dec 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.7-1mdv2007.1
+ Revision: 94846
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.5-1mdv2007.1
+ Revision: 86528
- new version
- Import perl-Email-MIME

* Sat Sep 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.2-1mdv2007.0
- New version (upstream version 1.852)

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.85.1-1mdv2007.0
- New version (upstream version: 1.85.1)

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.85-1mdv2007.0
- new version

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.82-2mdk
- fix buildrequires

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.82-1mdk
- first mdk release



