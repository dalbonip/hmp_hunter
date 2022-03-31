import re
from check_external import check_mitre
from search_db_for_lib import look_for_lib

def read_data(lib,version):
  vulnlist = []
  retorno = look_for_lib(lib,version)
  if retorno != 404 and retorno != None :
    retorno_vulns = list(dict.fromkeys(retorno))
    return retorno_vulns
  else:
    return [f'lib {lib} {version} está segura de acordo com as CVEs publicadas até o momento']

def get_cve(vulns):
  cvelist=[]
  for vuln in vulns:
    cvelist.append(vuln[:(vuln.find(':'))])
  return cvelist

def get_version(vulns):
  versionlist=[]
  for vuln in vulns:
    versionlist.append(vuln[(vuln.find(':')):])
  return versionlist