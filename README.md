# kmapper_law_analysis
**Korean law data analysis using Topological Data Analysis and Mapper Algorithm**

---

## Installation & Execution

### Prerequistes
- Python (>= 3.6)
- NumPy
- Scikit-learn
- openpyxl

### 1. Clone

```shell
$ git clone https://github.com/zeebraa00/kmapper_law_analysis.git
```

### 2. Install Packages

```bash
$ pip install numpy
$ pip install -U scikit-learn
$ pip install openpyxl
```

### 3. Make custom distance matrix of data

```shell
$ python make_metric.py
```
We have focused on the reference relation of law.
1. Initiate the distance matrix. (Set distances between all laws to 1.)
2. Shorten distance between laws used in same precedent while scanning Korean precedents.
3. The completed distance matrix is saved as a binary file. (law_data/custom_metric.npy)

### 4. Cluster Korean-law-data using kepler-mapper
```shell
$ python main.py
```

Copyright ⓒ 2021 성균관대학교 수학과 김성훈, 정재헌 All Rights Reserved
