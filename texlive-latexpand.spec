%global tl_name latexpand
%global tl_revision 66226

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7.2
Release:	%{tl_revision}.1
Summary:	Expand \input and \include in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latexpand
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexpand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexpand.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latexpand.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Latexpand is a Perl script that simply replaces \input and \include
commands with the content of the input or included file. The script does
not deal with \includeonly commands.

