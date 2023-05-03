
# Purpose
The FAQ AI Bot was created to provide quick and efficient answers to common questions for students in the YWCC Capstone Class. Before the creation of the bot, students would have to wait anywhere from a few minutes to a few hours for an answer to their question on the YWCC Capstone Discord server. This bot helps eliminate waiting times for students as the bot is capable of providing answers within seconds. The bot also helps the professor and the Capstone Operations Team focus their resources in other areas of the program that need to be addressed.

# How It Works
The questions we gathered were from the YWCC Capstone Discord server that contains all sections of IS, IT, and CS 491 classes. After identifying the server(s) students asked their questions in, a Google Sheets was created to store all the questions asked along with the answers that the professor or operations team provided. Google Sheets was used for it's quick collaboration between the FAQ AI Bot Team, and serves as an intuitive and simple data base to pass on to future FAQ teams without the need of downloading extra software. The Sheet contains 4 columns - Questions (patterns), Answers (responses), Tag, and Variable Required. These sections can be explained through the RunBook [here](https://docs.google.com/document/d/10CepY-fEfIVmCnIb1tU2k7zSC41Usgvq4Mhn-z8GRL0/edit?usp=sharing) and the Google Sheet can be found [here](https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/edit?usp=sharing).

# How To Use The Bot
The Bot utilizes simple commands in order to ask it questions within the Discord server. Follow the examples below to see how to interact with the bot:

## Setting up the bot environment
### Prerequisites

-   `credentials` directory with the following files:
    -   `service_account_credentials.json`: Contains the credentials for a Google Sheets service account, required for accessing Google Sheets API.
    -   `config.json`: Contains the configuration settings for the Discord bot, including token and command prefix.
### Setup
-  Clone the repository.
-  Install the required libraries using `pip` or `conda` located in `docs/requirements.txt` in your working directory:

	```python
	pip install -r docs/requirements.txt
	```

-  Replace the `SPREADSHEET` variable in the cogs/ask file with the URL of your Google Sheets spreadsheet containing question and answer data.
### Usage

1.  Make sure the required prerequisites are met and the configuration files are present in the `credentials` directory.
2.  Run the script using `python bot.py` command.
3.  The bot will log in to Discord using the provided token and set up event handlers for handling Discord events, such as `on_ready` for bot readiness.
4.  The bot will load all the commands from the `/cogs` directory by calling the `load_extension()` function for each Python file with `.py` extension.
5.  Once the bot is ready, it will be able to respond to commands with the specified command prefix, and the logging output will be written to `docs/discord.log` file.

Note: The bot provides two custom commands, `/load` and `/unload`, for loading and unloading extensions (cogs) respectively, which are defined in the script, but please use the `/reload` command instead as this implementation is more secure.

## /ask
This code implements a Discord bot cog for the `/ask` command using the `discord.py` library. The bot responds to questions asked by users by fetching answers from a Google Sheets spreadsheet containing question and answer data. The bot uses the `neuralintents` library to train a machine learning model to understand and respond to questions.
### Usage
- In your Discord server, use the `/ask` command followed by your question to ask the bot a question. For example: `/ask Wh`
- The bot will fetch the answer from the Google Sheets spreadsheet and respond with the answer in an embedded message.
  ```
  /ask When is the Open house?
  ```
- Bot response  
 ![example ask response](https://drive.google.com/uc?id=1wbDYmRXhW6XzhT52i36ZojQIpp9ZBDlp)
## /refresh
This code contains a Discord bot command cog for the `/reload` command on FaqAiBot. The "/reload" command allows an administrator to reload the bot's cogs, which are modular components of the bot that handle different functionalities.

### Features

-   The "/reload" command is only accessible to users with the "administrator" permission.
-   Upon running the `/reload` command, the bot will display a dropdown menu with options to choose which cog to reload.
-   After selecting a cog from the dropdown menu, the bot will unload and then reload the selected cog.
-   The bot will send a message to notify everyone in the server that the selected cog will be temporarily down for less than a minute.
-   The bot will update an embed with fields indicating the cogs that were successfully reloaded and any cogs that failed to reload with the corresponding error messages.
-   Once the cog is reloaded, the bot will send a follow-up message notifying that the selected cog is back up and running.

### Usage

-   Run the `/reload` command in a server where the bot is installed.
-   Select the cog you want to reload from the dropdown menu.
-   Wait for the bot to unload and reload the selected cog.
-   Once the cog is reloaded, the bot will send a follow-up message to notify that the cog is back up and running.
 
 ```python
 /refresh
 ```
   -	example bot Response  
![example reload command](https://drive.google.com/uc?id=15_0uyPcfv8OIP3shrRPLNmbLfd0MooAR)

## /add

This code contains a Discord bot command cog called `/add`, which allows users to add questions, answers, and tags to a database.

### Features

-   The code defines a Discord UI Modal called AddModal, which is used for inputting the question, answer, and tag values in a user-friendly way using Discord UI components.
-   The AddModal has an on_submit method that is triggered when the user submits the input values. The method retrieves the values of the question, answer, and tag inputs, and sends a confirmation message to the user.
-   The code also defines a Discord cog called Add, which is a command cog for handling the /add command. The command is used to open the AddModal and allow users to add question, answer, and tag values to the database.
-   The Add cog has error handling for checking if the user has the necessary permissions to use the /add command and logging any errors that may occur during command execution.

### Usage

- Run the `/add` command and input the question, answer, and tag set into the discord UI modal
  - example add Modal  
![example add modal](https://drive.google.com/uc?id=1j2zaEaVJLxbadpix1ecgG0zMHfBK5NHM)
### Future Considerations

-   The code currently uses Google Sheets for storing the question, answer, and tag values, but it may be prudent to move to a more robust database solution like MySQL in the future.
-   The code could benefit from additional error handling and input validation to ensure the data entered by users is valid and secure.
-   The code could be extended to include more features like editing existing question, answer, and tag values, deleting question, answer, and tag values, and searching for question, answer, and tag values.


## /help
The Help class is a cog for a `/help` command in a Discord bot. It extends the commands.Cog class from discord.py and provides a hybrid command `help` that sends an embed with a title "Help" and a description "Need Help? Here's a List of Commands!" when invoked. The `view` object for the embed includes an instance of the HelpSelect class, which generates the help select dropdown.
### Usage
- Run the `/help` command and choose a command from the dropdown menu for a detailed list of the commands and options available 
 - example help dropdown  
![example help dropdown](https://drive.google.com/uc?id=1dEOA1iEshr8ull4hRd1heTJghLv2Ur2a)
 
 
