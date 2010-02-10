# TODO
# - modules images are not accessible from web
%define		mainver	5.2
Summary:	Phorum is a web based message board written in PHP
Summary(pl.UTF-8):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	%{mainver}.14
Release:	0.48
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	944211b4f195a538bcb6e2883d2187c5
Source1:	http://www.phorum.org/phorum5/file.php/download/65/2522/%{name}-estonian-5.2.7a.zip
# Source1-md5:	cd2d5fb9b0b17da0d805209ac76b58d4
Source2:	http://www.phorum.org/phorum5/file.php/65/4131/Russian-Utf8.zip
# Source2-md5:	510e8b1750bebef99fdfdab3504ac60d
Source3:	apache.conf
Patch0:		paths.patch
Patch1:		mysql.patch
Patch2:		docsurl.patch
Patch3:		sys-phpmailer.patch
Patch4:		sys-recaptcha.patch
URL:		http://www.phorum.org/
BuildRequires:	glibc-misc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	webapps
Requires:	webserver(php) >= 4.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
%define		_phpdocdir	%{_docdir}/phpdoc
%define		_cachedir	/var/cache/phorum

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

%package phpdoc
Summary:	Online manual for Phorum
Summary(pl.UTF-8):	Dokumentacja online do Phorum
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for Phorum.

%description phpdoc -l pl.UTF-8
Dokumentacja do Phorum.

%package mod-announcements
Summary:	Phorum Announcements module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-announcements
Shows topics from one forum as announcements in a variety of ways.

%package mod-bbcode
Summary:	Phorum BBcode module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-bbcode
This module allows users to add BBcode (Bulletin Board Code) tags to
their postings. BBcode tags are a safe way of adding markup (bold,
italic, images, links, etc.). Created by Phorum Dev Team

%package mod-editor_tools
Summary:	Phorum Editor tools module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-editor_tools
This module will add a tool bar to the Phorum message editor, which
can be used by visitors to easily add things like BBcode tags and
smileys to their postings.

%package mod-event_logging
Summary:	Phorum Event Logging module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-event_logging
This module implements an event logging system, which can be used for
logging various events. Other modules can use this module for logging
purposes too.

%package mod-smtp_mail
Summary:	Phorum Send mail through SMTP module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php-phpmailer >= 2.3

%description mod-smtp_mail
This module allows Phorum to send the email through an SMTP server
instead of using PHP's mail() function.

Some ISPs disable the mail() function, in which case this module is
needed to send emails to users. Only use it if you need it.

%package mod-replace
Summary:	Phorum Simple Text Replacement Module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-replace
This module allows admins to define text replacement in messages.

%package mod-smileys
Summary:	Phorum Smileys Module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-smileys
This module allows users to add graphical smileys to their messages.

%package mod-spamhurdles
Summary:	Phorum Spam Hurdle Module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php-recaptcha

%description mod-spamhurdles
This module sets up some hurdles for forum spammers. It implements
both interactive (CAPTCHA) and non-interactive anti-spam methods to
keep away spam bots. On the settings page, you can control exactly
what hurdles to enable.

%package mod-tidy
Summary:	Phorum Tidy Output Module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-tidy
This module removes unneeded white space from Phorum's output saving
bandwidth.

%package mod-username_restrictions
Summary:	Phorum Username Restrictions Module
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description mod-username_restrictions
This module implements configurable features for enforcing user name
restrictions. The module will check the user name at registration time
and show an error to the user if the new username does not meet the
restrictions.

%package template-classic
Summary:	Classic template for Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(template) = %{mainver}

%description template-classic
Classic template for Phorum.

%package template-emerald
Summary:	Emerald template for Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(template) = %{mainver}

%description template-emerald
Emerald template for Phorum.

%package template-lightweight
Summary:	Lightweight template for Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(template) = %{mainver}

%description template-lightweight
Lightweight template for Phorum.

%prep
%setup -q -a1 -a2
find '(' -name '*.php' -o -name '*.css' -o -name '*.js' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

install -d htdocs/admin examples

# htaccess will be provided by apache.conf
find -name .htaccess | xargs rm -v

# php-phpmailer
rm -rf mods/smtp_mail/phpmailer

# php-recaptcha
rm -rf mods/spamhurdles/captcha/recaptcha-php-1.9
rm -f mods/spamhurdles/MANIFEST

