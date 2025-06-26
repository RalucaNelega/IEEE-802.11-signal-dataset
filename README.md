# 📡 IEEE 802.11 Synthetic RF Signal Dataset

This dataset was generated as part of a research effort aimed at improving RF signal classification using deep learning, while addressing challenges related to data scarcity and environmental variability. Large datasets are crucial to capture the diverse characteristics of real-world wireless scenarios. However, practical constraints on storage and processing require that the training and testing sets remain within reasonable bounds. To address this, a carefully selected set of parameters was used to generate a finite yet representative dataset.

In total, **134,400 synthetic IEEE 802.11 signals** were generated as complex I/Q samples. These samples replicate real transmission behaviors under different modulation, coding, and channel conditions. Each signal recording contains **512 I/Q samples**, randomly extracted from the **data field of IEEE 802.11 frames**. This dataset is made publicly available for use in RF signal processing and deep learning research.

---

## 🧾 Dataset Overview

This dataset is designed to support the training and evaluation of machine learning models for tasks such as:

-  **Classification of IEEE 802.11 standard versions**  
-  **Prediction of Modulation and Coding Schemes (MCS)**  
-  **Assessment of wireless propagation environments**

It is suitable for research in spectrum monitoring, RF fingerprinting, modulation recognition, and adaptive wireless systems.

---

## 📁 Files Included

- `dataset.npy`  
  NumPy array file containing the full dataset. Each row represents a wireless transmission.

- `columns.txt`  
  Text file listing the column names for building a Pandas DataFrame from the array.

---

## 📊 Data Structure

Each row contains a set of features describing one generated signal. The columns are:

| Column              | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| `IQSamples`         | Array of complex-valued I/Q samples (512 samples per row)           |
| `DelayProfile`      | Channel model used (e.g., Ideal, Model-A, Model-B, etc.)            |
| `MCS`               | Modulation and Coding Scheme index                                  |
| `SNR`               | Signal-to-Noise Ratio                                               |
| `Modulation`        | Modulation format (OFDM or DSSS)                                    |
| `Speed`             | Travel speed (1.2km/h and 120km/h)                                  |
| `IEEE Standard`     | Protocol version (e.g., 802.11b, 802.11a/g, 802.11n)                |
| `IEEE Transmission` | Transmission mode (DSSS, OFDM non-HT, OFDM HT 20MHz, OFDM HT 40MHz) |

---

## 🔎 Sample Entry Format

Each row in the dataset corresponds to a single signal recording. Below is a representative example:

```
IQSamples            [(0.4796677225675269-0.11023387281558178j), (0.51...]
DelayProfile                                                      Ideal
MCS                                                                   0
SNR                                                               11.81
Modulation                                                         OFDM
Speed                                                               120
IEEE Standard                                                  802.11n
IEEE Transmission                                         OFDM HT 40MHz
```

---

## 🧪 Usage Example

```python
import numpy as np
import pandas as pd

# Load dataset
dataset = np.load('dataset.npy', allow_pickle=True)

# Load column headers
with open('columns.txt', 'r') as f:
    column_names = [line.strip() for line in f]

# Create DataFrame
df = pd.DataFrame(dataset, columns=column_names)
print(df.head())
```

---

## 📝 Citation

If you use this dataset in your research or publication, please cite the associated work or acknowledge the authors accordingly.

📌 **Note**: A link to the publication will be provided here once it becomes available.