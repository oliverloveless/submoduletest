#!/usr/bin/env python
#####################################
# Installation module for testSSL
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Steven van der Baan (vdbaan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SSLScan (rbsec - Ian Ventura-Whiting)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/rbsec/sslscan.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sslscan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,gcc,make,build-essential,openssl,zlib1g-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,gcc,make"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

LAUNCHER="sslscan"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make static"
