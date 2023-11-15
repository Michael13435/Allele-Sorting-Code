# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:14:25 2021

@author: Michael Shadoff
"""

import pandas as pd

from pandas import DataFrame





"""This code assists in compiling
raw genome data into a series of files that include all alleles 
passing the stutter threshold at a locus. This
version of the code was checked against the 185 AFA samples processed in the
paper"""


import os

"""The below variable is the input directory, which idealy should contain all
 the genome data. This data must be in .xlsx format and all the data, including 
 the column index if one should exist, must be moved down one row."""




drct7 = str(input("Copy and paste in the input directory:"))

lst = os.listdir(drct7)

"""This variable is the output directory. This directory should contain a folder for
each locus you are looking for, named appropriately. It is very important the folder name
matches the locus name used in the input data exactly. For example if searching for
locus August_7, write August_7 as the name of the file that will contain all data
pertinent to said locus."""

gdrct7 = str(input("Copy and paste the output directory:"))





glst = os.listdir(gdrct7)


"""Two other variables may need to be altered if the input data was not collated
using STRait Razor. If you would like to modify the code to work with outputs
with slightly different formatting please view the paragraph below.

The program looks for MarkerName to avoid taking the Strand Bias Reporting section of the data. If
necessary you can change this string, on line 188, to the title of the Bias Reporting
section. Additionally, the program looks at column 5 for significant data.
If the significant data points are not in column 5, enter the number of the 
column-1 in place of the 4 in the string Unnamed: 4 on line 233. I have
refrained from creating user input variables for these 2 instances to avoid
additional confusion on the part of the user. 

