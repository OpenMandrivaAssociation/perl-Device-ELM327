%define upstream_name Device-ELM327
%define upstream_version 0.08

Summary:		Methods for reading OBD data with an ELM327 module
Name:			perl-%{upstream_name}
Version:		%perl_convert_version %{upstream_version}
Release:		3
License:        GPL or Artistic
Group:          Development/Perl
Url:            https://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/modules/by-module/Device/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  perl(Device::SerialPort)
Requires:       perl(Device::SerialPort)

%description
Methods for reading OBD data with an ELM327 module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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