def compress(file, dims):
    """
    Will compress a given ``file`` with a factor of ``factor``.

    Will only work for files that sunpy.map.Map can read.

    Parameters
    ----------
    file : `str`
        File to compress.
    dims : `float`
        Final dimensions of the compressed image in pixels.
    """
    import astropy.units as u
    from astropy.io import fits

    from sunpy.map import Map

    amap = Map(file)
    new_dimensions = [dims, dims] * u.pixel
    resampled_map = amap.resample(new_dimensions)
    # Write the resampled map to a new file.
    # You will want to move the file to the correct location later on.
    resampled_map.save(f"{file}.resample.fits", hdu_type=fits.CompImageHDU)
