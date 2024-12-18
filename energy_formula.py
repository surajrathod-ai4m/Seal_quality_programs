# Function to calculate thickness from GSM and density
def calculate_thickness(gsm, density):
    # Thickness (in meters) = GSM (g/m²) / Density (g/m³)
    return gsm / density

# Function to calculate E_total with A factored out in the numerator
def calculate_E_total(T, T0, t, gsm_A, gsm_B, gsm_C, k_A, k_B, k_C, A):
    # Densities in g/m³ for the materials --------------------------Not to be changed
    density_A = 900000  # BOPP
    density_B = 930000  # MET BOPP (average of 910,000 - 950,000 g/m³)
    density_C = 925000  # LDPE (average of 910,000 - 940,000 g/m³)

    # Calculate thicknesses from GSM and density in meters
    d_A = calculate_thickness(gsm_A, density_A)
    d_B = calculate_thickness(gsm_B, density_B)
    d_C = calculate_thickness(gsm_C, density_C)

    # Calculate the denominator (thermal resistances of the materials without A)
    denominator = (d_A / k_A) + (d_B / k_B) + (d_C / k_C)
    print(denominator)
    
    # Calculate E_total with A in the numerator
    E_total = ((T - T0) * t * A) / denominator
    
    return E_total

# Inputs
T = 165  # Current temperature in degrees Celsius
T0 = 55  # Reference temperature in degrees Celsius
t = 0.165  # Time in seconds (1 hour)
gsm_A = 15.3  # GSM for BOPP (in g/m²)
gsm_B = 12.5  # GSM for MET BOPP (in g/m²)
gsm_C = 25.75  # GSM for LDPE (in g/m²)
k_A = 0.1  # Thermal conductivity of BOPP in W/m·K ---------------------Not to be changed
k_B = 0.15  # Thermal conductivity of MET BOPP in W/m·K-----------------Not to be changed
k_C = 0.33  # Thermal conductivity of LDPE in W/m·K---------------------Not to be changed
A = 0.00516  # Cross-sectional area in square meters

# Calculate E_total
E_total = calculate_E_total(T, T0, t, gsm_A, gsm_B, gsm_C, k_A, k_B, k_C, A)

# Output the result
print(f"E_total = {E_total:.2f} J")