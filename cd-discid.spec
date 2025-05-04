%global debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		cd-discid
Version:	1.4
Release:	2
Summary:	Utility to get CDDB discid information
Group:		File tools
License:	GPLv2+
URL:		https://github.com/taem/cd-discid
Source0:	https://github.com/taem/cd-discid/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
#Source0:	http://linukz.org/download/%%{name}-%%{version}.tar.gz
Patch0:		fix-install-dir-openmandriva.patch
# Fix MusicBrainz TOC compute per current specs - https://github.com/taem/cd-discid/pull/6
Patch1:		https://github.com/taem/cd-discid/pull/6/commits/3af2cc90365bf9695e5c5ae2082042397027a060.patch

BuildRequires:	make

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc. It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%doc changelog COPYING README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*

