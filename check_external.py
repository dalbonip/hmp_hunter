import urllib.request
from bs4 import BeautifulSoup


def check_mitre(libtosearch):
  url = libtosearch.replace(" ","+")
  result = []
  con1 = urllib.request.urlopen(f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={url}")
  soup1 = BeautifulSoup(con1, "html.parser")

  cves_dirty=soup1.find_all("td", valign="top")


  for cves in cves_dirty:
    cve = cves.text.strip()
    if "Search CVE Using Keywords:" in cve or "Search CVE Using Keywords:" in cve or "For More Information:  CVE Request Web Form (select “Other” from dropdown)" in cve:
      break
    if len(cve) < 20:
      title = cve
    else:
      title_and_cve = title + " : " + cve
      result.append(title_and_cve)
  return result
