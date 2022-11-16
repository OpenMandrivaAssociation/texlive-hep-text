Name:		texlive-hep-text
Version:	64906
Release:	1
Summary:	List and text extensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-text
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-text.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-text.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-text.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-text package extends LaTeX lists using the enumitem
package and provides some text macros. The package is loaded
with \usepackage{hep-text}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-text
%{_texmfdistdir}/tex/latex/hep-text
%doc %{_texmfdistdir}/doc/latex/hep-text

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
