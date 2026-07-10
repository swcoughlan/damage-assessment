import os

# Copernicus Data Space Ecosystem (CDSE) credentials.
# Set these as environment variables rather than hardcoding them here
# Open Windows Powershell and paste the following two lines (insert your credentials
# [Environment]::SetEnvironmentVariable('CDSE_USERNAME', 'YOUR USERNAME', 'User')
# [Environment]::SetEnvironmentVariable('CDSE_PASSWORD', 'YOUR PASSWORD', 'User')

username = os.environ.get('CDSE_USERNAME')
password = os.environ.get('CDSE_PASSWORD')

if not username or not password:
    raise RuntimeError(
        "CDSE_USERNAME and/or CDSE_PASSWORD environment variables are not set. "
        "Set them to your Copernicus Data Space Ecosystem login before running this notebook."
    )

