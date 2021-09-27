import numpy as np


class state_space_hub():
	def __init__(self):
		
		#sample time of the simulation
		self.dt = 1.0

		self.x_sub_k_minus_1           = np.array([0.0,0.0,0.0]).T
		self.u_sub_k_minus_1           = np.array([4.5,0.0]).T

		self.F_matrix = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
		self.B_matrix = np.array([[np.cos(self.x_sub_k_minus_1[2]) * self.dt,0.0],[np.sin(self.x_sub_k_minus_1[2]),0.0],[0.0,self.dt]])
		self.state_noise = np.array([0.01,0.01,0.003]).T



class measurement_model_hub():
	def __init__(self):

		self.H_matrix = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
		self.measurement_noise = np.array([0.07,0.07,0.04]).T


class predicted_covariance_hub():
	def __init__(self):
		self.P_sub_k_minus_1_d = np.array([[0.1,0.0,0.0],[0.0,0.1,0.0],[0.0,0.0,0.1]]) 
		self.Q_sub_k = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])

class sensor_hub():
	def __init__(self):
		self.z_sub_k = [4.721,0.143,0.006]



#If we are sure about our sensor measurements, the values along the diagonal of R decrease to zero. 
class rasidual_covariance_hub():
	def __init__(self):
		self.R_sub_k = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])