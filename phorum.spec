# TODO
# - module images are not accessible from web
# - jquery accessed only by mods/editor_tools, move to plugin as hook?
%define		mainver	5.2
%define		php_min_version 5.2.0
Summary:	Phorum is a web based message board written in PHP
Summary(pl.UTF-8):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	%{mainver}.20
Release:	1
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	46c9edad965401102e1a943d13bf315e
Source3:	apache.conf
Patch0:		paths.patch
Patch1:		mysql.patch
Patch2:		docsurl.patch
Patch3:		sys-phpmailer.patch
Patch4:		sys-recaptcha.patch
Patch5:		enable-mbstring.patch
Patch6:		no-pear-json.patch
Patch10:	translate-macros.patch
Patch11:	wordwrap.patch
Patch12:	unhide-errors.patch
URL:		http://www.phorum.org/
BuildRequires:	iconv
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.595
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	%{name}(DB_Provider)
Requires:	php(date)
Requires:	php(gd)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	rpm-whiteout >= 1.33
Requires:	webapps
Requires:	webserver(access)
Requires:	webserver(alias)
Requires:	webserver(php) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no pear deps
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	php-date php-tokenizer

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

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

%package admin
Summary:	Administrative Interface for Phorum
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Obsoletes:	phorum-setup

%description admin
This package contains Administrative interface for Phorum.

%package phpdoc
Summary:	Online manual for Phorum
Summary(pl.UTF-8):	Dokumentacja online do Phorum
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for Phorum.

%description phpdoc -l pl.UTF-8
Dokumentacja do Phorum.

%package db-mysql
Summary:	Phorum MySQL Backend: mysql
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php(mysql)
Provides:	%{name}(DB_Provider)

%description db-mysql
Phorum MySQL Database backend via mysql PHP extension.

%package db-mysqli
Summary:	Phorum MySQL Backend: mysqli
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	php(mysqli)
Provides:	%{name}(DB_Provider)

%description db-mysqli
Phorum MySQL Database backend via mysqli PHP extension.

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
%setup -qc
mv Phorum-Core-*/* .
%undos -f php,css,js,html,txt

install -d htdocs/admin examples

# htaccess will be provided by apache.conf
find -name .htaccess | xargs rm -v

# php-phpmailer
%{__rm} -r mods/smtp_mail/phpmailer

# php-recaptcha
%{__rm} -r mods/spamhurdles/captcha/recaptcha-php-1.9

# php-json
%{__rm} include/api/json-pear.php

mv include/db/config.php.sample .
mv include/api/examples examples/api
mv docs/example_mods examples/mods
mv portable scripts examples

# move console_upgrade back, it is actually useful
install -d scripts
mv examples/scripts/console_upgrade.php scripts
chmod a+rx scripts/*

# so we don't have to package html/pdf/docbook via docs/*
mv docs/html htmldoc
mv docs/docbook .
mv docs/pdf pdfdoc

# kill old files by phorum
%{__rm} post.php

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

# NOTE when upgrading version:
# no paths should contain ./mods/, ./includes, those should be marked by
# PHORUM_DIR or PHORUM_INCLUDES_DIR constants
# grep -Fr ./mods/ .
# grep -Fr ./includes/ .
# you can rm -rf these dirs to simplify:
# rm -rf htmldoc/ docbook/ docs/ examples/ *.lang

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{_cachedir}}
cp -a *.php htdocs include mods templates scripts $RPM_BUILD_ROOT%{_appdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -p config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/config.php

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
fr french-utf8
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
	echo "%dir %{_appdir}/$mod" >> $file
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

%post admin
%banner -o -e %{name} <<-EOF
Initial Phorum setup is simple as:

1. creating mysql database:
mysqladmin create phorum5
2. granting privs and editing %{_sysconfdir}/config.php
3. opening http://localhost/phorum/admin.php
EOF

# Same as post-scriptlet, runs only on version upgrade
%triggerpostun admin -- %{name}-admin < %{version}-0
# don't do anything on --downgrade
if [ $1 -le 1 ]; then
	exit 0
fi
%{_appdir}/scripts/console_upgrade.php || :

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
%dir %{_appdir}/scripts
%dir %{_appdir}/templates

%dir %{_appdir}/include
%dir %{_appdir}/include/db

# yes, base mysql code in main package as both mysql/mysqli use it
%dir %{_appdir}/include/db/mysql
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

# TODO: check and use external pkg
%dir %{_appdir}/include/javascript
%{_appdir}/include/javascript/jquery-1.4.4.min.js
%{_appdir}/include/javascript/jquery.bgiframe-2.1.2.min.js
%{_appdir}/include/javascript/jquery.json-1.3.min.js
%{_appdir}/include/javascript/phorum-javascript-library.php

%dir %attr(770,root,http) /var/cache/phorum

%{_examplesdir}/%{name}-%{version}

%files admin
%defattr(644,root,root,755)
%{_appdir}/htdocs/admin
%{_appdir}/htdocs/admin.php
%{_appdir}/include/admin
%{_appdir}/include/db/upgrade
%attr(755,root,root) %{_appdir}/scripts/console_upgrade.php

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}

%files db-mysql
%defattr(644,root,root,755)
%{_appdir}/include/db/mysql/mysql.php

%files db-mysqli
%defattr(644,root,root,755)
%{_appdir}/include/db/mysql/mysqli.php
%{_appdir}/include/db/mysql/mysqli_replication.php

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
%{_appdir}/mods/spamhurdles/hurdles
%{_appdir}/mods/spamhurdles/include
%{_appdir}/mods/spamhurdles/spamhurdles.js

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
