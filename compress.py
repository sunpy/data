def compress(file, factor):
    from astropy.io import fits
    from scipy.ndimage import zoom

    with fits.open(file) as hdus:
        for hdu in hdus:
            if isinstance(hdu, fits.hdu.table.TableHDU):
                continue
            hdu.verify("fix")
            if "NAXIS3" in hdu.header:
                data = []
                for i in range(hdu.data.shape[0]):
                    data.append(zoom(hdu.data[i], factor, order=0))
                hdu.data = data
                hdu.header["NAXIS1"] = hdu.data.shape[2]
                hdu.header["NAXIS2"] = hdu.data.shape[1]
                hdu.header["NAXIS3"] = hdu.data.shape[0]
            hdu = fits.CompImageHDU(hdu.data, hdu.header)
        hdus.writeto(f"{file}.fits")
