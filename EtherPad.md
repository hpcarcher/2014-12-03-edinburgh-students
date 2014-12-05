# EtherPad 

## General

Typical (simple) editors:

* Windows: notepad, nano (from within GitBash).
* Linux/OSX: nano, xemacs.

Recognising prompts and how to exit: http://hpcarcher.github.io/2014-12-03-edinburgh/novice/ref/05-prompts-exits.html

---

## Version control with Git

Mario's session script: https://github.com/hpcarcher/2014-12-03-edinburgh/tree/gh-pages/archer/git)

Including the modified file names in your git commit string helps understanding what was changed when reading back through git logs.

Single line logs to view more history in the visible window:

    git log --oneline

Colours can help:

    git config --global color.ui "auto"

Git tags are labels for particular points in your history (more memorable than the magic hash strings). Often used for things like marking the revision corresponding to a release of the software, or the exact version used for a particular analysis.

    git tag -a v1 -m "version one"

Run:

    git tag -n

to see what tags you've got.

For more on tagging commits in Git, see http://git-scm.com/book/en/v2/Git-Basics-Tagging

Tags are very useful on GitHub/FigShare, as tagged releases can be assigned DOIs to be cited in other publications, later. This is good for open/reproducible research.

Can use:

    git add --interactive
    
to individually review and stage changes within each file.

    git reset HEAD somefile

will remove a file from the staging area

Third party repository hosting services:

* https://bitbucket.org/
* https://github.com/
* https://about.gitlab.com/

Remote git repositories let you push (and otherwise interact) in two main ways:

1. With an SSH public key.
2. Via HTTPS.

If you see a problem with (public-key) authentication errors, then using the https method should bypass the problem. This involves changing the origin on the respository:

    git remote rm origin
    git remote add origin https://site/username/repository

