# Angel Oak 🍂
### Bring Order to Your Most Chaotic Folders

Here's a fun little Python script you can run from your terminal. Pick your messiest, most dauntingly undermaintained folder, and blink. *Done.* Angel Oak sorts all your unsorted crud into neat little subfolders based on file extension. Hooray! It also creates a handy output log upon completion, which is placed in the target directory.

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

From your terminal, navigate to the directory where you downloaded Angel Oak.

~~~
cd Downloads/angel-oak
~~~

When you run the script via `python main.py`, you'll be prompted to enter a target directory and a name for the output log.

~~~
python main.py
Enter path of directory to be sorted: 
Enter name for output log:
~~~

Complete the prompts and *kuh-blam.* You're all set! Now grab a second (or third) coffee and admire how organized you are. 🙌
