# Slithering Python

1. Make sure you have Python 3 and pipenv installed.

2. Go to the directory with the `Pipfile` and run
   ```
   pipenv install
   ```

3. After the install completes, run
   ```
   pipenv shell
   ```
   This will get you into the virtual environment. At this point, you should be able to run Python 3 by just running `python`:

  python3 <filename>

   ```
   $ python --version
   Python 3.6.5
   ```

   You can exit the virtual environment by typing `exit()`.

# rooms

rooms are 2 ways

# player

# inventory

# monsters

# hp

# lives

W: &#8592;
N:
E:
S:

🔦
🗺️

inventory = ['🔦', '🗺️']
for i in inventory:
    print(i)




So you can just add properties to an instance of a class by assigning it a value even though it wasn’t declared in the class itself? (e.g. `room['outside'].n_to = room['foyer']` works even though we never said that the Room class had a property called `n_to`)

PYTHON for graphics, computation, AI
