Summary:	Phorum is a web based message board written in PHP
Summary(pl):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	3.4
Release:	1
License:	Apache-like
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
URL:		http://phorum.org/
Requires:       webserver
Requires:	php >= 4.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define	_phorumdir	/home/services/httpd/html/phorum
%define		_phorumdir	/home/httpd/html/phorum

%description
Phorum is a web based message board written in PHP
who's goal is to be database and platform independent.
Phorum is designed with high-availability and visitor
ease of use in mind. Features such as mailing list
integration, easy customization and simple
installation make Phorum a powerful add-in to any
website.

%description -l pl
Phorum jest forum dyskusyjnym WWW napisanym w PHP.
Zamierzeniem deweloper�w jest uzyskanie niezale�no�ci
od konkretnego systemu bazy danych. 
�atwa obs�uga dla wypowiadaj�cych si� przybysz�w,
prosta instalacja, mo�liwo�� �atwego dostosowania
do indywidualnych potrzeb oraz integracja z listami
dyskusyjnymi czyni� Phorum atrakcyjnym dodatkiem
do ka�dej witryny

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phorumdir}
cp -a . $RPM_BUILD_ROOT%{_phorumdir}
rm -rf $RPM_BUILD_ROOT%{_phorumdir}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,http,755)
%doc docs/*
%{_phorumdir}/*.php
%{_phorumdir}/*.css
%{_phorumdir}/db
%{_phorumdir}/images
%{_phorumdir}/include
%{_phorumdir}/lang
%{_phorumdir}/plugin
%{_phorumdir}/scripts
%{_phorumdir}/smileys
%{_phorumdir}/admin/*.php
%{_phorumdir}/admin/actions
%{_phorumdir}/admin/lang
%{_phorumdir}/admin/pages
# fixme:
# may be the files below should be marked as config files
%dir %attr(775,root,http) %{_phorumdir}/admin/settings
%attr(664,root,http) %{_phorumdir}/admin/settings/forums.php
