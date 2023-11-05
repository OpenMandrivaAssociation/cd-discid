%define _empty_manifest_terminate_build 0

Name:		cd-discid
Version:	1.4
Release:	1
Summary:	Utility to get CDDB discid information
Group:		File tools
License:	GPLv2+
URL:		https://github.com/taem/cd-discid
Source0:  https://github.com/taem/cd-discid/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
#Source0:	http://linukz.org/download/%{name}-%{version}.tar.gz
Patch0:  fix-install-dir-openmandriva.patch

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
#{_bindir}/cd-discid
#{_mandir}/man1/cd-discid.1*


%changelog
* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.3-1
+ Revision: 732041
- imported package cd-discid

