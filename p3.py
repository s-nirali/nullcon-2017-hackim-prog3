import subprocess

def runCmd(cmds):
    p = subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()
    return output, err

def rename(old, new):
    o,e = runCmd('mv '+old+' '+new)
    return new

cond = True
count = 0

while cond == True:

    print "\n\n----------------------------------------------------------------"
    count += 1
    print count

    o,e = runCmd('ls 26685*')
    existingfile = o[:-1]   # o = file, has terminal '\n' char
    print existingfile
    newfile = existingfile+'_t' # just giving a temporary name

    newfile = rename(existingfile, newfile)
    o,e = runCmd('wc -c '+newfile)  # character count = size of file in bytes
    size = o.split()[0]
    print  size+' bytes'

    o,e = runCmd('file '+newfile)
    print o

    if 'LZMA' in o:
        newfile = rename(newfile, newfile+'.lzma')
        o,e = runCmd('unlzma '+newfile)
        print o

    elif 'XZ' in o:
        newfile = rename(newfile, newfile+'.xz')
        o,e = runCmd('unxz '+newfile)
        print o

    elif 'gzip' in o:
        newfile = rename(newfile, newfile+'.gz')
        o,e = runCmd('gzip -d '+newfile)
        print o

    elif 'ZPAQ' in o:
        newfile = rename(newfile, newfile+'.zpaq')
        o,e = runCmd('zpaq x '+newfile)
        print o

    elif 'lzip' in o:
        o,e = runCmd('lzip -d '+newfile)
        print o

    elif 'POSIX tar' in o:
        o,e = runCmd('tar xvf '+newfile+' -v')
        print o

    elif 'bzip2 compressed data, block size = 900k' in o:
        o,e = runCmd('bzip2 -d '+newfile)
        print o

    elif 'NuFile' in o:
        o,e = runCmd('nulib2 -x '+newfile)
        print o

    elif 'Zip' in o or 'ARJ' in o or '7-zip' in o or 'Zoo' in o:
        o,e = runCmd('unar '+newfile)
        print o

    else:
        cond = False

    if cond == True:
        o,e = runCmd('ls 26685*')
        print o
        o,e = runCmd('rm -rf '+newfile)
        # delete existing file - when a file is unarchived, either a newfile is created or existing file is renamed, so deleting the old file avoids confusion
