# InSAR Damage Assessment

This project maps building and infrastructure damage over a user-defined area of interest using Sentinel-1 SAR interferometric coherence loss as a proxy.  Collapsed or heavily damaged structures decorrelate the radar return between passes, while intact, unchanged ground mostly does not. 

1. The pipeline queries the Copernicus Data Space Ecosystem catalog for Sentinel-1 SLC acquisitions over the AOI and automatically selects a triplet of scenes on a shared orbital track: 2 pre-event images and 1 post-event image. 
2. Downloads and processes them with ESA SNAP into two coherence products: a "baseline" pair (pre-event1 vs. pre-event2, characterizing ordinary non-damage decorrelation from vegetation, weather, and seasonal change) and a "co-event" pair (pre-event2 vs. post-event, capturing whatever additionally decorrelated during the event window).
3. Pixels where coherence drops significantly more in the co-event pair than in the baseline pair are flagged as damage candidates, connectivity-filtered to suppress speckle noise, and the result is written out as a georeferenced multi-band GeoTIFF, a static comparison figure, an interactive HTML map with coherence/damage layers, and a JSON summary of affected-area statistics. 
