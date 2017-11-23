# Rock-Paper-Scissors
# mjk 2016.05.09

[![Code Health](https://landscape.io/github/marshki/rock_scissor_paper/master/landscape.svg?style=flat)](https://landscape.io/github/marshki/rock_scissor_paper/master)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)
 
A text-based implementation of the game [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors) for Python 2 and Python 3. 

Game play:
	* User defines number of rounds. 
        * Each round, both players select from: rock, paper, or scissors.  
        * Rock beats scissors, scissors beats paper, and paper beats rock. 
        * A player receives 1 point per round (s)he wins. 
        * 0 points are awarded for ties, and playes replay the round.  
        
## Usage 
To run directly from a shell: 
`python rock_paper_scissor_1.0.py` or `python3 rock_paper_scissor_2.0.py` 

Menu driven program. Each round player is prompted for input. Program determines victor, while keeping cumulative score. Game is over when one player wins user defined number of rounds first.    

## Todo: 
- [x] Increase code efficiency. 
- [x] Add support for Python 3.  
- [ ] Add unit test. 
- [ ] Add support for Travis-CI and ~~Landscape.io~~

## History 
First commit May 9, 2016 @ 14:10 ET. 

Version 2.0 August 8, 2016 

## License 
[MIT license](https://opensource.org/licenses/MIT). 'Nuff said. 
