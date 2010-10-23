%define upstream_name	 Email-MIME
%define upstream_version 1.906

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Easy MIME message parsing
License:	GPL+ or Artistic
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Email::Date::Format)
BuildRequires:	perl(Email::MessageID)
BuildRequires:	perl(Email::MIME::ContentType)
BuildRequires:	perl(Email::MIME::Encodings)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Email::Simple::Creator)
BuildRequires:	perl(MIME::Types)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Email-MIME-Creator <= 1.456.0
Provides:  perl-Email-MIME-Creator  = 1.456.0
Obsoletes: perl-Email-MIME-Modifier <= 1.444.0
Provides:  perl-Email-MIME-Modifier  = 1.444.0

Requires:       perl(Email::Simple)

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its constituent
parts, and allows you access to various parts of the message. Headers are
decoded from MIME encoding.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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
