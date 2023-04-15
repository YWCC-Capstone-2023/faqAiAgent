# Purpose
The FAQ AI Bot was created to provide quick and efficient answers to common questions for students in the YWCC Capstone Class. Before the creation of the bot, students would have to wait anywhere from a few minutes to a few hours for an answer to their question on the YWCC Capstone Discord server. This bot helps eliminate waiting times for students as the bot is capable of providing answers within seconds. The bot also helps the professor and the Capstone Operations Team focus their resources in other areas of the program that need to be addressed. <br><br>

# How It Works
The questions we gathered were from the YWCC Capstone Discord server that contains all sections of IS, IT, and CS 491 classes. After identifying the server(s) students asked their questions in, a Google Sheets was created to store all the questions asked along with the answers that the professor or operations team provided. Google Sheets was used for it's quick collaboration between the FAQ AI Bot Team, and serves as an intuitive and simple data base to pass on to future FAQ teams without the need of downloading extra software. The Sheet contains 4 columns - Questions (patterns), Answers (responses), Tag, and Variable Required. These sections can be explained through the runbook here **<LINK>.** and the Google Sheet can be found here <Link>.
  
After creation of the Sheets, we used Python as our choice of coding language to develop the bot that could be used on the YWCC Capstone Channel. Python was used because ... To make changes to the bot or view the documentation, follow the runbook here <Link>. <br><br>

# How To Use The Bot
The Bot utilizes simple commands in order to ask it questions within the Discord server. Follow the examples below to see how to interact with the bot:

## /ask
This command is used for the bot to understand a question is about to be asked. The command is then followed by the question the user will ask.</br>
  ```
  /ask When is the Open house?
  /ask Do I have to attend the Open house?
  ```
  
## /refresh
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor purus sit amet elit malesuada, non pellentesque magna venenatis. Praesent quis aliquam nibh. Nulla facilisi.
 ```
 /refresh
 ```
## /add
  This command is used by users who think that there is an important broad question that is missing from the excel sheet. Following the command would be the question followed by a '?' and then the answer which will automatically populate the excel sheet. The FAQ Bot Team will need to review and refine it for the bot to properly query it in the future for other students to use. 
  ```
  /add Is this a proper question? Yes it is
  /add Do Co-PMS need to submit PM evaluation sheets? No they do not, they are PMs.
  ```

## /help
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor purus sit amet elit malesuada, non pellentesque magna venenatis. Praesent quis aliquam nibh. Nulla facilisi.
 ```
 /help
 ```
