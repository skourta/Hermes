# Hermes

**Hermes** is a hybrid desktop application built using Electron and Vue to solve the Symmetric Traveling Salesman Problem(TSP), it provides different methods written in Python to solve TSP varying from exact ones to hybrid meta-heuristics.

![Preview](https://i.imgur.com/WcoqAfV.png)

## 1.1. Requirements
This project is based on Electron and VueJs

## 1.2. Build

1. First thing you need to do is clone this repository
```
git clone https://github.com/skourta/Hermes
```
2. Positing yourself in the root of the project:
```
cd   Hermes
```
3. Install dependencies using your favorite package manager 
```
yarn
```
4. (optional) you can build your executable by running
```
yarn electron:build
```
## 1.3. Usage
You can run build the project then run the executable or serve the project in development mode:
```
yarn electron:serve
```
## Credits
| Algorithm        | Provided By           |
| ---------------- | --------------------- |
| 2OPT             | BENABED Youcef        |
| AC               | KOURTA Smail          |
| ACO[2OPT]        | TAHMI Omar            |
| ACO+2OPT         | TAHMI Omar            |
| AG               | IFERROUDJENE Mouloud  |
| AG[2OPT]         | IFERROUDJENE Mouloud  |
| AG+2OPT          | IFERROUDJENE Mouloud  |
| Branch and Bound | KOURTA Smail          |
| Brute Force      | IFERROUDJENE Mouloud  |
| Greedy Algorithm | BENDJABALLAH Oussama  |
| Nearest Neighbor | TAHMI Omar            |
| Tabu Search      | BENBELGACEM Rahma Aya |
| Or-Tools Usage   | KOURTA Smail          |
| TSPlib Parser    | KOURTA Smail          |

The UI was developed by Smail KOURTA using Electron, VueJS and lowDB.
