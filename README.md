# Angel Oak 🍂
### Trim up your overgrown directories

Here's a fun little Python script you can run from your terminal. Pick your messiest, most dauntingly undermaintained directory, and blink. *Done.* Angel Oak sorts all your unsorted crud into neat little subdirectories based on file extension. Hooray! It also creates a handy output log upon completion, which is placed in the target directory.

Here's the directory tree you can expect after running the script:

~~~
└── your-target-directory
    ├── Audio
    ├── Docs
    ├── Folders
    ├── Images
    ├── MISC
    ├── Packages
    ├── Programs
    ├── Video
    ├── Web_Pages
    └── all_clean.txt
~~~

> [!NOTE]
> As the universe of file extensions continues to expand, it's impossible to account for all of them. But I've covered the most common ones.

### Running the Script

Make sure you have Python installed on your system, and [install](https://www.python.org/downloads/) if needed.

~~~
python --version
~~~

> [!IMPORTANT]
> **MacOS users:** If you receive the error `zsh: command not found: python`, try the following: `echo "alias python=/usr/local/bin/python3" >> ~/.zshrc`.

Clone the Angel Oak repo or download the .zip from the "<> Code" dropdown above. Then, in your terminal, navigate to `angel-oak` (clone) or `angle-oak-main` (.zip). For the best results, move Angel Oak **outside** of the directory you'd like to sort.

~~~
cd Desktop/angel-oak-main
~~~

When you run the script via `python main.py`, you'll be prompted to enter a target directory and a name for the output log.

~~~
python main.py
Enter path of directory to be sorted: 
Enter name for output log:
~~~

Complete the prompts and *kuh-blam.* You're all set! Now grab a second (or third) coffee and admire how organized you are. 🙌
