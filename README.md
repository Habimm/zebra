# Solving the Zebra Puzzle using Python and an online SAT solver

We solve the Zebra Puzzle using Python and a online SAT solver.

Run
```sh
./INSTALL
. RUN
```

This will create a folder *milestones/* with a few files in it.

This is the Zebra Puzzle solution:

![Zebra Solution](https://raw.githubusercontent.com/Habimm/zebra/master/zebra_solution.png)

This repo empowers you to 1-click-create a `.csv` file with this data in it.

For that, go to
```
https://simewu.com/SAT-solver/
```
and enter your constraints and solve the puzzle. Then you will get a solution that might be formatted as:
```
x1 = 0
x2 = 0
x3 = 1
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 1
x11 = 0
x12 = 0
```

Paste the solution into a new file at
```sh
milestones/proposition_assignment.csv
```


Then, run
```
. RUN
```
again. You'll get a new `.csv` file called
```
milestones/decoded_proposition_assignment.csv
```
with the content
```
,1,2,3,4,5
Color,Yellow,Blue,Red,Ivory,Green
Nationality,Norwegian,Ukrainian,Englishman,Spaniard,Japanese
Pet,Fox,Horse,Snails,Dog,Zebra
Drink,Water,Tea,Milk,OrangeJuice,Coffee
Cigarettes,Kools,Chesterfields,OldGold,LuckyStrike,Parliaments
```

Have fun!
