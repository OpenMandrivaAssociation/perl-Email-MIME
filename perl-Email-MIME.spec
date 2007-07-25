%define module	    Email-MIME
%define name	    perl-%{module}
%define version     1.86.0
%define up_version  1.860
%define release     %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Easy MIME message parsing
License:	GPL or Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
Requires:       perl(Email::Simple)
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Email::MIME::ContentType)
BuildRequires:	perl(Email::MIME::Encodings)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its constituent
parts, and allows you access to various parts of the message. Headers are
decoded from MIME encoding.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Email
%{_mandir}/*/*


