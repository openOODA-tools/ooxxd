Name:           ooxxd
Version:        0.1.0
Release:        1%{?dist}
Summary:        Generates and reverses hexadecimal binary representations to and from raw files.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooxxd
Source0:        ooxxd-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooxxd is a sovereign, capability-bounded HEX REVERSER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooxxd
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooxxd-uninstall

%files
/usr/bin/ooxxd
/usr/bin/ooxxd-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
