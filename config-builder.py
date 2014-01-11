#! /usr/bin/python

# This will generate the kerneltools-build-config needed by the Builder

import fileinput
import sys
import os
import commands

# Getting the Device Spec's

def devicespec():
  a = raw_input('\nCROSS_COMPILE=~/')
  b = raw_input('LOCAL_BUILD_DIR=~/')
  c = raw_input('TARGET_DIR=~/')
  d = raw_input('SYSTEM_PARTITION=/dev/block/mmcblk0p')
  e = raw_input('DEFCONFIG=')
  f = raw_input('N_CORES=')
  g = raw_input('VERSION=')

# Print the Device Spec's

  print '\n=====================================\n'
  print 'CROSS_COMPILE=~/' + a
  print 'HOST_CC=gcc'
  print 'LOCAL_BUILD_DIR=~/' + b 
  print 'TARGET_DIR=~/' + c
  print 'SYSTEM_PARTITION=\"/dev/block/mmcblk0p' + d + '\"'
  print 'DEFCONFIG=' + e
  print "\nFLASH_BOOT='write_raw_image(\"/tmp/boot.img\", \"boot\")'"
  print '\n# ----\n'
  print 'N_CORES=' + f
  print 'VERSION=' + g
  print '\n# ----\n\n'
  print 'BANNER=`cat <<EOF'
  print 'ui_print("**********************************************");'
  print 'ui_print("*                                            *");'
  print 'ui_print("  VERSION: ' + g + '                     ");'
  print 'ui_print("*                                            *");'
  print 'ui_print("**********************************************");'
  print 'EOF`'
  print '\n=====================================\n'

# Generate kerneltools-build-config file
  
  answer1 = raw_input('\nDoes this Look Correct? Y or N? ')
  if answer1 == 'n':
    main()
  else:
    nf = 'kerneltools-build-config'
    outfile = open(nf, 'w')
    outfile.write('CROSS_COMPILE=~/' + a +
                  '\nHOST_CC=gcc' +
                  '\nLOCAL_BUILD_DIR=~/' + b +
                  '\nTARGET_DIR=~/' + c +
                  '\nSYSTEM_PARTITION=\"/dev/block/mmcblk0p' + d + '\"' +
                  '\nDEFCONFIG=' + e +
                  "\n\nFLASH_BOOT='write_raw_image(\"/tmp/boot.img\", \"boot\")'" +
                  '\n\n# ----' +
                  '\n\nN_CORES=' + f +
                  '\nVERSION=' + g +
                  '\n\n# ----\n\n' +
                  'BANNER=`cat <<EOF\n' +
                  'ui_print("**********************************************");\n' +
                  'ui_print("*                                            *");\n' +
                  'ui_print("  VERSION: ' + g + '                     ");\n' +
                  'ui_print("*                                            *");\n' +
                  'ui_print("**********************************************");\n' +
                  'EOF`')
    outfile.close()
    commands.getstatusoutput('mv ' + nf + ' ~/' + b)
    print '\nSaved config file to: ' + '~/' + b + '/' + nf + '\n'

def main():
  devicespec()
  exit()

if __name__ == '__main__':
  main()
