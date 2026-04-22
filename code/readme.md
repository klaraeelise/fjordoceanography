Prepare:

1. ctd_nc_to_npy: This script converts CTD data from NetCDF files into structured NumPy .npy files. It also computes key seawater properties (e.g., density and σ₀) using TEOS-10 via the GSW Oceanographic Toolbox.

2. convert.py: This script calls a function: ctd_nc_to_npy to batch convert all CTD NetCDF files in a folder into .npy files and saves them to a specified output directory.

3. plot_CTD_location1: This script plots bathymetry and CTD station locations for each .npy file within a defined region. It generates maps with depth contours, station labels, and a sill mooring marker, saving each figure automatically.

Diffusivity:

1. calculate_hypsometry: This script computes basin hypsometry from bathymetry data by calculating area and cumulative volume as functions of depth, and outputs the results as tables and plots.

2. Plot_1314, 1516: This script compares the 2013 and 2014 (2015 and 2016) CTD density profiles by computing σ₀, applying a deep-layer offset correction to align the profiles, then saving and plotting the aligned density differences.

3. Plot_2224: This script compares the 2022–2024 CTD density profiles by computing σ₀, aligning the deep parts of the profiles using bottom values, then saving and plotting the aligned density differences between years.

4. mixing_scan_u_1314,1516: This script estimates vertical diffusivity k(u) from two aligned density profiles and basin hypsometry by scanning different depths, then saves and plots the resulting mixing profiles.

5. mixing_scan_u_2224: This script estimates vertical diffusivity for 2022–2024 by combining basin hypsometry with both aligned and raw density-profile differences, then compares the resulting k(u) profiles across depth and time.

6. Plot_mixing_u: This script reads the diffusivity profiles from different stagnation periods, removes selected unreliable depths, and plots the vertical diffusivity k(u) curves together for comparison.

Compare CTD: 

1. compare_2017_2019: This script compares selected CTD profiles from 2017–2019 by calculating vertical profiles and layer-mean values of σ₀, CT, SA, and dissolved oxygen, then quantifies year-to-year changes and plots them in a four-panel figure.

2. compare_2023_2025: This script compares selected CTD profiles from 2023–2025 by calculating vertical profiles and layer-mean values of σ₀, CT, SA, and dissolved oxygen, then quantifies year-to-year changes and plots them in a four-panel figure.


Vn and HD frequency:

1. calculate_oxygen_Vn: This script extracts 200–400 m averages (O₂, σ₀, temperature, salinity) from selected CTD stations across years, builds time series, performs trend and change analyses, and computes annual ventilation rates (Vn).

2. sognes_Vn: This script computes the frequency of high-density water at Sognesjøen from the 75 m time series, matches it with Masfjorden ventilation rates (Vn), and then evaluates and plots their relationship through correlation and linear regression.