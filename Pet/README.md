# Pet
Pet is a vanilla Python game inspired by Tamagotchi!

## 🔨 Usage
```bash
git clone https://github.com/xyntechx/Python-Projects.git
```
```bash
cd Python-Projects/Pet
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```

## 🗺 Folder Structure
[`main.py`](https://github.com/xyntechx/Python-Projects/blob/main/Pet/main.py): main program to run

[`pet.py`](https://github.com/xyntechx/Python-Projects/blob/main/Pet/pet.py): Pet class (+ subclasses) definition

[`utility.py`](https://github.com/xyntechx/Python-Projects/blob/main/Pet/utility.py): miscellaneous functions

[`keyboard_settings.py`](https://github.com/xyntechx/Python-Projects/blob/main/Pet/keyboard_settings.py): set up keyboard listener

[`colours.py`](https://github.com/xyntechx/Python-Projects/blob/main/Pet/colours.py): initialise colours

## 👾 How to Play
See the instructions below to learn how to play Pet!

### 📖 Backstory
Congratulations! You have just adopted a brand new pet!

After naming your pet, you soon realise that it's very vulnerable. Your pet gets easily hungry, thirsty, tired, lethargic, and sad. As a responsible owner, you vow to keep your pet alive for as long as possible before it's beyond help.

### 📊 Stats
Your pet has a total of 5 stats:
- hunger
- thirst
- energy
- fitness
- mental health

If any of the above stats reaches `0`, it's game over!

### 🪜 Levels
`Level 1`: **3 stats** in play, stats drop every **3 seconds**

`Level 2`: **4 stats** in play, stats drop every **3 seconds**

`Level 3`: **4 stats** in play, stats drop every **2 seconds**

`Level 4`: **5 stats** in play, stats drop every **2 seconds**

`Level 5`: **5 stats** in play, stats drop every **1 second**

### ❤️ Taking Care of Your Pet
Press these keys to take care of your pet:

`h`: Feed your pet (hunger)

`t`: Give your pet a drink (thirst)

`e`: Let your pet sleep (energy)

`f`: Make your pet exercise (fitness)

`m`: Play with your pet (mental health)

Every time you press any of the above keys, the corresponding stat will increase by `1`.
