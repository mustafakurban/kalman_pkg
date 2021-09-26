import numpy
import time
import configuration


class predicted_covariance():
	def __init__(self):
		"""
		The P matrix has variances on the diagonal and covariances on the off-diagonal. 
		"""

		self.P_sub_k_to_minus_1 = None
		veriables = configuration.predicted_covariance_hub()

		self.Q_sub_k = veriables.Q_sub_k 
		self.P_sub_k_minus_1_d = veriables.P_sub_k_minus_1_d


	def execute_model(self,F_matrix,):

		self.P_sub_k_to_minus_1 = F_matrix @ self.P_sub_k_minus_1_d @ F_matrix.T + self.Q_sub_k 

