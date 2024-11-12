###
# Prints vehicle registration numbers from Krakow
#
polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]

for i in range(0, len(polish_license_plates)):
    if polish_license_plates[i][0:2] == "KR" or polish_license_plates[i][0:2] == "KK":
        print(polish_license_plates[i])