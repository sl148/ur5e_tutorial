# ServoJ is well-suited for executing smooth, continuous robot motions.
# Ensure that the motion paths are sufficiently fine-grained so that moveJ can properly scale the speed.

import threading
import rtde_control
import numpy as np
import os
import sys
from robotiq_gripper_control import RobotiqGripper
from rtde_control import RTDEControlInterface
import time


rtde_c = rtde_control.RTDEControlInterface("192.168.0.3")

# Parameters
velocity = 0.5
acceleration = 0.5
dt = 1.0/500  # 2ms
lookahead_time = 0.1
gain = 300
joint_q = [-1.54, -1.83, -2.28, -0.59, 1.60, 0.023]

# Move to initial joint position with a regular moveJ
rtde_c.moveJ(joint_q)

# Execute 500Hz control loop for 2 seconds, each cycle is 2ms
for i in range(1000):
    t_start = rtde_c.initPeriod()
    rtde_c.servoJ(joint_q, velocity, acceleration, dt, lookahead_time, gain)
    joint_q[0] += 0.001
    joint_q[1] += 0.001
    rtde_c.waitPeriod(t_start)

rtde_c.servoStop()
rtde_c.stopScript()