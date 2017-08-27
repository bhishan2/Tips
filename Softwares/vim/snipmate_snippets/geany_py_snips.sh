name=if __name__ == '__main__':\n    main()
box=#\n# ==============================================================================\n#            %cursor%\n#\n# ==============================================================================\n#\n
if=if %cursor%:\n
else=else:\n    %cursor%
elif=elif %cursor%:\n
try=try:\n    %cursor%\nexcept Exception, e:\n
for=for i in range(%cursor%):
# function
def=def %cursor%():\n    """%cursor%."""\n    %cursor%
def2=def f():\n    '''\n# Depends :\n#\n# Outputs :\n#\n# Returns :\n#\n# Info:\n# 1.\n#\n    '''\n\n    pass\n\n\n
doc=""" %cursor% """
doc2='''\n# Depends :\n#\n# Outputs :\n#\n# Returns :\n#\n# Info:\n# 1.\n#\n    '''
# class
class=class %cursor%(object):\n    """ Class doc """\n    \n    def __init__ (self):\n        """ Class initialiser """\n            pass
.=self.%cursor%
# main
main=def main():\n    %cursor%
maint=##==============================================================================\n## Main program\n##==============================================================================\nif __name__ == '__main__':\n    # Beginning time\n    begin_time,begin_ctime = time.time(), time.ctime()\n\n    # Run main program\n    main()\n\n    # Print the time taken\n    end_time,end_ctime  = time.time(), time.ctime()\n    seconds             = end_time - begin_time\n    m, s                = divmod(seconds, 60)\n    h, m                = divmod(m, 60)\n    d, h                = divmod(h, 24)\n    print('\\nBegin time: ', begin_ctime,'\\nEnd   time: ', end_ctime,'\\n' )\n    print("Time taken: {0:.0f} days, {1:.0f} hours, \\\n          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))\n
# head
h=#!/usr/local/bin/env python3\n# -*- coding: utf-8 -*-\n#\n# Author      : Bhishan Poudel, Physics PhD Student, Ohio University\n# Date        : {date}\n# Last update :\n#\n# Imports\n\ndef main():\n    """Main Module."""\n\n    %cursor%\n\nif __name__ == '__main__':\n    main()\n
## imports
time=import time
impall=import numpy as np\nimport pandas as pd\nimport time
implt=import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport time
imppar=import multiprocessing as mp\nfrom joblib import Parallel,delayed\n\n
mp=import multiprocessing as mp
np=import numpy as np
pd=import pandas as pd
df=from pandas import DataFrame as DF
plt=import matplotlib.pyplot as plt
sp=import scipy as sp
nat=natsort.natsorted(%cursor%)
impnat=import natsort
#ap=import astropy.io
#fits=from astropy.io import fits
#getheader=from astropy.io.fits import getheader
#getval=from astropy.io.fits import getval
#getdata=from astropy.io.fits import getdata
# prints
pr=print(%cursor%)
prr=print('%cursor% = ', %cursor%)
rp=print(%cursor%)
pra=print(a)
prb=print(b)
prc=print(c)
prd=print(pd.DataFrame(%cursor%))
prdf=print(DF(%cursor%))
prdfh=print(df.head())
prf=print('%cursor% = %.0f'%(%cursor%))
prff=print('{} {} {}'.format('%cursor%','', ''))
prn=print("\\n")
prnn=print("\\n")\nprint(%cursor%)
prr=print("\\n")\nprint(r"%cursor%")\nprint(%cursor%)\n
prnn=print("\\n")
# numpy
arange=np.arange(%cursor%,%cursor%,step =%cursor%)
arange2=np.arange(1000,2000,step =1)\ny = np.arange(1e-5,1e-5*1000+1e-5,step =1e-5)\n
linspace=np.linspace(%cursor%,%cursor%,num=%cursor%,endpoint=True)
# file read/write
fileread=infile = '%cursor%'\nx = np.genfromtxt(infile,delimiter=None,usecols=(0),dtype=float,unpack=True)\ny = np.genfromtxt(infile,delimiter=None,usecols=(1),dtype=str,unpack=True)\nprint('{} {} {} {}'.format('\\nFirst row    : ', x[0], y[0],'\\n ' ))\n
fileread2=##=============================================================================\n# read in a file\ninfile = '%cursor%'\nprint('{} {} {} {}'.format('\\nreading file : ', infile, ' ',' ' ))\nx = np.genfromtxt(infile,delimiter=None,usecols=(0),dtype=str,unpack=True)\ny,z = np.genfromtxt(infile,delimiter=None,usecols=(1,2),dtype=float,unpack=True)\nprint('{} {} {} {}'.format('First row    : ', x[0], ' ','\\n ' ))\n##=============================================================================
fileread3=# read in a file\ninfile = '%cursor%'\nf=open(infile,'r')\nk=0\ncol0=[]\ncol1=[]\nfor line in f:\n   if not line.startswith("#"):\n    row=line.split()\n    col0.append(float(row[0]))\n    col1.append(float(row[1]))\n    k = k+1\nf.close()
filereadpd=infile = '%cursor%'\ncolnames = ['c0', 'c1']\ndf = pd.read_csv(infile,sep='\\s+', header = None,skiprows = 0,\n                 comment='#',names=colnames,usecols=(0,1))\n
filewrite=np.savetxt('%cursor%.txt', np.array([x,y]).T,\n           delimiter=' ', comments='',\n           fmt=['%-7d', '%.7f'],\n           header='%-7s %+4s'%('x','y'))\n
filewrite2=outfile = '%cursor%.csv'\nprint('Creating : ', outfile)\nwith open(outfile,'w') as f:\n\n    # write header\n    header = '# x  y '\n    print(header,file=f)\n\n    # write data\n    for i in range(len(x)):\n        print(x[i],y[i],sep='   ', file=f)\n
filewrite3=mydata = '\\n'.join('\\t'.join(map(str,row)) for row in zip(x,y))\nwith open('%cursor%.csv', 'w') as fo:\n    print(mydata, file=fo)
filewritepd=outfile = '%cursor%.csv'\ndf.to_csv(outfile,index=None,header=None,sep='\\t')
# plots
plotall=#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# Author  : Bhishan Poudel\n# Date    : {date}\n\n# Imports\nimport matplotlib.pyplot as plt\nimport numpy as np\n\n\n# data\nx = np.arange(0,10,1)\ny = np.exp(x)\n\n# subplots\nfig, ax = plt.subplots()\nplt.plot(x,y,color='k',linestyle="--")\n\n# title and axes labels\nplt.title('title')\nplt.xlabel('xlabel', fontsize=10)\nplt.ylabel('ylabel', fontsize=10)\n\n# axes limit\nplt.xlim(0,6)\nplt.ylim(0,1000)\n\n# text marker\ntxt = r'$\mu=100,\  \\sigma=15$'\nplt.text(4, 500, txt)\n\n# major ticks\nplt.xticks(np.arange(min(x), max(x)+1, 2))\nplt.yticks(np.arange(0, 1000+0.001, 200))\n\n# minor ticks\nx_minor_ticks = np.arange(min(x), max(x)+1, 1 )\ny_minor_ticks = np.arange(0, 1000+0.001, 100)\nax.set_xticks(x_minor_ticks, minor=True)\nax.set_yticks(y_minor_ticks, minor=True)\n\n# grid\nplt.grid(False)\n\n# save and show plot\n#plt.savefig("fig1.png",dpi = 200, height = 14, width = 14)\nplt.show()
plotfileall=#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# Author  : Bhishan Poudel\n# Date    : May 23, 2016\n\n# Imports\nimport numpy as np\nimport matplotlib.pyplot as plt\n\ninfile = 'bhishan.txt'\ncol0,col1 = np.loadtxt(infile, comments="#", skiprows=0, usecols=(0,1), unpack=True)\nplt.plot(col0, col1)\nplt.xlabel('x')\nplt.ylabel('y')\nplt.title('Title')\nplt.show()
subplots=plt.subplot(2, 1, 1)  # rows, columns, and plot number\nplt.plot(x1, y1, 'yo-')\nplt.title('%cursor%')\nplt.ylabel('plot 1')\n\nplt.subplot(2, 1, 2)\nplt.plot(x2, y2, 'r.-')\nplt.xlabel('')\nplt.ylabel('plot 2')\n\nplt.show()
subplotsall=#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\n# Author  : Bhishan Poudel\n# Date    : {date}\n\n\n# Imports\nimport numpy as np\nimport matplotlib.pyplot as plt\n\nx1 = np.linspace(0.0, 5.0)\nx2 = np.linspace(0.0, 2.0)\n\ny1 = np.cos(2 * np.pi * x1) * np.exp(-x1)\ny2 = np.cos(2 * np.pi * x2)\n\nplt.subplot(2, 1, 1)  # rows, columns, and plot number\nplt.plot(x1, y1, 'yo-')\nplt.title('one plot 2 subplots')\nplt.ylabel('plot 1')\n\nplt.subplot(2, 1, 2)\nplt.plot(x2, y2, 'r.-')\nplt.xlabel('time (s)')\nplt.ylabel('plot 2')\n\nplt.show()
# time
now=print('\\nCurrent time: ', time.ctime())
# process
subprocess=commands = " " +\\\n" %cursor% ; " +\\\n"  ; " +\\\n" "\n\n\nprint("\\nRunning commands :\\n", commands, "\\n")\nsubprocess.call(commands,shell=True)\n
call=import subprocess\ncommands = '''\necho a\necho b\n'''\n\nsubprocess.call(commands,shell=True)\n
run_process=def run_process(name, args,):\n    """ Run another program from this program.\n    Example:\n    run_process("Running example.py", ["python3", 'example.py', 'arg1' ])\n\n    """\n    process = subprocess.Popen(args)\n    process.communicate()\n    if process.returncode != 0:\n        print("Error: %s did not terminate correctly. \\\n              Return code: %i."%(name, process.returncode))\n        sys.exit(1)\n
run_process2=import subprocess,time,sys\n\n\n\n##==============================================================================\n# Usage   :Run a process using subprocess.Popen\n# Command : run_process("Running example.py", ["python3", 'example.py', 'arg1' ])\n##==============================================================================\ndef run_process(name, args,):\n    print("-------------------------------------------------")\n    print("Running: %s\\nCommand:"%name)\n    for arg in args:\n        print(arg, end=' ')\n    print("")\n    print("---------------------------------------------------")\n\n    subprogram_start_time = time.time()\n    process = subprocess.Popen(args)\n\n    process.communicate()\n    if process.returncode != 0:\n        print("Error: %s did not terminate correctly. \\\n              Return code: %i."%(name, process.returncode))\n        sys.exit(1)\n\n    # Print time\n    subprogram_end_time = time.time()\n    sec                 = subprogram_end_time - subprogram_start_time\n    m, s                = divmod(sec, 60)\n    h, m                = divmod(m, 60)\n    d, h                = divmod(h, 24)\n    print("\\nTime for'{}' ==> {:2.0f} days, {:2.0f} hr,\\\n         {:2.0f} min, {:f} sec.".format( name, d, h, m, s))\n\n    print("End of command: %s\\nCommand:"%name)\n    print("------------------------------------------------")\n
parallel=from multiprocessing import Process\n\ndef func1():\n    %cursor%\n\ndef func2():\n\ndef func3():\n\ndef func4():\n\ndef runInParallel(*fns):\n  proc = []\n  for fn in fns:\n    p = Process(target=fn)\n    p.start()\n    proc.append(p)\n  for p in proc:\n    p.join()\n\n# Running parallel\nrunInParallel(func1, func2,func3,func4)
parallel2=from joblib import Parallel, delayed\nimport multiprocessing as mp\n\n\n\n# function\ndef my_func(i):\n    return i * i\n\n# run in parallel\nnum_cores = mp.cpu_count()\nargs = range(10)\nresults = Parallel(n_jobs=num_cores)(delayed(my_func)(i) for i in args)\n\n# print\nprint(list(range(10)))\nprint(results)\n
# user defined functions
replace=def replace_outdir(outdir):\n    """Replace a folder."""    \n    if os.path.exists(outdir):\n        print('Replacing folder: %s\\n'%outdir)\n        shutil.rmtree(outdir)\n        os.makedirs(outdir)\n    else:\n        print('Making new folder: %s\\n'%outdir)\n        os.makedirs(outdir)\n\noutdir = '%cursor%'\nreplace_outdir(outdir)
re_search=re.search('(.+?)(\d+)(\.fits$)', line).group(2)
interpolate=# interpolation\nfrom scipy import interpolate\nprint('Interpolating ...\n')\nxnew = np.linspace(%cursor%,,num=)\nynew = interpolate.interp1d(x, y, kind='cubic')(xnew)
# some completions
file_remove=os.remove(outfile) if os.path.exists(outfile) else None\n
roundoff=float(str(round(value, 1)))
loop=# print loop info\nprint("\\n\\n"+'#'*50+"\\n# Running loop: ", i, '\\n'+'#'*50+'\\n\\n')
chunks=[LST[i:i + SIZE] for i in range(0, len(LST), SIZE)]
copy_folder=def copy_folder(frm,to):\n    if os.path.isdir(frm):\n        shutil.rmtree(to)\n    shutil.copytree(frm,to)\n

# For reST format in docstrings
note=.. note::\n\n   %cursor%.
seealso=.. seealso::\n\n   %cursor%.
seealso2=.. seealso::\n   Module :py:mod:`zipfile`\n      Documentation of the :py:mod:`zipfile` standard module.\n\n   `GNU tar manual, Basic Tar Format <http://link>`_\n      Documentation for tar archive files, including GNU tar extensions.\n
warning=.. warning::\n\n   %cursor%.
todo=.. admonition:: todo\n\n   %cursor%
info=.. admonition:: Info\n\n   %cursor%
info=.. admonition:: Readme\n\n   %cursor%
code=.. code-block:: c\n\n    printf("hi there");\n
math=\n.. :math:: %cursor%
mth=\n:math: `alpha`
math2=.. math::\n\n    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k\n
topic=.. topic:: Topic\n\n    Indented text is the body.
params="""%cursor%.\n\nParameters\n----------\narg1 : int\n    %cursor%\narg2 : str\n    %cursor%\n\nReturns\n-------\nNone\n\n"""\n
frac=\frac{%cursor%}{%cursor%}
