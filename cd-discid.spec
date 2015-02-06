Name:		cd-discid
Version:	1.3
Release:	2
Summary:	Utility to get CDDB discid information
Group:		File tools
License:	GPLv2+
URL:		https://github.com/taem/cd-discid
Source0:	http://linukz.org/download/%{name}-%{version}.tar.gz

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc.  It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.

%prep
%setup -q -n taem-%{name}-157505f

%build
%make

%install
%makeinstall_std

%files
%doc changelog COPYING README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*


%changelog
* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.3-1
+ Revision: 732041
- imported package cd-discid

