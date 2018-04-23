Name:		texlive-latexpand
Version:	1.41gb32a776
Release:	1
Summary:	Expand \input and \include in a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexpand
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexpand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexpand.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latexpand.bin = %{EVRD}

%description
Latexpand is a Perl script that simply replaces \input and
\include commands with the content of the file input/included.
The script does not deal with \includeonly commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latexpand
%{_texmfdistdir}/scripts/latexpand
%doc %{_texmfdistdir}/doc/support/latexpand

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/latexpand/latexpand latexpand
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
