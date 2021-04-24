import numpy as np
from field import rep_field
from field import att_field
from field import guassian

def create_map(mx,my,X,Y,SIGMA_X,SIGMA_Y,TYPE):
	n = len(X)
	Map = np.zeros((mx,my,3))
	for i in range(n):
		if(TYPE[i] == 0):
			Map[:,:,2] += rep_field(X[i],Y[i],SIGMA_X[i],SIGMA_Y[i],mx,my)
		elif(TYPE[i] == 2):
			Map[:,:,2] += att_field(X[i],Y[i],mx,my);
	return Map
	
def filter_map(mx,my,X,Y,SIGMA_X,SIGMA_Y,TYPE):
	n = len(X)
	Map = np.zeros((mx,my,3))
	for i in range(n):
		if(TYPE[i] == 0):
			Map[:,:,2] += 2*rep_field(X[i],Y[i],SIGMA_X[i],SIGMA_Y[i],mx,my)
	return Map

