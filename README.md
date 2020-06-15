# **PROJECT NAME**
Pacman game

---

### **Table of contents**
- [Description](#description)
- [Environment](#environment)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## **Description**
This pacman game was developped with A* algorithm to simulate the action which the pacman eat the coins using the A* searching. While doing action, pacman will update the maze if have something changes and continue eat the coins.

---

## **Environment**
- Window 10 or Ubuntu 18.04

---

## **Prerequisites**
- [Python 2.7.12 or Python(>=3.6)](https://www.python.org/downloads/);
- pygame (>=1.9.6);
- numpy (>=1.18.5);

---

## **Installing**
```
git clone https://github.com/tainp98/pacman.git
cd pacman
py -m pip install -r requirements.txt (on Window)
python/python3 -m pip install -r requirements.txt (on Ubuntu)
```

---

## **How To Use**
1. Parameters
   - '-s', '--select' : input parameters
   - if s = `a star` switch to maze for a* algorithm
   - if s = `bfs` switch to maze for bfs algorithm
   - > **select s that show same maze between a* and bfs to compare 2 algorithms
   - if s = `None` nomal mode
   - **Note : the BFS algorithm only run on origin maze**
2. Run program
   - py main.py (on Window)
   - python/python3 main.py or ./run.sh (on Ubuntu)
2. KeyBroad
   - Press any keybroad to start game
   - Then press keybroad[1,2,3,4,5,6,7,8,9,q,w,e,r,a,s] to start action add coins to maze [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] numbers of coin 
   - Press keybroad P to changes maze while program is running. Keybroad O to return origin maze
   - Press keybroad C to assign `select` = `None`
   - Press keybroad V to assign `select` = `a star`
   - Press keybroad B to assign `select` = `bfs`

---

## **Author Info**
- Students of Hanoi University of Science And Technology:
  - ``` Nguyen Phu Tai```
  - ```Nguyen Trung Kien ```