Thank you for viewing my code,it is greatly appreaciated!"""


sttr= float(input("Please enter the inverse of your stutter threshold percentage represented as a decimal:"))


"""The below for loop opens the file in the input directory by making a list of files
and then concatenating it together with the directory name"""

for filex in lst:




        
    ext7 = '\_'
    
    nm7 = filex
    
    
    ext7 = ext7.replace('_' , nm7)
    
    
    fln7 = drct7 + ext7
    
    
    
    iv = nm7
    
    fg = pd.read_excel(fln7)

    
    """This next loop opens the output file using the same method, this prevents
    overwrites, as well it loads in the name of the file which is used to
    identify the locus. This loop continues for each file in the output directory
    so all the data from one file will be read before mocing on to the next"""


    
    
    for flx2 in glst:
        
        ext8 ='\_'
        
        nm8 = flx2
        
        ext8 = ext8.replace('_', nm8)
        
        fln8 = gdrct7 + ext8
        
        
        EF1 = pd.read_excel(fln8)
        
        
        bs = flx2.split('.')[0]
    
        
    
        
    
        
        
        
    
    
        h = len(EF1)-1

    
    
    
    
    
    
        
    
    
        a= 0
        
        b= 0
        c = 0
        i = 0
        gl =[]
        gg = fg.shape
        
        gs = gg[0]
        
        x2=-1
        x3=-1
        
    
        
        
        
        
        
        
    
     
        
        
        
    
        
        s=100000000000000000
        
        
        """This while loop is the bulk of the code, it runs while i is 
        less than the length of the spreadsheet to ensure it reads every cell.
        It checks the cell name for the first column to find the gene based
        off the name of the corresponding output file. Then it uses indexing
        values c and s for start and end respectively to find where the gene is.
        s is set to some arbitrarily high value such that the program would crash
        due to pythons limit of reading 1000000 line excel sheets before s
        would be exceeded. This way whatever the first number is it will be
        less than s, but each subsequent number will not."""
        
        while int(i) < int(len(fg)):
            
            
            
            
            if i > 0:
                fgstr1 = str(fg.iloc[i-1, 0])
            if i > 1:
                fgstr0 = str(fg.iloc[i-2, 0])
            fgstr = str(fg.iloc[i,0])
            
            
            fgstr2 = fgstr.split(':')[0]
            
            
            
            bl = len(fgstr2)
            
            
            
            
            

            fgstr3 = str(fg.iloc[i+1,0])
            

            
            
            if fgstr[0:10] == 'MarkerName':
                
                
            
                break
            
            
            


            
            
            if fgstr[0:bl] == str(bs):
                
                c = i+1
    

                    
                if i<s:
                    s = i
                    if i > 0:
                        if fgstr1[0:bl] == fgstr[0:bl]:
                            s = i-1
            
            
            """An important note here is that the program stops reading for a 
            locus after it successfully finds, and subsequently fails to find 
            the given locus. This is so that the program stops when a section
            of data stops, without this it would read the bias reports. However,
            it means the program will fail if the data for a single locus is not 
            uniformly lumped together. This feature also helps save time, as
            it stops the program from reading the rest of the file, once it stops
            reading loci. This also means that theoretically, 2 files of 5000 lines
            should preform faster than one file of 10000 lines, which I state 
            in case the reader may have some use for said information."""
            
            if s != 100000000000000000 and  fgstr[0:bl] != str(bs):
                
                
                
                break

            

            
            
            i = i+1
            
            
            
            
            
            
        """If s is still the same arbitrarily high constant, the program found
        nothing so it goes on to the next locus"""
        if s == 100000000000000000:
  
            
            continue    
            
        
        """Extracts column of backwards reads as a list, and narrows said list
        to the area of the given locus"""
        
        fg3 = fg['Unnamed: 4'].tolist()
        
    
        
        fg4 = fg3[s:c]
        
      
        
        

        
        
        
        
        
       
        j=0
        k=0
        
        
        
        """If the list somehow comes up empty due to strange formatting like a
        file having no data except the bias report this prevents crashes."""
        if str(fg4[0]) == 'nan':
            
            continue
        
        
        """This part finds the largest element in a list for the stutter
        calculation"""
        for x in fg4:
            
            if x>x2:
                xi = j
                
                xg = x
                x2=x
            j=j+1
            
        
        
        
        fg4.remove(xg)
        
        
        
        
            
        
        if len(fg4) > 0:
        
              
            """This part accounts for the shift in the length of the list
            caused by removing xg. Then xi and xi2 track the position of our
            significant data relative to their original points on the spreadsheet
            so the entire row can be retreived later."""
        
            for x in fg4:
            
                if x>x3:
                    
                    if j<=k:
                        xi2 = k+2
                        
                        
                        
                    elif j>k:
                        xi2 = k+1
                        
                    xg2 = x
                    x3=x
                k=k+1
            
            
                
            fg4.remove(xg2)
            
            
            if xi2 == xi:
                xi2 = xi2 -1
            

        
                
            
            
            """This line is the stutter threshold, where 7 is the inverse
            of the stutter threshold percentage as a decimal."""
                
            if sttr*xg2 > xg:
        
                
                
        
                fgg2=fg.iloc[xi2+s]
                
                
                                    
                                    
                sfg2= fgg2.reset_index(drop = True)
                                    
                                    
                                    
                lsfg2 = sfg2.tolist()
                lsfg2[5] = iv
                tlsfg2 = pd.DataFrame(lsfg2).T
                                    
                                    
                                    
                                    
                fggd2 = sfg2.to_frame()
                                    
                                    
                                   
                tfgg2 = fggd2.transpose()
                                    
                                    
                        
                EF1 = EF1.append(tlsfg2)   
            
                        
            
        """If both values are significant both are appended to EF1 which is
        then saved to the output file. The extra commands are to ensure proper
        formatting."""
            
    
                       
        fgg=fg.iloc[xi+s]
                            
                            
                            
                            
                            
                            
        sfg= fgg.reset_index(drop = True)
                            
        lsfg = sfg.tolist()
                            
        lsfg[5] = iv
                            
        tlsfg = pd.DataFrame(lsfg).T
                            
        fggd = sfg.to_frame()
                            
                            
                           
        tfgg = fggd.transpose()
                            
                            
                    
        EF1 = EF1.append(tlsfg)
                    
        
                    

        EF1.to_excel((fln8))
    
            
        print(filex)


"""This is a quick piece of code that cleans up the output by removing a junk
output leftover by the program, this additional output doesn't interfere with
 the rest of the data, assuming everything is properly formatted, so it can
 be removed."""

for filen9 in glst:
    
    
    ext = '\_'
    
    

    ext = ext.replace('_' , filen9)
    
    j = gdrct7 + ext
    
    
    
    file = pd.read_excel(j)


    
    
    p1 = file.iloc[:,1:7]


    
    p1.to_excel(j)
        
        

    
    
    

