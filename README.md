

# InSAR Damage Assessment

This project maps building and infrastructure damage over a user-defined area of interest using Sentinel-1 SAR interferometric coherence loss as a proxy.  Collapsed or heavily damaged structures decorrelate the radar return between passes, while intact/unchanged ground mostly does not. 

1. The pipeline queries the Copernicus Data Space Ecosystem catalog for Sentinel-1 SLC acquisitions over the AOI and automatically selects a triplet of scenes on a shared orbital track: 2 pre-event images and 1 post-event image. 
2. Downloads and processes them with ESA SNAP into two coherence products: a "baseline" pair (pre-event1 vs. pre-event2, characterizing ordinary non-damage decorrelation from vegetation, weather, and seasonal change) and a "co-event" pair (pre-event2 vs. post-event, capturing whatever additionally decorrelated during the event window).
3. Pixels where coherence drops significantly more in the co-event pair than in the baseline pair are flagged as damage candidates, connectivity-filtered to suppress speckle noise, and the result is written out as a georeferenced multi-band GeoTIFF, a static comparison figure, an interactive HTML map with coherence/damage layers, and a JSON summary of affected-area statistics.

<br>
How it works: 
<br><br>
<img width="1354" height="679" alt="Screenshot_5" src="https://github.com/user-attachments/assets/1ccf08ba-2221-4ff1-aed7-3a716730113f" />
<br><br>

Processing pipeline: 
<br><br>
<img width="1460" height="627" alt="Screenshot_6" src="https://github.com/user-attachments/assets/5a61931d-1d27-4ab6-a1c7-d150ed2ef2ce" />
<br><br>

Examples:
<br><br>
Damage to Caracas, Venezuela, caused by an earthquake on 24/06/2026
<br><br>
<img width="1433" height="726" alt="Screenshot_2" src="https://github.com/user-attachments/assets/e6e65aba-ab2e-44f4-a91a-9c7d5c4dd520" />
<br><br>
Battle damage to Mosul, Iraq, between 09/04/2017 – 21/04/2017
<br><br>
<img width="1450" height="952" alt="Screenshot_4" src="https://github.com/user-attachments/assets/fdddcbef-e55d-4fdb-a47a-8ae14a94ef95" />






