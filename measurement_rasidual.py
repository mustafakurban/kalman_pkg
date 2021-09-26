"""
State estimation with kalman filter


author: Mustafa KURBAN (@mustafakurban)
"""

import numpy as np
import configuration



class measurement_rasidual():
	def __init__(self):
		veriables = configuration.sensor_hub()
		self.z_sub_k = veriables.z_sub_k
		self.predicted_y_sub_k = None


	def execute_model(self,h_sub_k):
		self.predicted_y_sub_k = self.z_sub_k - h_sub_k
