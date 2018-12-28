import numpy as np

#######################################################################
###                  Constructing Global Matrices                  ####
#######################################################################

def local2global(Me,Mg,gll_connect,el_no):
    """Takes in an element matrix and global matrix as input 
    and returns the modified global matrix.
    Me = Element matrix.
    Mg = Global matrix.
    gll_connect = Containing the GLL connectivities and used for array conversion
    el_no = Index of the element whose Me is being sent to add into Mg."""

    Mg_new = np.zeros(np.shape(Mg))	#Initializing empty array for storing the elements to be added to Mg

    #el_no could also be a list of element indices but then Me would also have another dimension.
    #For now we are using el_no as a single integer.
    for e in np.array(el_no):	
        for i in range(len(Me)):
            for j in range(len(Me[i,:])):
                Mg_new[gll_connect[e,i],gll_connect[e,j]] += Me[i,j]

    return Mg_new	#returning array with entries from the Element Matrix inserted at correct places
                        #to be added to the global matrix at the point where this function has been called.


