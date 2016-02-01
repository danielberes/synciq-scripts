#!/usr/bin/python

import os, sys, getopt
import isi.fs.siq as siq

NEWLINE = '\n'
UNDERLINE = '\033[4m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
ENDC = '\033[0m'

def main(argv):
  policy_name = ''
  delete_file = ''
  try:
      opts, args = getopt.getopt(argv,"hp:f:",["policy=","file="])
  except getopt.GetoptError as err:
      print str(err)
      print "deletepolicyfile.py -p <policy> -f <file_to_delete>"
      sys.exit(2)
  if not (args or opts):
      print "Not enough options or aruments given. Try '-h' for help"
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
        print "deletepolicyfile.py -p <policy> -f <file_to_delete>"
        sys.exit()
      elif opt in ("-p", "--policy"):
        policy_name = arg
      elif opt in ("-f", "--file"):
        all_arguments = arg.split(',')
      else:
        assert False, "unhandled option"
        usage()
        sys.exit()
  print NEWLINE + CYAN + "Starting process..." + NEWLINE + ENDC
  synciq = siq.SyncIQ()
  trecs = synciq.get_target_status()
  dom_id = dom_gen = 0
  for trec in trecs:
    if trec.policy_name == policy_name:
       dom_id = trec.domain_id
       dom_gen = trec.domain_generation
       break
  if dom_id != 0 and dom_gen != 0:
     utils = siq.SyncIQUtils()
     utils.ifs_domain_allowwrite(dom_id, dom_gen)
  # do unlink
  error_amount = 0
  for delete_list in all_arguments:
     the_file = delete_list
     if os.path.exists(the_file):
         print BOLD + GREEN + "SUCCESS:" + ENDC + " Deleted %s" % the_file
         os.unlink(the_file)
     else:
         print BOLD + RED + "FAILURE:" + ENDC + " Cannot delete %s." % the_file
         error_amount += 1
  if error_amount:
     print NEWLINE + "There were "+ UNDERLINE +"%s" % error_amount + ENDC + " error(s)."
  print NEWLINE + CYAN + "Ending process." + NEWLINE + ENDC

if __name__ == "__main__":
   main(sys.argv[1:])
