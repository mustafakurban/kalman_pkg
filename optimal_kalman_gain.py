import numpy as np



class optimal_kalman_gain():
	def __init__(self):
		self.K_sub_k = None


	def execute_model(self,H_matrix,P_sub_k_to_minus_1,S_sub_k):

		self.K_sub_k = P_sub_k_to_minus_1 @ H_matrix.T @ np.linalg.pinv(S_sub_k)