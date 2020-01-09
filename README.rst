===================
Rock-Paper-Scissors
===================

.. image:: https://travis-ci.org/marshki/rock_paper_scissors.svg?branch=master
    :target: https://travis-ci.org/marshki/rock_paper_scissors

.. image:: https://api.codacy.com/project/badge/Grade/c51fb45f342445e3bc2fe2f9d94f2d12    
    :target: https://www.codacy.com/manual/marshki/rock_paper_scissors?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/rock_paper_scissors&amp;utm_campaign=Badge_Grade

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges/


Rock-Paper-Scissors from the CLI
-----------------------------------
No-frills implemenation of the classic game for Python 2 & 3.
 
Requirements
------------
None.

Usage
-----
From a shell: 
::
    python rock_paper_scissors.py
    python3 rock_paper_scissors.py

Game play:

- Player defines number of rounds needed to win.
- Player selects from: "rock" (r), "paper" (p), "scissors" (s), "quit" (q).
- Player's move is evaluated against randomized move from bot.
- Rock beats scissors, scissors beat paper, and paper beats rock.
- One (1) point is awarded to round's winner.
- Zero (0) points are awarded for a tie, and the round must be replayed until winner is determined.
- First player to win defined number of rounds is the victor. 
 
Change Log
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/rock_paper_scissors/blob/master/CHANGELOG.rst
 
License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/rock_paper_scissors/blob/master/LICENSE.txt
