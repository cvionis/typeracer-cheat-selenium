# typeracer-cheat-selenium
Automatically fill input with prompt text in a type-racing match on typeracer.com

<b>Limitations to Consider:</b></br>
- Upon achieving a high wpm for the first time, typeracer users are required to verify that they aren't cheating with a timed test. As the test's prompt is image-based, it can't be scraped by this script.
- If the script is used to achieve a typing rate above the user's own capabilities, the user won't be able to verify his speed with the timed test and therefore the rate achieved by the script won't be considered in the user's average wpm (if the user is logged in).
- When a user's bpm reaches 350-400 wpm, the website kicks the user from the race before it finishes due to suspicions of cheating.
