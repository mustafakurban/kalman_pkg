import numpy
import time
import measurement_model
import state_space_model
import predicted_covariance
import measurement_rasidual
import rasidual_covariance
import optimal_kalman_gain

class main():
	def __init__(self):
		
		self.measurement_model_obj = measurement_model.measurement_model()
		self.state_space_model_obj = state_space_model.state_space_model()
		self.predicted_covariance_obj = predicted_covariance.predicted_covariance()
		self.measurement_rasidual_obj = measurement_rasidual.measurement_rasidual()
		self.rasidual_covariance_obj = rasidual_covariance.rasidual_covariance()
		self.optimal_kalman_gain_obj = optimal_kalman_gain.optimal_kalman_gain()

		self.state_vector = None


		#start processes
		#self.main_precess()

	def call_space_model(self):

		self.state_space_model_obj.execute_model()
		self.state_vector = self.state_space_model_obj.x_sub_k
		#print("{}{}{}{}{}".format("state_vector","\n",self.state_vector,"\n","*"*20,"\n"))

	def call_measurement_model(self,state_vetor):
		self.measurement_model_obj.execute_model(state_vetor)
		#print("{}{}{}{}{}".format("y_sub_k","\n",self.measurement_model_obj.y_sub_k,"\n","*"*20,"\n"))

	def call_predicted_covariance(self,F_matrix):
		self.predicted_covariance_obj.execute_model(F_matrix)
		#print("{}{}{}{}{}".format("P_sub_k_to_minus_1","\n",self.predicted_covariance_obj.P_sub_k_to_minus_1,"\n","*"*20,"\n"))
	
	def call_measurement_rasidual(self,y_sub_k):
		self.measurement_rasidual_obj.execute_model(y_sub_k)
		#print("{}{}{}{}{}".format("predicted_y_sub_k","\n",self.measurement_rasidual_obj.predicted_y_sub_k,"\n","*"*20,"\n"))
		
	def call_rasidual_covariance(self,H_matrix,P_sub_k_to_minus_1):
		self.rasidual_covariance_obj.execute_model(H_matrix,P_sub_k_to_minus_1)
		#print("{}{}{}{}{}".format("S_sub_k","\n",self.rasidual_covariance_obj.S_sub_k,"\n","*"*20,"\n"))

	def call_optimal_kalman_gain(self,H_matrix,P_sub_k_to_minus_1,S_sub_k):

		self.optimal_kalman_gain_obj.execute_model(H_matrix,P_sub_k_to_minus_1,S_sub_k)
		#print("{}{}{}{}{}".format("K_sub_k","\n",self.optimal_kalman_gain_obj.K_sub_k,"\n","*"*20,"\n"))

	def update_state_estimate(self):
		self.corrected_state_vector = self.state_space_model_obj.x_sub_k  + (self.optimal_kalman_gain_obj.K_sub_k @ self.measurement_rasidual_obj.predicted_y_sub_k)
		#print("{}{}{}{}{}".format("corrected state_vector","\n",self.corrected_state_vector,"\n","*"*20,"\n"))
		self.state_space_model_obj.update_parameters()
	def update_state_covariance(self):
		#P_k - (K_k @ H_k @ P_k)
		self.predicted_covariance_obj.P_sub_k_minus_1_d =  self.predicted_covariance_obj.P_sub_k_to_minus_1 - (self.optimal_kalman_gain_obj.K_sub_k @ self.measurement_model_obj.H_matrix @ self.predicted_covariance_obj.P_sub_k_to_minus_1)

	def main_precess(self):
		self.call_space_model()
		self.call_measurement_model(self.state_vector)
		self.call_predicted_covariance(self.state_space_model_obj.F_matrix)
		self.call_measurement_rasidual(self.measurement_model_obj.y_sub_k)
		self.call_rasidual_covariance(self.measurement_model_obj.H_matrix,self.predicted_covariance_obj.P_sub_k_to_minus_1)
		self.call_optimal_kalman_gain(self.measurement_model_obj.H_matrix,self.predicted_covariance_obj.P_sub_k_to_minus_1,self.rasidual_covariance_obj.S_sub_k)
		self.update_state_estimate()
		self.update_state_covariance()





"""if __name__ == '__main__':
	main_obj = main()
"""

