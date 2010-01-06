Summary:	Phorum is a web based message board written in PHP
Summary(pl.UTF-8):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	5.2.14
Release:	0.1
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	944211b4f195a538bcb6e2883d2187c5
Source1:	%{name}-apache.conf
Patch0:		%{name}-paths.patch
Patch1:		%{name}-mysql.patch
Patch2:		docsurl.patch
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

%description -l pl.UTF-8
Phorum jest forum dyskusyjnym WWW napisanym w PHP. Zamierzeniem
deweloperów jest uzyskanie niezależności od konkretnego systemu bazy
danych. Łatwa obsługa dla wypowiadających się przybyszów, prosta
instalacja, możliwość łatwego dostosowania do indywidualnych potrzeb
oraz integracja z listami dyskusyjnymi czynią Phorum atrakcyjnym
dodatkiem do każdej witryny.

%package setup
Summary:	Phorum setup package
Summary(pl.UTF-8):	Pakiet do wstępnej konfiguracji Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial Phorum installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl.UTF-8
Ten pakiet należy zainstalować w celu wstępnej konfiguracji Phorum po
pierwszej instalacji. Potem należy go odinstalować, jako że
pozostawienie plików instalacyjnych mogłoby być niebezpieczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm {scripts,templates,cache,portable,include,mods}/.htaccess
mv include/db/config.php.sample .
mv include/api/examples docs/api_examples

# kill old files by phorum
rm post.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}/htdocs/templates/default,/var/cache/phorum}

cp -a *.php images $RPM_BUILD_ROOT%{_appdir}/htdocs
mv $RPM_BUILD_ROOT%{_appdir}/{htdocs/,}common.php

cp -a include mods templates $RPM_BUILD_ROOT%{_appdir}

# TODO: move themes images to htdocs
#mv $RPM_BUILD_ROOT%{_appdir}/{,htdocs/}templates/default/images
#mv $RPM_BUILD_ROOT%{_appdir}/{,htdocs/}templates/default/images

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/config.php

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
%doc docs/* scripts portable
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php

%dir %{_appdir}
%{_appdir}/common.php
%{_appdir}/templates
%{_appdir}/mods

%dir %{_appdir}/include
%{_appdir}/include/*.php
%{_appdir}/include/db
%{_appdir}/include/controlcenter
%{_appdir}/include/lang
%{_appdir}/include/posting
%{_appdir}/include/ajax
%{_appdir}/include/api
%{_appdir}/include/cache

%dir %{_appdir}/htdocs
%{_appdir}/htdocs/templates
%{_appdir}/htdocs/images

%{_appdir}/htdocs/addon.php
%{_appdir}/htdocs/ajax.php
%{_appdir}/htdocs/changes.php
%{_appdir}/htdocs/control.php
%{_appdir}/htdocs/css.php
%{_appdir}/htdocs/feed.php
%{_appdir}/htdocs/file.php
%{_appdir}/htdocs/follow.php
%{_appdir}/htdocs/index.php
%{_appdir}/htdocs/javascript.php
%{_appdir}/htdocs/list.php
%{_appdir}/htdocs/login.php
%{_appdir}/htdocs/moderation.php
%{_appdir}/htdocs/pm.php
%{_appdir}/htdocs/posting.php
%{_appdir}/htdocs/profile.php
%{_appdir}/htdocs/read.php
%{_appdir}/htdocs/redirect.php
%{_appdir}/htdocs/register.php
%{_appdir}/htdocs/report.php
%{_appdir}/htdocs/rss.php
%{_appdir}/htdocs/script.php
%{_appdir}/htdocs/search.php
%{_appdir}/htdocs/versioncheck.php

%dir %attr(770,root,http) /var/cache/phorum

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/admin.php
%{_appdir}/include/admin
