#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-openhtmltopdf-core
Version  : 0.0.1.rc9
Release  : 1
URL      : https://repo1.maven.org/maven2/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9/openhtmltopdf-core-0.0.1-RC9.jar
Source0  : https://repo1.maven.org/maven2/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9/openhtmltopdf-core-0.0.1-RC9.jar
Source1  : https://repo1.maven.org/maven2/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9/openhtmltopdf-core-0.0.1-RC9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: mvn-openhtmltopdf-core-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-openhtmltopdf-core package.
Group: Data

%description data
data components for the mvn-openhtmltopdf-core package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9/openhtmltopdf-core-0.0.1-RC9.jar
/usr/share/java/.m2/repository/com/openhtmltopdf/openhtmltopdf-core/0.0.1-RC9/openhtmltopdf-core-0.0.1-RC9.pom
