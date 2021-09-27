import numpy as np
import time
import main


def main2():
    main_obj = main.main()

    z_k = np.array([[4.721,0.143,0.006], # k=1
                    [9.353,0.284,0.007], # k=2
                    [14.773,0.422,0.009],# k=3
                    [18.246,0.555,0.011], # k=4
                    [22.609,0.715,0.012]])# k=5

    time_k = 1
    while(time_k < len(z_k)):
        main_obj.main_precess()
        main_obj.measurement_rasidual_obj.z_sub_k = z_k[time_k]
        time_k += 1

        print("state estimate before ekf=",main_obj.state_space_model_obj.x_sub_k,"\n")
        print("observaton=",main_obj.measurement_model_obj.y_sub_k,"\n")
        print("State estimate after ekf=",main_obj.corrected_state_vector,"\n")
        print("*************************************************************")





if __name__ == '__main__':
    main2()