##
# This file is part of N.O.D.A.C.
#
# (c) Copyright 2009 N.O.D.A.C. Development Team
#
# N.O.D.A.C. is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License,
# or (at your option) any later version.
#
# N.O.D.A.C. is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# Please refer to the GNU Public License for more details.
#
# You should have received a copy of the GNU Public License along with
# this program; if not, write to:
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
##

from config import *

# Test section #

Net = NeuralNetwork()	
Net.new([
		{'neurons': 2},
		{'neurons': 2, 'activation': 'tanh'}, 
		{'neurons': 1, 'activation': 'tanh'}
		])				
#print "\n\n- read_config test section -"				
#Net.read_config("testnet.xml")
#Net.write_config("out.xml")

print "\n- read_dataset test section -"
Net.read_dataset("dataset.xml")
Net.make_landscape()
