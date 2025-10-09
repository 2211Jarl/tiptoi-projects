# 🎵 Tiptoi Data Sonification for the Visually Challenged

This project explores **data sonification** — representing data through sound — using the **Ravensburger Tiptoi** pen system.  
It aims to make data exploration **accessible to visually challenged individuals** by enabling them to *hear* data patterns through interactive OID codes.

The project is built using **tttool v1.11**, located in:

tiptoi-projects/tttool/tttool-1.11


---

## ⚠️ Directory Note

> All **YAML configuration files** and **Python scripts** must be placed **in the same directory as `tttool`** (inside `tttool-1.11/`).  
> `tttool` depends on relative paths, so commands like `assemble` or `oid-codes` will fail if the YAML files are located elsewhere.

---

## 🎬 Demo

[Watch a demo on YouTube](https://youtu.be/SiKodwf9AK4)

---

## 🗂️ Project Structure

<details>
<summary>Click to expand folder structure</summary>

Tiptoi-experiments/
└── tiptoi-projects/
    ├── tttool/
    │   ├── tttool-1.11/
    │   │   ├── data/                   # CSV datasets (e.g., storm, pricing, etc.)
    │   │   ├── elect-media/            # Electronic media: sound files, effects, etc.
    │   │   ├── Sample templates/       # Experimental layouts for OID integration
    │   │   │   ├── Idea_1/             # Concept 1: Bar Graph with Sonified OIDs
    │   │   │   ├── Idea_2/             # Concept 2: Spatial or Map Layout
    │   │   │   └── Idea_3/             # Concept 3: Interactive Data Cards
    │   │   ├── src/                    # YAML configurations + Python scripts
    │   │   ├── output/                 # Compiled .gme files for Tiptoi pen
    │   │   └── tttool.exe              # tttool binary (v1.11)
    └── GIMP/                            # GIMP .xcf files for designing layouts


</details>

---

## 🧠 Concept

Each **data point** is assigned a sound or tone that represents specific attributes like:
- **Pitch** → Magnitude  
- **Volume** → Intensity  
- **Duration** → Frequency or time dimension  

Users interact with **OID codes** printed next to data visuals. When touched, the **Tiptoi pen** plays a corresponding sound, transforming visual information into an **auditory experience** that supports inclusive, tactile learning.

---

## 🧪 Sample Templates

The `Sample templates` directory includes three concepts for integrating OID codes into different data visualizations:

| Folder | Concept | Description |
|--------|---------|-------------|
| **Idea_1** | Bar Chart Sonification | Bars linked to OIDs that trigger tones representing their values. |
| **Idea_2** | Spatial Layout / Map | OIDs embedded in regions or areas to represent spatial data. |
| **Idea_3** | Data Cards | Individual cards or panels for comparing categories through sound. |

Each folder includes:
- The **OID codes** positioned for alignment and printing  
- Notes on data mapping and audio behavior  

> **Design files (`.xcf`) are located in `Tiptoi-experiments/tiptoi-projects/GIMP/`**.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Tiptoi SDK / tttool v1.11** | Generate `.gme` files and OID codes |
| **Python** | Automate data-to-sound mapping and file generation |
| **GIMP** | Align visuals and integrate OID codes (.xcf files in `GIMP/`) |

---

## ⚙️ How to Use

### 1. Prepare Your Dataset
Add your numeric dataset (e.g., weather, finance, etc.) to the `data/` folder.

### 2. Generate OID Codes
Use `tttool` to generate 20x70 mm OID codes:

```bash
./tttool oid-codes --code-dim 20x70mm src/project.yaml
```

### 3. Design Templates

Open a layout in **GIMP** (`Tiptoi-experiments/tiptoi-projects/GIMP/`), align the OID codes next to visual elements, and export the final printable layout.

---

### 4. Compile the `.gme` File

Assemble your Tiptoi project file:

```bash
./tttool assemble src/project.yaml
```

## 🙌 Acknowledgments

- **Ravensburger Tiptoi** — for the interactive learning platform
- **tttool developers** — for reverse-engineering the Tiptoi format
- **Aarhus University** — for supporting accessibility and inclusive technology research