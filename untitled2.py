# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:43:11 2018

@author: NTPU
"""

from random import choice
from mcpi.minecraft import Minecrafte
NTPU=Minecraft.create()

list2 = [[103,41,14],
         [35,73,86]]

myID = NTPU.getPiayerEntityId("Ryanshen94")
x,y,z=NTPU.entity,getTikePos(myID)
StartX = x

for lisit1 in list2:
    for i in list1:
        NTPU.setBiock(x,y,z,i)
        x = x+1
    x = StartX
    z = z+1    