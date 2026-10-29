import numpy as np

L_1 = 0.1400
L_2 = 0.3500
L_3 = 0.0500
L_4 = 0.2500
L_5 = 0.1500
BETA = np.arctan(L_3/L_2)

LAMBDA_1 = L_1
LAMBDA_2 = np.sqrt(L_2**2 + L_3**2)
LAMBDA_3 = L_4 + L_5

def T_homo(framei):
        theta, d, a, alpha = framei

        return np.array([
            [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
            [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
            [0, np.sin(alpha), np.cos(alpha), d],
            [0, 0, 0, 1]
        ])

def forward_kin(phi):
    '''
    Implement a forward kinematics function for the QArm

    Input:
        phi: the joint angles in radians, in order of base, shoulder, elbow, wrist

    Output:
        location: the end effector coordinate system origin position in the base {0} coordinate system
        rotation: rotation matrix from the end effector {4} coordinate system to the base {0} coordinate system
    '''

    phi = np.array(phi, dtype=float, copy=True)

    # == your code here ==

    f1 = [phi[0], LAMBDA_1, 0, np.deg2rad(-90)]
    f2 = [phi[1]-(np.deg2rad(90)-BETA), 0, LAMBDA_2, 0]
    f3 = [phi[2] - BETA, 0, 0, np.deg2rad(-90)]
    f4 = [phi[3], LAMBDA_3, 0, 0]

    T_0_1 = T_homo(f1)
    T_1_2 = T_homo(f2)
    T_2_3 = T_homo(f3)
    T_3_4 = T_homo(f4)

    T_0_4 = T_0_1 @ T_1_2 @ T_2_3 @ T_3_4

    # Replace these two definitions
    location = T_0_4[:3,3]
    rotation = T_0_4[:3,:3]

    # == end of your code ==

    return location, rotation



if __name__ == '__main__':

    # Function input is radians

    phi = np.radians(np.array([0,-11,-75,0]))
    location, rotation = forward_kin(phi)
    print('Input -> location:', location, 'rotation:', rotation)