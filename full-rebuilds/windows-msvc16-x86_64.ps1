# Time this with Measure-Command -Expression { .\conan-ccdc-index\full-rebuilds\windows-msvc16-x86_64.ps1 > .\rebuildall.log 2>&1 }
# in a powershell with administrative access
$WS=Resolve-Path -Path "$($PSScriptRoot)/../.."

# This presumes you have a python virtualenv in citvenv with conan-ccdc-index-tools installed
. "$($WS)\citvenv\Scripts\Activate.ps1"

# choco install -y cmake.install --installargs 'ADD_CMAKE_TO_PATH=System'
# choco install -y python2

Write-Host "If the meson build fails, you may have to enable Developer Mode. See https://github.com/conan-io/conan/issues/10726"
Write-Host "If the inchi build fails, with this error: fatal error RC1015: cannot open include file 'afxres.h'"
Write-Host "You should add the MFC libraries to your visual studio install"

$CONAN_USER="cbantaloukas"
$Env:LOCAL_CONAN_INDEX="$($WS)/conan-ccdc-index"
$Env:LCI_PLATFORM_COMBINATION="native-windows-msvc16-x86_64"
$Env:CONAN_USER_HOME="E:\conan-home-msvc16"

Remove-Item -recurse -force $Env:CONAN_USER_HOME -ErrorAction SilentlyContinue
conan config install "$($WS)/conan-ccdc-common-configuration"

conan user --remote ccdc-3rdparty-conan-testing --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-center --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-bincrafters --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER


cit publish recipe


cd csd-database-proto
conan export . csdprotobufs/1.0.193.1@
cd ..
cd data-standards-cql
conan export . cqlprotobufs/1.0.103.1@
cd ..
cd conan-installbuilder-licence
conan export . installbuilder-licence/2021.7.26@
cd ..


cit build


conan install csdprotobufs/1.0.193.1@ --profile:build build-on-windows-msvc16-x86_64 --profile:host windows-msvc16-x86_64-release --build=csdprotobufs -s build_type=Release
conan install csdprotobufs/1.0.193.1@ --profile:build build-on-windows-msvc16-x86_64 --profile:host windows-msvc16-x86_64-release --build=csdprotobufs -s build_type=Debug
conan install cqlprotobufs/1.0.103.1@ --profile:build build-on-windows-msvc16-x86_64 --profile:host windows-msvc16-x86_64-release --build=cqlprotobufs -s build_type=Release
conan install cqlprotobufs/1.0.103.1@ --profile:build build-on-windows-msvc16-x86_64 --profile:host windows-msvc16-x86_64-release --build=cqlprotobufs -s build_type=Debug
conan install installbuilder-licence/2021.7.26@ --profile:build build-on-windows-msvc16-x86_64 --profile:host windows-msvc16-x86_64-release --build=installbuilder-licence

conan upload --all --parallel --remote ccdc-3rdparty-conan-testing '*' --confirm
