import re

from check_external import check_mitre
# from check_external import check_mitre

# lib = "mcafee webadvisor"
# version = "16.0.40"

def look_for_lib(lib,version):
  cve_version_regex = '(( |v)(\d+)\.(\d+)\.?(\d+)\.?(\d+)?\.?(\d+)?( |\.))'
  cve_version_regex_bkp = '(( |v)(\d+)( |\.)?(\d+)?)'

  version.strip()

  check_dot_mistake = version.count(",")

  if check_dot_mistake >= 1:
    version.replace(",",".")


  vuln_list = []
  return_list = []
  first_decimal = 0
  second_decimal = 0
  third_decimal = 0
  fourth_decimal = 0
  
  query_first_decimal = 0
  query_second_decimal = 0
  query_third_decimal = 0
  query_fourth_decimal = 0


  global dec_count
  dec_count = version.count(".")
  
  if dec_count == 0:
    #actual_version = version
    first_decimal = int(version)
  elif dec_count == 1:
    first_decimal = int(re.findall("(\d+)\.?(\d+)?",version)[0][0])
    second_decimal = int(re.findall("(\d+)\.(\d+)",version)[0][1])
  elif dec_count == 2:
    first_decimal = int(re.findall("(\d+)\.?(\d+)?",version)[0][0])
    second_decimal = int(re.findall("(\d+)\.(\d+)",version)[0][1])
    third_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)",version)[0][2])
  elif dec_count >= 3:
    first_decimal = int(re.findall("(\d+)\.?(\d+)?",version)[0][0])
    second_decimal = int(re.findall("(\d+)\.(\d+)",version)[0][1])
    third_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)",version)[0][2])
    fourth_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)?\.?(\d+)?",version)[0][3])


  cves = check_mitre(lib)

  for item in cves:
    #print("\n",item)

    cve = item[(item.find(":"))+2:]

    try:
      version_from_query = re.findall(cve_version_regex,cve)[0][0].strip()
    except:
      try:
        version_from_query = re.findall(cve_version_regex_bkp,cve)[0][0].strip()
      except:
        version_from_query = "1337"
    finally:
      query_dec_count = version_from_query.count(".")
    
    if version_from_query == "1337":
      vuln_list.append("safe")
      continue

    while version_from_query[-1] == "." or version_from_query[-1] == " ":
      query_dec_count = query_dec_count -1
      version_from_query = version_from_query[:-1]

    try:
      query_first_decimal = int(re.findall("(\d+)\.(\d+)",version_from_query)[0][0])
    except:
      query_first_decimal = int(re.findall("(\d+)\.?(\d+)?",version_from_query)[0][0])


    if query_dec_count == 1:
      query_second_decimal = int(re.findall("(\d+)\.(\d+)",version_from_query)[0][1])
    elif query_dec_count == 2:
      query_second_decimal = int(re.findall("(\d+)\.(\d+)",version_from_query)[0][1])
      query_third_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)",version_from_query)[0][2])
    elif query_dec_count == 3:
      query_second_decimal = int(re.findall("(\d+)\.(\d+)",version_from_query)[0][1])
      query_third_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)",version_from_query)[0][2])
      query_fourth_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)?\.?(\d+)?",version_from_query)[0][3])
    elif query_dec_count > 3:
      query_second_decimal = int(re.findall("(\d+)\.(\d+)",version_from_query)[0][1])
      query_third_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)",version_from_query)[0][2])
      query_fourth_decimal = int(re.findall("(\d+)\.(\d+)\.(\d+)?\.?(\d+)?",version_from_query)[0][3])


    if first_decimal > query_first_decimal:
      vuln_list.append("safe")
    elif (first_decimal == query_first_decimal) and (second_decimal > query_second_decimal):
      vuln_list.append("safe")
    elif (first_decimal == query_first_decimal) and (second_decimal == query_second_decimal) and (third_decimal > query_third_decimal):
      vuln_list.append("safe")
    elif (first_decimal == query_first_decimal) and (second_decimal == query_second_decimal) and (third_decimal > query_third_decimal) and (fourth_decimal > query_fourth_decimal):
      vuln_list.append("safe")
    else:
      vuln_list.append(item)

  if vuln_list.count("safe") == len(vuln_list):
    return 404
  else:
    for vul in vuln_list:
      if vul != "safe":
        return_list.append(vul)
    return return_list


# y = look_for_lib(lib,version)

# for x in y:
#   print(f"\n{x}")