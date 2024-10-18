#--------------------------------------------------------------------------
# Plot symbol's recordings from Panda Co-Manipulation Dataset
#
# Written by Giovanni Braglia, 2024
# University of Modena and Reggio Emilia
# 
# tested on Python 3.10.12
#--------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


symbol_data = np.load( "Panda_CoManipulation_Data/04/symbol_data.npy", allow_pickle=True )
Ts = 0.001 # Sampling-time of recordings

plt.figure( figsize=(8,6) )
for i in range(6):
    L = symbol_data[i]['pos'].shape[1]
    T = Ts*L
    t = np.linspace( 0, T, L )
    label = 'Rec'+str(i)
    # Plot 2D symbol
    ax0 = plt.subplot(1,2,1)
    plt.plot( symbol_data[i]['pos'][0,:], symbol_data[i]['pos'][1,:], linewidth=2, label=label )
    # Plot x velocity
    ax1 = plt.subplot(2,2,2)
    plt.plot( t, symbol_data[i]['vel'][0,:], linewidth=2 )
    # Plot y velocity
    ax2 = plt.subplot(2,2,4)
    plt.plot( t, symbol_data[i]['vel'][1,:], linewidth=2 )


#------------------ 
ax0.legend() 
ax0.grid()
ax0.set_xlim([-0.6,-0.35])
ax0.set_ylim([-0.45,-0.15])
ax0.set_xlabel(r'$x$[m]', fontsize=14 )
ax0.set_ylabel(r'$y$[m]', fontsize=14 )

#------------------
ax1.grid()
ax1.set_xlabel(r'$t$[s]', fontsize=14 )
ax1.set_ylabel(r'$\dot{x}$[m/s]', fontsize=14 )

#------------------
ax2.grid()
ax2.set_xlabel(r'$t$[s]', fontsize=14 )
ax2.set_ylabel(r'$\dot{y}$[m/s]', fontsize=14 )

plt.tight_layout()
plt.show()