mv include/db/config.php.sample .
mv include/api/examples examples/api
mv docs/example_mods examples/mods
mv portable scripts examples
# so we don't have to package html/pdf/docbook via docs/*
mv docs/html htmldoc
mv docs/docbook .
mv docs/pdf pdfdoc

mv russian.php include/lang
iconv -fcp1251 -tutf8 'readme!!!.txt' > docs/README.ru
rm -f 'readme!!!.txt'

# kill old files by phorum
rm post.php

# fixup structure, move public files to htdocs.
mv *.php images htdocs

# still private files (not for web)
mv htdocs/common.php .
mv htdocs/script.php .

# admin css
mv include/admin/css htdocs/admin

# move template images to htdocs
for a in templates/*/images; do
	d=$(dirname "$a");
	install -d htdocs/$d
	mv $a htdocs/$d
done

# unify loading includes
a="'" q='"'
grep -Elr '(include|require)_once' include htdocs mods *.php | xargs sed -i -e "
# common.php
	s,\\(include\\|require\\)_once(\s*[$a$q]\./common.php[$a$q]\s*);,require_once PHORUM_DIR.'/common.php';,g
	s,include_once(\s*[$a$q]./common.php[$a$q]\s*);,require_once PHORUM_DIR.'/common.php';,g
	s,include_once\s*[$a$q]./common.php[$a$q]\s*;,require_once PHORUM_DIR.'/common.php';,g

# random includes
	s,include_once\s*([$a$q]include/\([^$a$q]\\+\)[$a$q]);,require_once PHORUM_INCLUDES_DIR.'/\\1';,g
	s,\\(include\\|require\\)_once\s*(\s*[$a$q]\./include/\([^$a$q]\\+\)[$a$q]\s*);,require_once PHORUM_INCLUDES_DIR.'/\\2';,g
	s,\\(include\\|require\\)_once\s*[$a$q]\./include/\([^$a$q]\\+\)[$a$q];,require_once PHORUM_INCLUDES_DIR.'/\\2';,g
	s,include\s*([$a$q]\./include/\([^$a$q]\\+\)[$a$q]);,include PHORUM_INCLUDES_DIR.'/\\1';,g

# mods
	s,require_once\s*([$a$q]\./mods/\([^$a$q]\\+\)[$a$q]);,require_once PHORUM_DIR.'/mods/\\1';,g
"

# update path to common.php
sed -i -e "s,require_once PHORUM_DIR.'/common.php';,require_once '../common.php';," htdocs/*.php
sed -i -e "s,require_once PHORUM_DIR.'/common.php';,require_once 'common.php';," *.php

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{_cachedir}}
cp -a *.php htdocs include mods templates $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/config.php

cat > langmap <<'EOF'
cs czech
cs czech-latin2
cs czech-utf8
cs czech-win1250
da danish
de german
de german_sie
en english
es spanish
es spanish_latin_american
et estonian
fi finnish
fr french
it italian
nb norwegian
nl dutch
nl dutch_informal
ru russian
sv swedish
tr turkish
EOF

rm -f *.lang

echo "%dir %{_appdir}/include/lang" >> %{name}.lang
while read code lang; do
	[ -f include/lang/$lang.php ] && echo "%lang($code) %{_appdir}/include/lang/$lang.php" >> %{name}.lang
done < langmap

for mod in mods/*/; do
	mod=${mod%/} file=${mod#mods/}.lang
	> $file
	[ -f $mod/Changelog ] && echo %{_appdir}/$mod/Changelog >> $file
	[ -f $mod/README ] && echo %{_appdir}/$mod/README >> $file
	[ -f $mod/TODO ] && echo %{_appdir}/$mod/TODO >> $file
	[ -f $mod/info.txt ] && echo %{_appdir}/$mod/info.txt >> $file
	[ -f $mod/MANIFEST ] && echo %{_appdir}/$mod/MANIFEST >> $file
	[ -d $mod/icons ] && echo %{_appdir}/$mod/icons >> $file
	[ -d $mod/images ] && echo %{_appdir}/$mod/images >> $file
	[ -d $mod/templates ] && echo %{_appdir}/$mod/templates >> $file
	if [ -d $mod/lang ]; then
		echo "%dir %{_appdir}/$mod/lang" >> $file
		while read code lang; do
			[ -f $mod/lang/$lang.php ] && echo "%lang($code) %{_appdir}/$mod/lang/$lang.php" >> $file
		done < langmap
	fi
	if [ -d $mod/help ]; then
		echo "%dir %{_appdir}/$mod/help" >> $file
		while read code lang; do
			[ -d $mod/help/$lang ] && echo "%lang($code) %{_appdir}/$mod/help/$lang" >> $file
		done < langmap
	fi
	echo "%{_appdir}/$mod/*.php" >> $file
done

# apidoc
install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
cp -a htmldoc/api/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

# examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post template-classic
rm -f %{_cachedir}/tpl-classic-*

%postun template-classic
if [ "$1" = 0 ]; then
	rm -f %{_cachedir}/tpl-classic-*
fi

%post template-emerald
rm -f %{_cachedir}/tpl-emerald-*

%postun template-emerald
if [ "$1" = 0 ]; then
	rm -f %{_cachedir}/tpl-emerald-*
fi

%post template-lightweight
rm -f %{_cachedir}/tpl-lightweight-*

%postun template-lightweight
if [ "$1" = 0 ]; then
	rm -f %{_cachedir}/tpl-lightweight-*
fi

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php

%dir %{_appdir}
%{_appdir}/common.php
%{_appdir}/script.php
%dir %{_appdir}/mods

%dir %{_appdir}/include
%dir %{_appdir}/include/db
%{_appdir}/include/db/mysql
%{_appdir}/include/db/mysql.php
%{_appdir}/include/*.php
%{_appdir}/include/controlcenter
%{_appdir}/include/posting
%{_appdir}/include/ajax
%{_appdir}/include/api
%{_appdir}/include/cache

%dir %{_appdir}/htdocs
%dir %{_appdir}/htdocs/templates
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
%{_appdir}/htdocs/search.php
%{_appdir}/htdocs/versioncheck.php

%dir %attr(770,root,http) /var/cache/phorum

%{_examplesdir}/%{name}-%{version}

%files setup
%defattr(644,root,root,755)
%{_appdir}/htdocs/admin
%{_appdir}/htdocs/admin.php
%{_appdir}/include/admin
%{_appdir}/include/db/upgrade

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}

%files mod-announcements -f announcements.lang
%defattr(644,root,root,755)

%files mod-bbcode -f bbcode.lang
%defattr(644,root,root,755)
%{_appdir}/mods/bbcode/colorpicker
%{_appdir}/mods/bbcode/*.js
%{_appdir}/mods/bbcode/help/*.css
%{_appdir}/mods/bbcode/help/*.gif

%files mod-editor_tools -f editor_tools.lang
%defattr(644,root,root,755)
%{_appdir}/mods/editor_tools/*.js
%{_appdir}/mods/editor_tools/*.css

%files mod-event_logging -f event_logging.lang
%defattr(644,root,root,755)
%{_appdir}/mods/event_logging/db
%{_appdir}/mods/event_logging/settings

%files mod-replace -f replace.lang
%defattr(644,root,root,755)

%files mod-smileys -f smileys.lang
%defattr(644,root,root,755)
%{_appdir}/mods/smileys/*.css
%{_appdir}/mods/smileys/*.gif
%{_appdir}/mods/smileys/help/*.css
%{_appdir}/mods/smileys/help/*.php

%files mod-spamhurdles -f spamhurdles.lang
%defattr(644,root,root,755)
%{_appdir}/mods/spamhurdles/captcha
%{_appdir}/mods/spamhurdles/db
%{_appdir}/mods/spamhurdles/lib
%{_appdir}/mods/spamhurdles/*.css
%{_appdir}/mods/spamhurdles/*.jpg

%files mod-tidy
%defattr(644,root,root,755)
%{_appdir}/mods/mod_tidy.php

%files mod-username_restrictions -f username_restrictions.lang
%defattr(644,root,root,755)

%files mod-smtp_mail -f smtp_mail.lang
%defattr(644,root,root,755)

%files template-classic
%defattr(644,root,root,755)
%{_appdir}/templates/classic
%{_appdir}/htdocs/templates/classic

%files template-emerald
%defattr(644,root,root,755)
%{_appdir}/templates/emerald
%{_appdir}/htdocs/templates/emerald

%files template-lightweight
%defattr(644,root,root,755)
%{_appdir}/templates/lightweight
%{_appdir}/htdocs/templates/lightweight
