Rerunning experiments using version 2.0 of the code.
Exploring the effect of symmetry in h-vectors on the resulting dual f-vectors.

For all experiments I did the following:
 1. Create an h-vector with obvious symmetry (e.g., all 1's)
 2. Compute the dual f-vector of the h-vector
 3. Cone the resulting f-vector zero or more times
 4. Run the resulting bit pattern through the NIST test suite

There are three sets of experiments:
 - Fix the h-vector length at 3751, with a pattern of all 1's, and vary the number of conings from 0 to 99 times. 
   '-p 3751 -f -c 0 -b' through '-p 3751 -f -c 99 -b'
 - Vary the h-vector length from 3750 to 3849, with a pattern of all 1's, and don't cone it at all. 
   '-p 3750 -f -b' through '-p 3849 -f -b'
 - Fix the h-vector length at 3750, vary non-end elements in the pattern from 1 to 100, and don't cone it at all. 
   '-p 3750 -i 1 -f -b' through '-p 3750 -i 100 -f -b'
