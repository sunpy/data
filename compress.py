def compress(file, factor):
    """
    Will compress a given ``file`` with a factor of ``factor``.

    Only created for 2D images.

    Parameters
    ----------
    file : `str`
        File to compress.
    factor : `float`
        Factor to shrink by.
        E.g., SDO 4k to 1k, factor = 0.25
    """
    from astropy.io import fits
    from scipy.ndimage import zoom

    with fits.open(file) as hdus:
        for hdu in hdus:
            if isinstance(hdu, fits.hdu.table.TableHDU):
                continue
            hdu.verify("fix")
            if hdu.header["NAXIS"] == 2:
                data = zoom(hdu.data, factor, order=0)
                hdu.data = data
                hdu.header["NAXIS1"] = hdu.data.shape[1]
                hdu.header["NAXIS2"] = hdu.data.shape[0]
            hdu = fits.CompImageHDU(hdu.data, hdu.header)
        # Avoid overwriting the original file, you will need to rename after the fact.
        hdus.writeto(f"{file}.fits", overwrite=True)
