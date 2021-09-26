"""
State estimation with kalman filter


author: Mustafa KURBAN (@mustafakurban)
"""

import numpy as np
import configuration


class measurement_model():
	def __init__(self):
		veriables = configuration.measurement_model_hub()
		self.H_matrix = veriables.H_matrix
		self.measurement_noise = veriables.measurement_noise
		self.y_sub_k = None

	def execute_model(self,state_vetor):
		self.y_sub_k = self.H_matrix @ state_vetor + self.measurement_noise
         

	def update_parameters(self):
		pass