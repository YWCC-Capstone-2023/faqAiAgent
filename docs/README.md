# FAQ AI Agent 
## Purpose
The FAQ AI Bot was created to provide quick and efficient answers to common questions for students in the YWCC Capstone Class. Before the creation of the bot, students would have to wait anywhere from a few minutes to a few hours for an answer to their question on the YWCC Capstone Discord server. This bot helps eliminate waiting times for students as the bot is capable of providing answers within seconds. The bot also helps the professor and the Capstone Operations Team focus their resources in other areas of the program that need to be addressed. 

## How It Works
The questions we gathered were from the YWCC Capstone Discord server that contains all sections of IS, IT, and CS 491 classes. After identifying the server(s) students asked their questions in, a Google Sheets was created to store all the questions asked along with the answers that the professor or operations team provided. Google Sheets was used for it's quick collaboration between the FAQ AI Bot Team, and serves as an intuitive and simple data base to pass on to future FAQ teams without the need of downloading extra software. The Sheet contains 4 columns - Questions (patterns), Answers (responses), Tag, and Variable Required. These sections can be explained through the runbook here **<LINK>.** and the Google Sheet can be found here <Link>.
  
After creation of the Sheets, we used Python as our choice of coding language to develop the bot that could be used on the YWCC Capstone Channel. Python was used because ... To make changes to the bot or view the documentation, follow the runbook here <Link>. 

  
## How To Use The Bot
The Bot utilizes simple commands in order to ask it questions within the Discord server. Follow the examples below to see how to interact with the bot:

### Commands 
#### /ask
  The /ask command is the most used command the bot interacts with. This pre-text is needed before the user inputs their question for the bot. The /ask tells the bot that the user is asking a question and that it must identify what is being asked (Mix of column A and D in the Sheet) and find an answer for it (column B).
#### /refresh
#### /add
  The /add feature is to be used by users who think that there is an important question that is missing from the excel sheet. The user utilizes the command when the question they tried to ask the bot was not found, but feel like it is a broad question that needs to be implemented in the database. Following the /add command would be the question and then the answer in which the user wants added to the Sheet. AFter hitting enter, the question and answer will automatically populate the excel sheet with the FAQ Bot Team needing to review and refine it for the bot to properly query it in the future for other students to use. When asking the question, students must cloe it with a '?' to let the bot know that is the end of the question, and the words that follow after the '?/ is the answer. Example:
  ```
  /add Is this a proper question? Yes it is
  ```
  "Is this a proper question?" Would be added in Column A, and "Yes it is" would be added in column B on the Sheet. 
#### /help
