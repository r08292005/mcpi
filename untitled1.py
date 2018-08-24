# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:12:14 2018

@author: NTPU
"""

from random import choice
from mcpi.minecraft import Minecraft
NTPU=Minecraft.create()

block=[14,15,16,56,73,129]

r = choice(block)
myID = NTPU.getPiayerEntityId("Ryanshen94")
x,y,z=NTPU.entity,getTikePos(myID)