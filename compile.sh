#!/bin/bash
#######################################################
# Mass Cross-Compile Shell Script, Darkerego 2016     #
# GPL. Do whatever, just be kind and give the credit! #
#######################################################
# Modified by isdrupter
#######################################################
##
## Path of C file
cpath=.
## Target program name
program=ktx
#######################################################
# Download toolchains from here: https://www.uclibc.org/downloads/binaries/0.9.30.1/
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2  
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2  
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2  
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc-440fp.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2 
#https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-x86_64.tar.bz2
## Path to toolchains
toolchainPath="/opt/toolchains"
# Create bin directory if not here
[[ ! -d bin ]] && mkdir bin

## Name of toolchains
#toolchains="cross-compiler-armv4l cross-compiler-m68k cross-compiler-powerpc-440fp cross-compiler-armv5l cross-compiler-mips cross-compiler-sh4 cross-compiler-i586 cross-compiler-mipsel cross-compiler-sparc cross-compiler-i686 cross-compiler-powerpc cross-compiler-x86_64"
## A more exhaustive example toolchain list:
toolchains="cross-compiler-armv4l cross-compiler-armv4tl cross-compiler-armv5l cross-compiler-armv6l cross-compiler-i486 cross-compiler-i586 cross-compiler-i686 cross-compiler-m68k cross-compiler-mips cross-compiler-mips64 cross-compiler-mipsel cross-compiler-powerpc cross-compiler-powerpc-440fp cross-compiler-sh2eb cross-compiler-sh2elf cross-compiler-sh4 cross-compiler-sparc cross-compiler-x86_64"
read -p "I will now remove the old binaries and compile the new, ok (y/n) ?" cleanupYN
if [ $cleanupYN == "y" ];
then
    rm bin/*
else
    echo "Abort." && exit 1
fi

for i in "$toolchains"
do

  target=$(echo $i | sed 's#.*-##')
  cfile=$cpath/"$program".c
  sed "s/xXxXx/$target/" $cfile > temp.c
  out="$(pwd)/bin"
  echo "C file location is $cfile, binary output is $out/$program-$target, Compiling $program for $target...!"
  sleep 0.25  
  
  export PATH=/usr/local/bin:/usr/bin:/bin:$toolchainPath/$i/bin
  "$target"-gcc temp.c -static -o $out/$program-$target && echo "$target compiled!" && file $out/$program-$target;rm temp.c

done

exit 0
