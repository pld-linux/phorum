Summary:	Phorum is a web based message board written in PHP
Summary(pl):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	5.0.21
Release:	0.5
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	9793ba89aa3ab074163e1c61e4cea25c
Source1:	%{name}-apache.conf
Patch0:		%{name}-paths.patch
URL:		http://www.phorum.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php >= 3:4.3.0
Requires:	webapps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Phorum is a web based message board written in PHP who's goal is to be
database and platform independent. Phorum is designed with
high-availability and visitor ease of use in mind. Features such as
mailing list integration, easy customization and simple installation
make Phorum a powerful add-in to any website.

%description -l pl
Phorum jest forum dyskusyjnym WWW napisanym w PHP. Zamierzeniem
deweloperów jest uzyskanie niezale¿no¶ci od konkretnego systemu bazy
danych. £atwa obs³uga dla wypowiadaj±cych siê przybyszów, prosta
instalacja, mo¿liwo¶æ ³atwego dostosowania do indywidualnych potrzeb
oraz integracja z listami dyskusyjnymi czyni± Phorum atrakcyjnym
dodatkiem do ka¿dej witryny.

%prep
%setup -q
%patch0 -p1
rm {cache,portable,include,mods}/.htaccess
rm -rf include/db/upgrade/mysql/200{3,4}* # Not supported in PLD
mv include/db/config.php.sample .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a cache images include mods portable smileys templates $RPM_BUILD_ROOT%{_appdir}

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -p config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc docs/* *.txt scripts
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%{_appdir}/*.php
%{_appdir}/mods
%{_appdir}/portable
%{_appdir}/smileys
%{_appdir}/templates
%{_appdir}/images
%dir %{_appdir}/include
%{_appdir}/include/*.php
%{_appdir}/include/*.js
%{_appdir}/include/db
%{_appdir}/include/admin
%{_appdir}/include/controlcenter
%{_appdir}/include/lang
