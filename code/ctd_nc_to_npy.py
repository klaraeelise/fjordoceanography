import xarray as xr
import numpy as np
import gsw
from pathlib import Path


def convert_ctd_nc_to_npy(ncfile, outfile=None):

    ncfile = Path(ncfile)

    if outfile is None:
        outfile = ncfile.with_suffix(".npy")
    else:
        outfile = Path(outfile)

    ds = xr.open_dataset(ncfile)

    P_all = ds["Pressure"].values
    T_all = ds["t"].values
    S_all = ds["sp"].values
    ST_all = ds["sta"].values
    TIME_all = ds["time"].values
    LON_all = ds["lon"].values
    LAT_all = ds["lat"].values

    if "o" in ds.variables:
        O_all = ds["o"].values
    elif "raw_o" in ds.variables:
        O_all = ds["raw_o"].values
    else:
        O_all = None

    nsta = len(ST_all)

    if T_all.shape[1] == nsta:
        depth_first = True
    elif T_all.shape[0] == nsta:
        depth_first = False
    else:
        raise ValueError("Cannot identify the station dimension")

    CTD = {}

    for i in range(nsta):

        stnum = int(ST_all[i])

        if depth_first:

            T = T_all[:, i]
            S = S_all[:, i]
            P = P_all[:, i] if np.ndim(P_all) == 2 else P_all

            if O_all is not None:
                OX = O_all[:, i]
            else:
                OX = np.full_like(T, np.nan)

        else:

            T = T_all[i, :]
            S = S_all[i, :]
            P = P_all[i, :] if np.ndim(P_all) == 2 else P_all

            if O_all is not None:
                OX = O_all[i, :]
            else:
                OX = np.full_like(T, np.nan)

        lon = float(LON_all[i])
        lat = float(LAT_all[i])

        good = np.isfinite(P) & np.isfinite(T) & np.isfinite(S)

        P = P[good]
        T = T[good]
        S = S[good]
        OX = OX[good]

        SA = gsw.SA_from_SP(S, P, lon, lat)
        CT = gsw.CT_from_t(SA, T, P)

        SIGMA0 = gsw.sigma0(SA, CT)
        RHO = gsw.rho(SA, CT, P)

        CTD[stnum] = dict(

            P=P,
            T=T,
            S=S,
            OX=OX,

            st=stnum,
            datetime=str(TIME_all[i]),

            LON=lon,
            LAT=lat,

            SIGMA0=SIGMA0,
            RHO=RHO
        )

    np.save(outfile, CTD, allow_pickle=True)

    print("saved:", outfile)

    return CTD



def batch_convert_ctd_nc_to_npy(
    input_path,
    pattern="*.nc",
    output_dir=None
):

    input_path = Path(input_path)

    if output_dir is None:
        output_dir = input_path
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)

    files = sorted(input_path.glob(pattern))

    for f in files:

        out = output_dir / f"{f.stem}.npy"

        convert_ctd_nc_to_npy(f, out)

    print("\nAll files processed")