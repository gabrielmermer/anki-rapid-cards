# Anki Rapid Cards 

Anki Rapid Cards is a Python script that will help you with making Anki cards quickly.

It works by taking your input and turing it into a .csv file that you can import straight into Anki.

## Features

* quick file naming
* tag support
* mobile friendly

## Installation

Simply clone the repository and launch `anki-rapid-cards.py`.

## Usage

### Date

select a file name and press `enter`


The script will then create a new file with the name you selected and current date.

eg. `2020-08-25--history.csv`

### Tags

Write cards tag (or leave blank for none), and press `enter` 

The tag you chose will be appended to all the cards that you will make.

### Cards writing

The process of adding new cards goes as follows:

`0 > this is front side of the card (the number represents the amount of cards made)`

(press `enter`)


`0 >> this is back side of the card`

(press `enter` again)

if you are done simply press `.` followed by `enter`.


### Made an error while making a card?
Simply open the .csv file after you're done and fix the erros in one batch before importing the file into Anki.


### Mobile
This script can work on Android devices running Termux, and syncing the working directory to computer for imports (via Syncthing).

The above setup works well with external keyboard.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
