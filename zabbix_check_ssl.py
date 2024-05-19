#!/usr/bin/pypy3
import ssl
import OpenSSL
import sys
from datetime import datetime, timezone

def get_ssl_expiry_date(host, port=443):
 
    try:
        cert = ssl.get_server_certificate((host, port),ssl.PROTOCOL_TLSv1_2)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    except Exception as e:
        print(e)
        return 3.14

    return x509.get_notAfter().decode()

if __name__ == "__main__":
     if len(sys.argv) != 2:
         print("使用方法: python test.py <网址>")
         sys.exit(1)
        
    url = sys.argv[1]
    days_difference = 0
    expiry_date = get_ssl_expiry_date(url)
    if expiry_date != 3.14:
        date_format = '%Y%m%d%H%M%S%z' 
        date_object = datetime.strptime(expiry_date, date_format)
        now = datetime.now(timezone.utc)
        delta = date_object - now 
        days_difference = delta.days
    else:
        days_difference = expiry_date
    print(days_difference)
