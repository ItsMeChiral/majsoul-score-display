# majsoul-score-display
A really inefficient, roundabout way to try and pull the current score in a live mahjongsoul match, apply rank bonuses and output it in a way suitable for casting. In python!

It was a good excuse for me to try and learn python while making something at least slightly useful to someone, hopefully, ahaha

What this does:

- Uses Tesseract to attempt to interpret score (I honestly don't remember how I got Tesseract to work, but I'm sure it's a lot easier to do than it felt to me at the time.)
- Applies a customisable rank bonus to the ingame score to predict the final outcome of the match
- Accepts an input for starting score on launch
- Outputs: The predicted change in score for the current match (top), the current score in the match (middle) and the predicted final score given the initial score input (bottom). Currently it colour codes the final scores based on who has the most points, it was made for the final of an event so only 4 players were left.
- On a key press of 1 (default): It will attempt to take screenshots of the ingame scores, update the display, then automatically switch the perspective to the player to the right. Ideally this is to be used when the dealer switches.
- On a key press of 3 (default): It will attempt to take screenshots of the ingame scores and update the display but will not switch perspective. This is meant for when the dealer earns a repeat.

What this does not do but it would be cool if it would:

- Accept starting scores from an external file, if it did you could display that player's current rank in the event, for example
- Output finished scores to an external file
- Work when two players are between 5000/-5000 points where one player is +ve and one -ve or if there are more than 5 riichi sticks in the pot for a hand (This could be fixed if you took scores by another method, or were able to train Tesseract into reading the riichi stick count, the problem's here because I have a sanity check which makes sure all the scores total to between 95,000 and 100,000, but knowing the amount of riichi sticks lets me know the total score at all times instead of just setting a tolerance)
