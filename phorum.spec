Summary:	Phorum is a web based message board written in PHP
Summary(pl):	Phorum - implementacja forum WWW w PHP
Name:		phorum
Version:	3.4.4
Release:	1
License:	Apache-like
Group:		Applications
Source0:	http://phorum.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	d64dbe39ce95fabfa1f17120a9de4e53
URL:		http://phorum.org/
Requires:       webserver
Requires:	php >= 4.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phorumdir	/home/services/httpd/html/phorum

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phorumdir}

cp -a . $RPM_BUILD_ROOT%{_phorumdir}
rm -rf $RPM_BUILD_ROOT%{_phorumdir}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,http,755)
%doc docs/*
%dir %{_phorumdir}
%{_phorumdir}/*.php
%{_phorumdir}/*.css
%{_phorumdir}/db
%{_phorumdir}/images
%{_phorumdir}/include
%{_phorumdir}/lang
%{_phorumdir}/plugin
%{_phorumdir}/scripts
%{_phorumdir}/smileys
%dir %{_phorumdir}/admin
%{_phorumdir}/admin/*.php
%{_phorumdir}/admin/actions
%{_phorumdir}/admin/lang
%{_phorumdir}/admin/pages
%dir %attr(770,root,http) %{_phorumdir}/admin/settings
%attr(660,root,http) %config(noreplace) %verify(not size mtime md5) %{_phorumdir}/admin/settings/forums.php
