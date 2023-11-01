# Start.gg Player Stream Deck Integration
Uses start.gg API calls to pull player names for tournaments and save them in text files

## Setup
1. Install Python 3.11
2. Download files
3. Edit PlayerNameSync.pyw
    * Edit line 9 to contain the name of your tournament in Start.gg
    * Replace API_TOKEN in line 27 with your API token
    * Edit the filenames in lines 43 and 47 to point to the appropriate folder
4. Create text elements in OBS that point to LeftPlayerName.txt and RightPlayerName.txt
5. Create an action in Elgato Stream Deck
    * Create a "System > Open" action
    * In "App / File", fill in with '"PATH_TO_PYTHON" "PATH_TO_PLAYER_NAME_SYNC_SCRIPT"'
    * Example:
      * "C:\Users\User\AppData\Local\Programs\Python\Python311\pythonw.exe" "C:\Users\User\Documents\Streaming\Smash Controls\PlayerNameSync.pyw"

## Use
1. In your Start.gg tournament, open the match that will play on stream
2. Click "Stream: Any"
3. Select the stream queue (can be named anything, create one if it doesn't exist)
4. Press the action created earlier in Stream Deck to sync player names to the files
