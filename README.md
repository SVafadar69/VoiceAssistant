# VoiceAssistant

Voice Assistant written entirely in Python, that performs numerous functions, primarily leveraging the abilites of OpenAIs public AIs GPT3, Dalle-2. The Voice Assistant is capable of other tasks, such as opening files, doing wolfram alpha queries, returning stock information, and more. Further incorporations of ChatGPT3 will include auto-applications of the AI based off Voice. Codex is currently not integrated in the application, but may be done so in coming days. 

The purpose of this repository is two fold: 
1) To increase productivity while interfacing with computers using voice (voice is faster than purely typing)
2) Leverage the AI abilities of OpenAI's public AIs. 

As the abilities of the AIs created by OpenAI are incredibly beneficial for individuals, their benefits can be leveraged in an easy-to-use format. The inclusion of other modules (Wolfram Alpha Search, Google Browser Open, etc.) are common use-cases an individual might need while trying to leverage the abilities of their computer. 

Note: You will need your own API key from Open AI. It is available here: `https://beta.openai.com/account/api-keys`
You will also require an API key to perform the scientific queries using Wolfram Alpha. Obtaining the key can be done here: `https://developer.wolframalpha.com/portal/myapps/`

To get started, start by cloning the repo: `https://github.com/SVafadar69/VoiceAssistant.git`.

__If you want to run the entire project, install anaconda, and proceed with the installations below. If you only want to run the OpenAI portion of the program, skip the following commands and proceed to the requirements.txt installation below.__

Next, you will need to install the following packages with anaconda. To do do, you first need to install Anaconda here: `https://www.anaconda.com/products/distribution`.

Next, run the following commands in your terminal: 

`install anaconda
conda activate chatting 
conda install selenium
conda install arrow
conda install statsmodel`

These will download all the dependencies needed to run all files of the voice assistant. If you want to run just the OpenAI files, they are not needed for installation. 

After, run this command `conda create -n chatting -> click yes `.

`pip install -r requirements.txt`. All the necessary packages for the project will download. The only bits of the code personable to you will be the email provided in `email.py`. 

