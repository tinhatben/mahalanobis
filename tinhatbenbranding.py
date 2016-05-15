#! /usr/bin/env python
"""!
-----------------------------------------------------------------------------
File Name : tinhatbenbranding.py

Purpose:

Created: 24-Apr-2016 08:00:45 AEST
-----------------------------------------------------------------------------
Revision History



-----------------------------------------------------------------------------
S.D.G
"""
__author__ = 'tinhatben'
__revision__ = '0.1'
__date__ = '24-Apr-2016 08:00:45 AEST'
__license__ = 'BSD 3 Clause'

# LICENSE DETAILS############################################################
# This Source Code Form is subject to the terms of the BSD 3 Clause License
# see the file LICENSE for more information

# IMPORTS#####################################################################

##############################################################################

# Constants
TINHATBEN_GRAY = "#7a7a7a"
TINHATBEN_YELLOW = "#ffaf1f"

def add_tinhatbendotcom(ax, pos):

    ax.text(pos[0], pos[1], 't',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_YELLOW, fontsize=25, style='normal')
    ax.text(pos[0] + 0.02, pos[1], 'in',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_GRAY, fontsize=25, style='normal')
    ax.text(pos[0] + 0.06, pos[1], 'h',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_YELLOW, fontsize=25, style='normal')
    ax.text(pos[0] + 0.09, pos[1], 'at',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_GRAY, fontsize=25, style='normal')
    ax.text(pos[0] + 0.135, pos[1], 'b',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_YELLOW, fontsize=25, style='normal')
    ax.text(pos[0] + 0.16, pos[1], 'en.com',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color=TINHATBEN_GRAY, fontsize=25, style='normal')

