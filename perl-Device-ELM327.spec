%define upstream_name Device-ELM327
Summary:		Methods for reading OBD data with an ELM327 module
Name:			perl-%{upstream_name}
Version:		0.08
Release:		4
License:        GPL or Artistic
Group:          Development/Perl
Url:            https://metacpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/modules/by-module/Device/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	make
BuildRequires:  perl-devel
BuildRequires:  perl(Device::SerialPort)
Requires:       perl(Device::SerialPort)

%description
Methods for reading OBD data with an ELM327 module.

%prep
%setup -q -n %{upstream_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{make}

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Device/ELM327.pm
%{_mandir}/man3/Device::ELM327.3pm.*