# Lab 1

This repo contains the code and documents needed to complete Lab 1. Requires `lab-machine-env` and the setup from Lab 0.

## Getting Started

Please follow **[Lab_1.pdf](Lab_1.pdf)**.

## Bugs

- The Quanser "QArmKeyboardNavigator" has a bug. If you run into an error message like this
  ```
  ee_position, ee_rotation, gamma = self.armMath.forward_kinematics(phi=initialPose)
  ValueError: not enough values to unpack (expected 3, got 2)
  ```
  the bug is that the forward_kinematics function only outputs 2 values. Simple go to the file (`...\Quanser\0_libraries\python\hal\products\qarm.py`, line 343) and delete `gamma`, then define it as 0 on the line below.
