"""
State estimation with kalman filter


author: Mustafa KURBAN (@mustafakurban)

"""

import numpy as np
import configuration


class rasidual_covariance():
	def __init__(self):


		self.S_sub_k = None
		veriables = configuration.rasidual_covariance_hub()

		self.R_sub_k = veriables.R_sub_k


	def execute_model(self,H_matrix,P_sub_k_to_minus_1):

		self.S_sub_k = (H_matrix @ P_sub_k_to_minus_1 @ H_matrix.T) + self.R_sub_k