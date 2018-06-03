# receiptData

Software for tracking (my food) purchases

## Usage

Create a `stores.txt` file (it can be empty), and a folder called `./receipts`

```bash
touch stores.txt
mkdir receipts
```

```bash
python3 main.py
```

Follow the following prompts.

It will try to save in `./receipts`

## Configuration Files

`stores.txt`

Generate this file when you download this repository. It may be empty.

Store names are separated by newlines. Lines with only whitespace on them are omitted.

## TODO

* have the program create the `./receipts` folder when saving the first receipt
* make not crash when the `stores.txt` file does not exist
* make program enter new stores into the `stores.txt` file that it has not seen before
