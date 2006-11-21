Summary:	Phorum is a web based message board written in PHP
Summary(pl):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	5.0.21
Release:	0.20
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	9793ba89aa3ab074163e1c61e4cea25c
Source1:	%{name}-apache.conf
Patch0:		%{name}-paths.patch
URL:		http://www.phorum.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	webapps
Requires:	webserver(php) >= 4.3.0
BuildArch:	noarch
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

%package setup
Summary:	Phorum setup package
Summary(pl):	Pakiet do wstêpnej konfiguracji Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial Phorum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl
Ten pakiet nale¿y zainstalowaæ w celu wstêpnej konfiguracji Phorum po
pierwszej instalacji. Potem nale¿y go odinstalowaæ, jako ¿e
pozostawienie plików instalacyjnych mog³oby byæ niebezpieczne.

%prep
%setup -q
%patch0 -p1
rm {cache,portable,include,mods}/.htaccess
rm -rf include/db/upgrade/mysql/200{3,4}* # Not supported in PLD
mv include/db/config.php.sample .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}/htdocs/templates/default,/var/cache/phorum}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}/htdocs
mv $RPM_BUILD_ROOT%{_appdir}/{htdocs/,}common.php
cp -a include mods templates $RPM_BUILD_ROOT%{_appdir}
cp -a images smileys $RPM_BUILD_ROOT%{_appdir}/htdocs
mv $RPM_BUILD_ROOT%{_appdir}/{,htdocs/}templates/default/images

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -p config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%post setup
if [ "$1" = 1 ]; then
	%banner -e %{name} <<-EOF
	Setup is simple as:
	1. creating mysql database:
	mysqladmin create phorum5
	2. granting privs and editing %{_sysconfdir}/config.php
	3. opening http://localhost/phorum/admin.php
EOF
fi

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc docs/* *.txt scripts portable
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%{_appdir}/common.php
%{_appdir}/templates
%{_appdir}/mods
%dir %{_appdir}/include
%{_appdir}/include/*.php
%{_appdir}/include/*.js
%{_appdir}/include/db
%{_appdir}/include/controlcenter
%{_appdir}/include/lang
%dir %{_appdir}/htdocs
%{_appdir}/htdocs/attach.php
%{_appdir}/htdocs/control.php
%{_appdir}/htdocs/edit.php
%{_appdir}/htdocs/file.php
%{_appdir}/htdocs/follow.php
%{_appdir}/htdocs/index.php
%{_appdir}/htdocs/list.php
%{_appdir}/htdocs/login.php
%{_appdir}/htdocs/moderation.php
%{_appdir}/htdocs/post.php
%{_appdir}/htdocs/profile.php
%{_appdir}/htdocs/read.php
%{_appdir}/htdocs/register.php
%{_appdir}/htdocs/script.php
%{_appdir}/htdocs/search.php
%{_appdir}/htdocs/smileys
%{_appdir}/htdocs/templates
%{_appdir}/htdocs/images
%dir %attr(770,root,http) /var/cache/phorum

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/admin.php
%{_appdir}/include/admin
