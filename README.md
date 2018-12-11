# Political Bias Detector Chrome extension

**Note:** Due to the large size of the word embedding matrix, it was uploaded to Google Drive and can be downloaded **[here](https://drive.google.com/open?id=1bSX5V_2N5PN9eYEq9KEN2PsVPJXWIn87)**
Extract the ```model.tar.gz``` file directly to the project directory.

## Load the extension
To load the extension into Google Chrome:
1. Open Google Chrome
2. Type ```chrome://extensions/``` in the address bar
3. Enable **Developer Mode** at the top right corner
4. Select **Load unpacked**
5. Select the *folder* **Chrome extension** in the project directory. The extension should be loaded

## Run the extension
1. Open a terminal window in the project directory and run the command: ```python3 app.py``` or ```python app.py``` (Flask must be installed in your system)
2. Once the server is running, the extension will display political ideologies results when users navigate to news articles on the following sites:
  * Huffington Post
  * The Guardian
  * Slate
  * NPR
  * The Economist
  * New York Times
  * Fox News
  * CNN
  * Breitbart
  * The Blaze
  * Wall Street Journal
  * BBC
  * Bloomberg
  * Medium
