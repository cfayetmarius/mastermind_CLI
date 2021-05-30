Welcome the my school project, coding a mastermind in CLI.

How to play :
You just use the py main.py command and the game starts.
The game chooses randomly combination in letters ['R','G','B','Y','W','M']
The game is gonna ask you a combination of 4 letters in RGBYWM. Only use these letters to play in the right order. As example :
RGBY will play 1 : red, 2 : green, 3 : blue, 4 : yellow.
Once you played, the board is displayed with each combination you ever played and an "indicator".
The indicator is composed of 4 points (the order of the points doesnt matter, as same as the real game).
a red point means that a point you played is not in the combination to find 
a blue point means that a point you played is in the combination to find 
a green point means that a point you played is in the combination to find

As example, if the combination choosen is RGBY, the play RBGW is gonna display:
-1 red point (W not in the combination)
-1 green point (R in the combination, at the right place)
-2 blue points (B and G both in the combination)
have fun !
