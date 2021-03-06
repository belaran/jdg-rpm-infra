%define jon_version XXX

%define jon_home XXX

%define username XXX
%define group XXX

Name:	    jdg
Version:	%{jdg_version}
Release:	1%{?dist}
Summary:    Packaging of Red Hat JBoss Data Grid, install required binary files.

Group:      Administration
License:	GPL
URL:        http://access.redhat.com/

Packager:   Romain Pelisse
BuildArch:  noarch

Requires(pre): shadow-utils

%pre
mkdir -p %{jdg_home}
getent group %{group} >/dev/null || groupadd -r %{group}
getent passwd %{username}  >/dev/null || \
    useradd -r -g %{group} -d %{jdg_home} -s /sbin/nologin \
        -c "JBoss Data Grid (JDG) user account" %{username}
exit 0

%post


%clean
exit 0

%description

%files
%defattr(-,%{username},%{group})
%{jdg_home}

%doc


%changelog

