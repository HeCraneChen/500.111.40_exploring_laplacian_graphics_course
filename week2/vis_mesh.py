import igl  # Import the libigl library 
import polyscope as ps  # Import the polyscope library
import numpy as np

# Read the mesh from a file
v, f = igl.read_triangle_mesh("HappyDragon.ply")

# Create a rotation matrix for 90 degrees rotation around x-axis
angle = np.radians(90)
rotation_matrix = np.array([[1, 0, 0],
                            [0, np.cos(angle), -np.sin(angle)],
                            [0, np.sin(angle), np.cos(angle)]])
# Rotate vertices with the matrix
v = np.dot(v, rotation_matrix)

# Print the dimensions of V (vertices) and F (faces)
print("Vertices shape:", v.shape)
print("Faces shape:", f.shape)

# Initialize Polyscope
ps.init()
ps.set_ground_plane_mode("shadow_only")  # set +Z as up direction
ps.set_shadow_darkness(0.1)              # lighter shadows
# Register the mesh in Polyscope
ps_mesh = ps.register_surface_mesh("my_mesh", v, f)
ps_mesh.set_color((68/255,254/255,157/255))  
ps_mesh.set_edge_color((0.36,0.36,0.36))  # white edges
ps_mesh.set_edge_width(1.5)      # adjust as needed
# Show the Polyscope GUI
ps.show()
