
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
	pip install docs/requirements.txt
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
 ![example ask response](https://lh3.googleusercontent.com/rLhvymZsChGP3mS83YKhTlPsuI386hOU_tiGGlhkI4d7v8aq6aySQy9tidOXTyZKbFwxSKpzGStF0n9HqPgAMAh4FZuPonIYHRvjRHGAIrME-7wQWMLyXHRK4UYaGgTgiJufFKw9AEJtTAuRsD-xPTigkssYVf2gCYunZnCSsKQAUrPpo7SQCXnYeMAZLYNUuLka1lbca8Ao6NHziGcXFlXqXn5YlzQTGx-z7-99xztb99twPrPTsekrwXJCrq5Utu91NlQ6Wg_dSQfuJJmtDFnwwTmRBFnvyjP058VJCmX5FKCAZT7_sFBE-Cc5cfeD4Cv4cbHMpgbpkBHip_Bjraljk-7AOgKm9dtxfO20d04pzDZ0ybVolt4_FJy28Wf1wk29v4-Zal-xvnxVBZCgTMsTwdpSsG8o9uNd-wDpSWLqIxO_UiQktFHdfi-Ho8pNR62BmfvvTiIEUQyaqfbaVvvaVERFvMjqzDhTPcR_Vlnc3yFZuFBFyOVFQCqICDMDilcSIEXl8A9jUC07wsdY5C4-LwuaZMm3HRlDhTm3wUJu6N4EmSjRDyn9xDzsK8S9KvbmXRVVosA32nBQnOsPOZJNXrYleIBs5K5DBM1DB5TOnvXZsf0M9qk_QTZAWhiW1ITsiJwRPUriVGz4HSugykxP2LtaenicXY-KRQuqTzjwqKfd-ibIxga9rvwdwA-_4zGJutDF52tRd-DlturhxOl0mkzG0nAal0gr6XoVrLfsUmK7wZfy8uaBvUrxiyjjHQZo53PcOJFYQyyKUrNRMsSHu4SOGmBKUe-MOgHM6_PQTV9MQr3WJ500f6e1EDorSxVeiiYjvQIIEanlhNM79H-j3bh7W53yxzmhXXaxhhMH4H03dc97u0BDxc5wsk3dBMnJvidYU9Uh1C3kdU0eUSh1MMNqLCqipzalYpHfFriUPQt8z61t2mEls9b7Z9dV8dFm02-X760LDE1NeF6ejdbQVolinoVz6LNo1sVb5pYYxMk5GvmpJw=w717-h163-s-no?authuser=1)
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
![example reload command](https://lh3.googleusercontent.com/wFYWxgSMxVZO-qCKf8cyHShFk0UaAl-ql1WuoS1ikLqyQNMSYu4Zrnm32KTYQe0wyNdif6AuXYaqgwJxzesjlxgYbqWlOO5AlVk5AsbTnq4e_55xP6oO04V6qEoWEpoCw7SNmXtI4CEC2kjR9-H89QcLFcQB_eBXM387PGB3mRsxsuQW50dBkT3eO_bY8ZU4ihBdch5wIpxNN2bGviurlqUU9F0tp_pL8kVOYJdzJk4bc_q_j1y5RNu74Sx4AejGh3P0jzDuxKKfoxEXNtb_zAEFUKDbaKWE4bn9P_fmofUrye5WhjL_MJvDPwCZVlF_HPgedZdp4UdaTFdK8J1beC7oM9GKcBUbYLQk0kVly64cGnP8pfSHcFQzV3iduSi7SXR4WmWBdzdT7cYaKmPKmbAreA3StGUGXCODXTQrjB5nn2792d8w8tQyGk5xg6vSjFhqEO4d5zHE1ZMxZsJJ4nre4lThVBzMtbCQrdClJphHzlOImbyOzd-wff3ivVY8843EgORDSvtWnFl6BfgfszBXLsgD89yhUT9ncFjW45TeCSlx9U53P4STNfeFKgx8SE3kK97nt_5UpUpaV3O3iqGOpO7QWIFOD_UDoWpbbyd0Z1WKAUH3usx5UUcWQMuLB47UaRdmPpVPVusIIcbvWUQv1hMJLBf9dmMGEbLCR_qr7WcDNvgKyUVhzzJsZbQNF9qvzoDpX6trFQsZuJQiabASeQ8kUghgBasEMRPh8EN9r4PFvzpUTsPPYpRmwknASabfGsq5XF32jODtDhejZiJ7GGejB8b9Gntm44pLJ__EYGDRZLx38GF8qbymZZrydWZLkbrmamPJJ7QMyET1A5csSbKbpqMpuP9qGKm8HqH0v5HWTqO-R-Z380nitl2cm7O0FwxD9YL2m6CcDbLizJYYCRJt4pjlsFQZeH3QWS5pk_gLYZqNYtpWszDE5v4NX9oTYhMZyvXtlT4_b1Zy0snQ2LO8uJoTmwf8bcqdi8ADzraIeYEKyg=w716-h400-s-no?authuser=1)
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
![example add modal](https://lh3.googleusercontent.com/T4sR24XiK1KS0_gsxzpth0BUAGt-TfkehhP-bHzlOidH9R7g_xeJ7-9ocEGtN_-ImkK7wHlVf7Sa1Nybb7rwGtLnUYzCt4Q4RbcZZSHdxSjjP8Zpq5T2L0fhBGE-OHVaWyS8n2_x_7hyNnZDHALjwz7vr6026asKrjxCh7-wh8WPa8Cj0lXnPVde4vVHVKukWRN-822jz6bBeGLD8YYcZlC893NUrWVOGRZVEOF4NPEUeq02dI1IxC1yUR_tupIMV4tqJJ0tfN4TFOnYMGijdHvAXnDG1wrAJnnxEcfMArLB1Xq_AV78sU3hLAqJxSPsy8IX1Rf-FGJ6EZYwTp7mni1ygEmYgI8IYEPzjvT3xDkuMD5-osIxtADvL5czHOerjfWx6sUOKaUXpXE2VGgPApmRpMXfW46LoX7SQMy9HUOxNxiaD8DTmOQgVSusOCX6wMtaCHzzw3b9HHTGJ9h78s_XwKRnASNwDD7MO2pcmlyFDOLmhqqoQqnkcfH3hRCPJvgGJsrTtqW7wPTu9TnbqLNaAdhByUU-_vVnZ7_Wf_CwpRsHHMvma2J4jd4553Nr-qQhSdw-VgRqLJ71YPFvkAF-eMoXckcavTYx5jdEfoIaYDudRZ636fVtHVn0x-fc19k0G3xoPyudXoTahtjTUVu5ez2fazmN84BAju0uhqialXMoQk9zKO-7tN-hYHMmTXzoYfrD731PZ0HnH5TuZNiXZbMWXK8QwcA8kdBsaDZWZOknzR4Eo0REHPYVuKhK8gJw0RlghfU9FT-ufy4Mboz7vHmnkZRXNScdkQstEFXpisSP86qn9FIZG2ug1hbIn1Z__GhDHehb3nBwYsnWxBr842E7Lx9YnvI_lNsMgsynOmviy69w9TFc9gjrf6NB-q7ZvlrGmxdqWkW_iT8aimuaBEdLDIo8RFVlaVKR2wIFxz2daXJi9QKVFNFoNyUOukvWsX0a3xl-uJi1k6RKy-GOhHTUNKkQnvEPLZ0h13Srtnd1kQQwCw=w443-h534-s-no?authuser=1)
### Future Considerations

-   The code currently uses Google Sheets for storing the question, answer, and tag values, but it may be prudent to move to a more robust database solution like MySQL in the future.
-   The code could benefit from additional error handling and input validation to ensure the data entered by users is valid and secure.
-   The code could be extended to include more features like editing existing question, answer, and tag values, deleting question, answer, and tag values, and searching for question, answer, and tag values.


## /help
The Help class is a cog for a `/help` command in a Discord bot. It extends the commands.Cog class from discord.py and provides a hybrid command `help` that sends an embed with a title "Help" and a description "Need Help? Here's a List of Commands!" when invoked. The `view` object for the embed includes an instance of the HelpSelect class, which generates the help select dropdown.
### Usage
- Run the `/help` command and choose a command from the dropdown menu for a detailed list of the commands and options available 
 - example help dropdown  
![example help dropdown](https://lh3.googleusercontent.com/eMW-MyFVLcZiMuVTtvgzvilWyBcRaV6MdB_Y3Lbh2KT-gtC_UyoNdxosCONyi2cKAbypfciMYzCF8ggKtF_q4lQnpmQqQ2inlr14dySLrdVOn1bG7V-0y9-AkSR27tam1uhAabrI4gAhIY5rT_JMmlfersHKtUJ3TpwxKN6AEoPqdTdjHiusIhbBgoRrjm22Jut12uIttKU63yt0qm4uTXMe6Ucr8DC9OYdqubVSpkVkyp0DDmkvmiIQQdQYWZ8cNMBVDPJYmzk50WvIN5mbzual8GB_BewQrrB_LecRDBZlzlgLIVo2iE_pQZkI5kgWMRzZ4e54GKHREGhHk_TQvRmgmE1wIzwb0QYkMdvQN8h0rsmVDS-r8dh5gt2unShgzSFAAhl6smuNbEVZ8sVr1ipr76qaR-2X7qhCbJ2ssqEAR_R5MxI9lr0Y9WVFy0HnTNw9cToxyBHoKOxZQHnKqJt8Yqjcs8oC21-Z9rYyGAuSGs80xXATcVPRNKW0OcPOEILIzUzhu3Y0xTdE-BjAtMrcfSLnBFl-n8zRT5ltD0ZBxJUbeRQD_Eb4Kwex6CEBCa3KPJxf9KNYudAw3pX11z0xvtdwYqiNHOrWjJoGzdxpZZWOpobUCyWSP3KPWv3RwIQWp38CrLU9gSfMALgOo5fpeaNj5Qa6Eh9mR5y-iR1ClVkeSeCEcMBNR4hS0sKJjAe2JsmZibryLI_8ima0pjmPx559abuP8yJM3jcGvdtQz1_ciiMjN2BFDcQR5hT9uB1eqCGl0_qKprLjc3aoidsHh7GSCZF0Hx43tr2TCoSQR63AD0lv3FFQevinX97b9xll3AoQdpBRNnKeiiUVM3C_YhimKxLXSJunBMlFhmSYc_1iiGwD_FSWhFrRpu3nNSCz0z7DxuqM3IjE7pGHgWokdyyzPLIpetyrI5zCxawgSezMNUFCoxNVD4gBOle3Me3qjkv8QxoaBHKMGzEXqcDyc6-ErU4nWvJpBLB1w_CPdxRyhgVKcg=w478-h400-s-no?authuser=1)
 
 
