"""
script to calculate rotational tumbling time of protein
"""

# Definition 1: Average time for protein to rotate by 1 radian
# Choose Ca atoms of two residues on oppositie ends of the protein between 406
# and 537
# 1: Residue 408 - Atom 82
# 2: Residue 459 - Atom 918

# Angle relative to +z axis of vector connecting atoms 82 and 918
# gmx command in *.xvg file
# 82_459_angle_z.xvg

import plot_xvg as pxvg
import matplotlib.pyplot as plt
import numpy as np

FNAME = "full_trajec/anglez_82-459_200-500ns.xvg"

#pxvg.plot_xvg(FNAME,
#         ylabel_set="Angle (Degrees)",
#         title_set="Angle from Positive Z-Axis, 2V1A",
#         legend="Data",
#         do_tot_avg=True,
#         do_running_avg=True)

time, angle_deg, metadata = pxvg.read_file(FNAME)  # time in ps, angle in degrees

print(time)
print(angle_deg)

# Convert degrees to radians
angle_rad = angle_deg * np.pi/180.0
time_ns = time / 1000.0

f1, ax1 = plt.subplots()
pxvg.make_plot(time_ns, angle_rad, metadata, ax1, ylabel_set="Angle (Rad)", title_set="Angle from Positive Z-Axis, 2V1A", legend="Data", do_running_avg=True)

# Find Average time to rotate by 1 radian:
start_idx = 0
curr_idx = 0
dt_rot_1rad = []
d_angle = 0
while curr_idx < len(time) - 1:
    while np.abs(d_angle) < 1:
        if curr_idx == len(time) - 1:
            break
        d_angle = angle_rad[curr_idx] - angle_rad[start_idx]
        curr_idx += 1
    dt = time[curr_idx] - time[start_idx]
    if np.abs(d_angle) > 1:
        dt_rot_1rad.append(dt)
    d_angle = 0
    start_idx = curr_idx

print(dt_rot_1rad)
avg_rot_1rad = np.average(dt_rot_1rad)
print("Average Time to Rotate 1 Radian (ps):", avg_rot_1rad)


plt.show()