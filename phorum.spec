Summary:	Phorum is a web based message board written in PHP
Summary(pl):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	5.0.10
Release:	0.2
License:	Apache-like
Group:		Applications/WWW
Source0:	http://phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	52519423489765db680acc1b1d17eba5
URL:		http://phorum.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php >= 3:4.0.6
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
rm {cache,portable,include,mods}/.htaccess

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a cache images include mods portable smileys templates $RPM_BUILD_ROOT%{_appdir}

> $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
> $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

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
%{_appdir}/admin.php
%{_appdir}/attach.php
%{_appdir}/common.php
%{_appdir}/control.php
%{_appdir}/edit.php
%{_appdir}/file.php
%{_appdir}/follow.php
%{_appdir}/images
%{_appdir}/include/admin
%{_appdir}/include/*.php
%{_appdir}/include/controlcenter
%{_appdir}/include/db/config.php.sample
%{_appdir}/include/db/mysql.php
%{_appdir}/include/db/postgresql.php
%{_appdir}/include/db/upgrade/mysql
%{_appdir}/include/dhtml_popup.js
%{_appdir}/include/lang/english.php
%{_appdir}/index.php
%{_appdir}/list.php
%{_appdir}/login.php
%{_appdir}/moderation.php
%{_appdir}/mods/bbcode
%{_appdir}/mods/html
%{_appdir}/mods/replace
%{_appdir}/mods/smileys
%{_appdir}/portable
%{_appdir}/post.php
%{_appdir}/profile.php
%{_appdir}/read.php
%{_appdir}/register.php
%{_appdir}/script.php
%{_appdir}/search.php
%{_appdir}/smileys
%{_appdir}/templates