(e.g. https://bitbucket.org/lp1234/planets)

Pulling a specific branch from a remote repository:

    git pull origin other-branch

Pushing a specific branch is similar:

    git push origin yet-other-branch

More on branching in git: http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

StackOverflow discussion of forking vs cloning, on GitHub: http://stackoverflow.com/questions/3611256/forking-vs-branching-in-github

Accidentally putting sensitive data into repositories happens often enough that there's a FAQ/protocol for removing it: https://help.github.com/articles/remove-sensitive-data/

MICE (Muon Ion Cooling Experiment) MAUS analysis software:

* https://code.launchpad.net/maus/
* Uses Bazaar which is another revision control tool.
* Each developer has their own branch so they don't introduce bugs that block another developer.
* The lp:maus branch is stable and only certain project members can merge developer-specific branches into this branch.

Jekyll - blog-aware static site generator written in Ruby:

* Used by GitHub to render web pagegit branch changes.
* https://github.com/jekyll/jekyll
* Click on branch:master and then tags and see how there is one tag for each Jekyll release.
* Click on commits to see the development history.
* Click on branches to see the current branches and their status with respect to the master branch.

Taverna workflow management system:

* https://code.google.com/p/taverna/source/browse/taverna
* Uses Subversion which is another revision control tool.
* Click Changes to see the development history.
* Click Browse and explore the directories on the left - you will see trunk, branches and tags directories - in Subversion creating branches and tags involves copying. files/directories to these directories in the repository.

Visual Git Reference - pictorial representations of what Git commands do, http://marklodato.github.io/visual-git-guide/index-en.html

Pro Git - the "official" online Git book, http://git-scm.com/book

Version control by example - an acclaimed online book on version control by Eric Sink, 
http://www.ericsink.com/vcbe/

ARCHER virtual tutorial giving an overview of and introduction to using version control (using Subversion mostly, not Git):

* http://archer.ac.uk/training/virtual/2014-11-12_VersionControl/VersionControl.pdf
* http://youtu.be/qO7K-CxXWao

Git documentation, http://git-scm.com/doc

Version Control with Git, http://shop.oreilly.com/product/0636920022862.do, 2nd Edition, O'Reilly book.

---

## Building programs with Python

If the shell commands (ls, cat, etc.) aren't working in ipython, especially on Windows, try using the exclamation mark before them, e.g.:

    ls inflammation.txt

becomes

    !ls inflammation.txt

Separation of values by commas in comma-separated output can sometimes fail (and silently!), where the comma has a functional meaning, e.g. as the decimal separator (sometimes happens with files from continental Europe).

Floating point precision in iPython, https://docs.python.org/2/tutorial/floatingpoint.html

The `round()` function, and print formatting, e.g. `print("%.3f" % 4.1234567)` can be useful for representation of truncated floats.

iPython has a number of "magic commands", including `%save`, to save your work, e.g.
`%save my_session.txt 1-110`

More about magic functions, http://ipython.org/ipython-doc/dev/interactive/tutorial.html

Broken Python function example:

    def fahr_to_kelvin(temp):
        kelvin_temp = (temp - 32)*(5.0/9) + 273.15
        return kelvin_temp

Python 2 does integer division so 5/9 gives zero. C and other languages do this too, but Python 3 changes this.

Fixed Python function example:

    def fahr_to_kelvin(temp):
        kelvin_temp = (temp - 32)*(5.0/9.0) + 273.15
        return kelvin_temp

By using 5.0/9.0 we are telling Python to do floating point division, and we get 0.555... and the function should be correct.

Editing functions in iPython at the command line (rather than in the ipython notebook) can be tricky, especially if you've stepped back through history with the arrow keys: 

* The tab/space alignment can be thrown out.
* It can be awkward to edit in loops/code blocks. 

It may be easier to edit in an external file and use `run filename.py`.

Tab completion at the command-line does not work if your string to be completed starts with a wildcard, because the shell "doesn't know where to start" e.g.

`*,<TAB>` will not autocomplete

but 

`b<TAB>` will autocomplete everything that starts with the letter `b`.

At least one instance of nano wraps lines at 80 characters, and inserts a newline character. This can break long lines in Python, so that code does not run. To continue lines, you can use the line continuation character `\` to tell Python that the line carries on, on the next line. So, if your line is forced to break as:

    [...] +
    my_variable

you can fix it by making the line:

    [...] + \
    my_variable
    
Other useful Python scientific libraries:

* Bioinformatics: Biopython, http://biopython.org/wiki/Main_Page
* Graph theory: NetworkX, https://networkx.github.io
* Symbolic maths: SymPy, http://www.sympy.org/en/index.html

## Automating tasks with Make

If make is installed correctly then, when you run `make` you should see:

    make: *** No targets specified and no makefile found.  Stop.

Beware that copy-and-pasting Makefiles from online may insert spaces in your text editor, rather than the tabs, which are required.

Note that if you forget to put a tab as the continuation to a target you will get a cryptic error:

    make 
    make: Fatal error in reader: Makefile, line 3: Unexpected end of line seen

Get used to that error as you will see it quite a few times if you use make..

If you want to check whether you have a tab at the beginning of each continuation line you can do:

    cat -ntv Makefile
     1  help:
     2  ^I@echo Hello world

where:

* `-n` - gives line numbers, hence the 1, 2 etc
* `-v` : is verbose, which is what shows you the tab (rendered as a `^I`)
* `-t` : renders the tab as `^I`

The `@` at the beginning of uses of `echo` in make stops the line from repeating itself otherwise (if you removed it) you would get:

    make
    echo Hello world
    Hello world

If you put the "@" back in you get:

    make
    Hello world

If you are a vi user you can use:

    :set list
    
to show hidden characters (you will see the tabs rendered as ^I)

    :set nolist

not to show the characters.

Note that by default if you just type make it will only do the first target it encounters. If you want to run one of the other targets you have to type it explicitly:

    make last.dat

would run the second target. 

You can create a target at the top:

    all: isles.dat abyss.data last.dat

which would run all the targets.

Using Makefiles for bioinformatics pipelines, http://www.bioinformaticszen.com/post/decomplected-workflows-makefiles/

GNU Make for Reproducible Data Analysis, http://zmjones.com/make/

---

## How (and how much) to test programs

When you use someone else's code - especially for research purposes - how often do you check that it is correct (gives the correct output for defined inputs), or that the author has checked it?

Python has core system modules specific for testing (beyond scope of this session):

* test, https://docs.python.org/2/library/test.html
* unittest, https://docs.python.org/2/library/unittest.html

and these are extended in the examples used, with the nose module, http://nose.readthedocs.org/en/latest/index.html

    import os
    import os.path

    def file_exists(filename):
        if (os.path.isfile(filename)):
                print "OK ", filename, " exists"
        else:
                print "FAIL ", filename, " does not exist"

    def test_anttsp(datafile, numberofcities, outputfile):
        cmd = "python anttsp.py " + numberofcities + " " + datafile + " " + outputfile
        os.system(cmd)
        file_exists(outputfile)

    file_exists("output.pickled")
    file_exists("mumbojumbo")

    test_anttsp("data/scottish_city.pickled", "5", "myoutput.pickled")

If you need to generate the `scottish_city.pickled` file again for any reason:

    python util/write_data_pickle.py data/scottish_city_distances.csv data/scottish_city.pi    ckled

Test code:

    import os
    import os.path
    import pickle
    
    def file_exists(filename):
        if (os.path.isfile(filename)):
                print "OK ", filename, " exists"
        else:
                print "FAIL ", filename, " does not exist"

    def test_path_form(outputfile, numberofcities):
        result = pickle.load(open(outputfile, "r"))
        best_path_nodes = result[0]
        best_path_names = result[1]
        best_path_cost = result[2]
        if (len(best_path_nodes) == int(numberofcities)):
                print "Path length OK"
        else:
                print "Path length failure"
        if (best_path_cost > 0):
                print "Path Cost OK"
        else:
                print "Path cost failure: path is zero or negative length"
        if (len(set(best_path_nodes)) == int(numberofcities)):
                print "Uniqueness satisfied"
        else:
                print "Duplicates in path".

    def test_anttsp(datafile, numberofcities, outputfile):
        cmd = "python anttsp.py " + numberofcities + " " + datafile + " " + outputfile
        os.system(cmd)
        file_exists(outputfile)
        test_path_form(outputfile, numberofcities)

    #file_exists("output.pickled")
    #file_exists("mumbojumbo")

    test_anttsp("data/scottish_city.pickled", "5", "myoutput.pickled")

The first run of `test_ant.py` with the config file may give an error because of the formatting of `test_config.txt`. If there is a BLANK line, the test script will give an error involving `path_length = int(input_args[0])`. That may be due to ending the second set of input arguments with a newline/carriage return. To fix it, just delete the blank line at the end of the config file. 

    import numpy as np
    from antgraph import AntGraph
    from nose.tools import assert_equal

    def tests_ones_distance_etha():
        distance = [[1 for col in range(3)] for row in range(3)]
        graph = AntGraph(3, distance)
        assert_equal(graph.etha(0,1), 1)

    def test_general_distance_etha():
        distance = [[0, 5, 4], [5, 0, 2], [4, 2, 0]]
        graph = AntGraph(3, distance)
        assert_equal(0.2, graph.etha(0,1))

Other funny behaviour around numerical representation in Python:

    In [37]: round(0.3123456, 4)
    Out[37]: 0.3123
    In [38]: round(0.300000, 4)
    Out[38]: 0.3
    In [39]: round(0.3, 4)
    Out[39]: 0.3

What every computer scientist should know about floating-point arithmeticm http://dl.acm.org/citation.cfm?id=103163

---

## Light relief

* Make, http://xkcd.com/149/
* Tar, http://xkcd.com/1168/
* Automation 1, http://xkcd.com/1205/
* Automation 2, http://xkcd.com/1319/
* Editors, http://xkcd.com/378/
* Shell, http://uni.xkcd.com/
