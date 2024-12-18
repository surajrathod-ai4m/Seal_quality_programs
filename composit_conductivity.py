def calculate_thermal_resistance(gsm_A, gsm_B, gsm_C):
    # Densities in g/m³ for the materials
    density_A = 900000  # BOPP
    density_B = 930000  # MET BOPP
    density_C = 925000  # LDPE
    
    # Thermal conductivities in W/m·K
    k_A = 0.1   # BOPP
    k_B = 0.15  # MET BOPP
    k_C = 0.33  # LDPE
    
    # Calculate thicknesses from GSM and density in meters
    d_A = gsm_A / density_A
    d_B = gsm_B / density_B
    d_C = gsm_C / density_C
    
    # Calculate total thermal resistance (denominator)
    thermal_resistance = (d_A / k_A) + (d_B / k_B) + (d_C / k_C)
    
    return thermal_resistance

# Example usage with your values
gsm_A = 17.1  # GSM for BOPP
gsm_B = 14.4  # GSM for MET BOPP
gsm_C = 29.44  # GSM for LDPE

result = calculate_thermal_resistance(gsm_A, gsm_B, gsm_C)
print(f"Total thermal resistance = {result:.6f} K·m²/W")