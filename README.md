# majsoul-score-display
A really inefficient, roundabout way to try and pull the current score in a live mahjongsoul match, apply rank bonuses and output it in a way suitable for casting. In python!

It was a good excuse for me to try and learn python while making something at least slightly useful to someone, hopefully, ahaha. It requires that the game you're spectating is happening on the main monitor of a multi monitor setup and it's tailored to my screen resolution (1920 by 1080) although it's definitely possible to go in and edit values for which pixels pyatuogui should be looking for.

What this does:

- Uses Tesseract to attempt to interpret score (I honestly don't remember how I got Tesseract to work, but I'm sure it's a lot easier to do than it felt to me at the time.)
- Applies a customisable rank bonus to the ingame score to predict the final outcome of the match
- Accepts an input for starting score on launch (For longer league formats)
- Outputs: The predicted change in score for the current match (top), the current score in the match (middle) and the predicted final score given the initial score input (bottom). Currently it colour codes the final scores based on who has the most points, it was made for the final of an event so there'd be a player very clearly in 1st, 2nd and 3rd...
- On a key press of 1 (default): It will attempt to take screenshots of the ingame scores, update the display, then automatically switch the perspective to the player to the right. Ideally this is to be used when the dealer switches.
- On a key press of 3 (default): It will attempt to take screenshots of the ingame scores and update the display but will not switch perspective. This is meant for when the dealer earns a repeat.

What this does not do but it would be great if it would:

- Accept starting scores from an external file/webpage, if it did you could display that player's current rank in the event, for example
- Output finished scores to an external file
- Rarely Tesseract will encounter trouble reading, if it doesn't seem to want to update it'll keep trying every 2 seconds and will get there eventually, but if there's a number it really can't read you may have to wait until the next hand for an update
- Work when the starting score is *not* 25,000 all
- Work when the gap between two players is less than 5000 while one is +ve and one -ve or if there are more than 5 riichi sticks in the pot for a hand (This could be fixed if you took scores by another method, or were able to train Tesseract into reading the riichi stick count's font, the problem's here because I have a sanity check which makes sure all the scores total to between 95,000 and 100,000, but knowing the amount of riichi sticks lets me know the total score at all times instead of just setting a tolerance)

Example of raw output:

![Raw output](https://cdn.discordapp.com/attachments/270668804030201856/971417364887396372/unknown.png)

Example of how it looks after doing OBS alchemy:

![I never lined it up quite right, well I should fix that before the next one](https://cdn.discordapp.com/attachments/270668804030201856/971417921349902386/unknown.png)
