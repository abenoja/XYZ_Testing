# HALO Parameters and GITHUB environment vaiables and secrets
##
# HALO parameters first
#
# PROD or DEV
HALO_ENVMNT           = sys.argv[1]
# The HALO ticket id; an SR
HALO_TICKET           = sys.argv[2]
# Name (in quotes)
GUEST_DISPLAYNAME     = sys.argv[3]
# Email
PARAM_GUEST_EMAIL     = sys.argv[4]
# 1.11 - trim the leading and trailing spaces
GUEST_EMAIL           = PARAM_GUEST_EMAIL.strip()
# Options
OPTIONS               = sys.argv[5]

print("Options           >{}<".format(OPTIONS))
