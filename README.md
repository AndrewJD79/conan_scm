Conan scm attribute doesn't work on windows drive created by subst.exe command:

1. Create folder c:\temp & cd temp
2. git clone https://github.com/AndrewJD79/conan_scm.git
3. cd conan_scm
4. conan source . --source-folder=tmp\source # success
5. subst Z: c:\temp 
6. cd Z:\conan_scm 
7. conan source . --source-folder=tmp\source # failure