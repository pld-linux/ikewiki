%define		_snap	2006-03-31
%define		_ver %(echo %{_snap} | tr -d -)
Summary:	IkeWiki - a Semantic Wiki
Summary(pl):	IkeWiki - semantyczne wiki
Name:		ikewiki
Version:	0.0.%{_ver}
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/ikewiki/%{name}-snapshot.%{_snap}-src.tar.gz
# Source0-md5:	198748e2a801487cb73074d369633256
URL:		http://ikewiki.salzburgresearch.at/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	ant
Requires:	webapps
Requires:	jre >= 1.5.0
Requires:	tomcat >= 5.5.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
IkeWiki is a special kind of Wiki (a "Semantic Wiki") that allows
users to annotate their pages using Semantic Web standards like RDF(S)
or OWL. It is easy to use and suitable as a tool for "knowledge
engineering".

%description -l pl
IkeWiki to specjalny rodzaj Wiki ("Semantyczne Wiki") pozwalaj±cy
u¿ytkownikom dodawaæ do stron obja¶nienia przy u¿yciu standardów
Semantic Web takich jak RDF(S) czy OWL. Jest ³atwe w u¿yciu i
odpowiednie jako narzêdzie do "in¿ynierii wiedzy".

%prep
%setup -q -n %{name}-snapshot.%{_snap}

%build
ant dist-bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a IkeWiki.war $tomcat/webapps/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
