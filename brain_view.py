def flatmaps(sub,roi):
	import sys
	sys.path.append("/usr/local/lib/python2.7/dist-packages")
	sys.path.append('/usr/lib/python2.7/site-packages')
	import cortex
	import h5py
	from cortex import webgl
	import numpy as np
	from cortex import quickflat
	import time
	import os
	import scipy.io as sio
	#shano mota alu
	#subjects={'AH','DS','JG','ML','WH'}   
	file=sio.loadmat('/auto/data/salman/data/{0}_flatmap.mat'.format(sub))
	data=file['data']
	data=np.array(data)
	h=webgl.show((data,'{0}fs'.format(sub),'{0}fs_nb'.format(sub)))
        #h=webgl.show((data,'{0}fs'.format(sub),'{0}fs_nb'.format(sub)),vmin=-0.3,vmax=0.3)
        #h.setColormap('bwr_r')
        #time.sleep(8)
        #h.get_view('{0}fs'.format(sub),'{0}_para'.format(sub))
       # h.saveIMG('/auto/data/oyilmaz/story_stimulus_methods/{0}{1}.png'.format(sub,method),(1920,1080))
	#time.sleep(2)        
	#os.system("killall firefox")
	return



