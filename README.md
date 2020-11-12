## About info
The project records the keyboard input, mouse input, and screenshot from a target computer. Combined with proper NLP methods and image processing, the logger can steal sensitive information, such as username, password, or email to the attacker.

## Log Options
### Text:
format: `timestamp    button action    coordinateX,coordinateY`
### Json:
format:
```
{
    records: [
        {
            button: button1,
            coordinates: [coordinateX,coordinateY],
            is_on_press: True/False,
            timestamp: ts
        }
        {
            button: button2,
            coordinates: [coordinateX,coordinateY],
            is_on_press: True/False,
            timestamp: ts
        }
        .
        .
        .
        {
            button: buttonN,
            coordinates: [coordinateX,coordinateY],
            is_on_press: True/False,
            timestamp: ts
        }
    ],
    timestamp: ts
}
```

## Samples
> - sample1
<img src="./samples/mouse_log_text.png" alt="drawing" width="500"/>

> - sample2
<img src="./samples/keyboard_log_text.png" alt="drawing" width="500"/>

## Installation
`git clone https://github.com/yuan64198/InputLogger.git`

## Requirements
> - pynput
> - pyscreenshot

or

`conda install --yes --file requirements.txt` in conda environments

## Run the Code
`python main.py`

