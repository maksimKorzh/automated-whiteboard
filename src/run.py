####################################
#
#      Use this script to run
#  automated whiteboard animation
#
####################################

# packages
import multiprocessing
import os

# python command
PYTHON = 'python3'

# create animation frames
print('Processing frames...', end=' ')
os.system(PYTHON + ' frames.py')
print('done')

# Creating the tuple of all the processes
animation_processes = ('whiteboard.py', 'animate.py')                                    
                                                  
# This block of code enables us to call the script from command line.                                                                                
def execute(process): os.system(PYTHON + f' {process}')
                                                                                
# create process pool                                                                                
process_pool = multiprocessing.Pool(processes = 2)                                                        

# run animation
print('Started animation')
process_pool.map(execute, animation_processes)
print('Animation is finished')

