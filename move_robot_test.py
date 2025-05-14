import rtde_control
import numpy as np
import time

def convert_to_rad(path):
    new_path = []
    for q in path:
        new_path.append([v/180.*np.pi for v in q])
    return new_path

def main():
    PI = np.pi
    arm_ip = "192.168.1.9"
    arm = rtde_control.RTDEControlInterface(arm_ip)

    q_init = [0., -PI/2, -PI/2, PI/2, -PI/2, 0.]
    arm.moveJ(q_init)
    arm_path = [[60., -120, -40, 225, 42, 77], [0, -65, -112, 150, -90, 90], [-37, -123, -50, 260, 144, 77]]
    arm_path = convert_to_rad(arm_path)
    for q in arm_path:
        print(f"\nMove to {q}")
        arm.moveJ(q)
        print("Movement Completed")

        time.sleep(1)


if __name__ == "__main__":
    main()
