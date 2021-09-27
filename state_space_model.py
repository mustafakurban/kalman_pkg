"""     
State estimation with kalman filter


author: Mustafa KURBAN (@mustafakurban)
"""

import numpy as np
import configuration


class state_space_model():
        def __init__(self):
                #import default matrix veriables 
                veriables = configuration.state_space_hub()


                self.x_sub_k_minus_1 = veriables.x_sub_k_minus_1
                self.u_sub_k_minus_1 = veriables.u_sub_k_minus_1

                self.x_sub_k                  = None
                self.u_sub_k                  = None

                self.F_matrix    = veriables.F_matrix
                self.B_matrix    = veriables.B_matrix
                self.state_noise = veriables.state_noise

        def execute_model(self):
                self.x_sub_k = (self.F_matrix @ self.x_sub_k_minus_1 + self.B_matrix @ self.u_sub_k_minus_1) + self.state_noise

        def update_parameters(self):
                self.x_sub_k_minus_1 = self.x_sub_k


