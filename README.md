# 🎵 Tiptoi Data Sonification for the Visually Challenged

This project explores **data sonification** — representing data through sound — using the **Ravensburger Tiptoi** pen system.  
It aims to make data exploration **accessible to visually challenged individuals** by enabling them to *hear* data patterns through interactive OID codes.

The project is built using **tttool v1.11**, located in:

```bash
tiptoi-projects/tttool/tttool-1.11
```

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

```bash
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

```

</details>

---

## 🧠 Concept

Each **part** is assigned an audio file, providing specific attributes like:
- **Context** → Providing background information similar to a journalism report.
- **Play** → Pause/Play the audio file.
- **Route** → In later visualizations, the audio file guides users on where to place the pen for the best experience.


Users interact with **OID codes** printed next to data visuals. When touched, the **Tiptoi pen** plays the corresponding audio file, transforming visual information into an **auditory experience** that supports inclusive, tactile learning.

---

## 🧪 Sample Templates

The `Sample templates` directory includes three concepts for integrating OID codes into different data visualizations:

| Folder | Concept | Description |
|--------|---------|-------------|
| **Tic-Tac-Tiptoi** | Tic-tac-toe|  A tic-tac-toe game to play|
| **Iris-bar-chart** | Bar charts | Bars linked to OIDs that trigger explanations representing their values. |
| **Electoral-College** | Spatial/Map data | OIDs embedded in regions or areas to represent spatial data. |

Each folder includes:
- The **OID codes** positioned for alignment and printing  
- Notes on data mapping and audio behavior  

> **Design files (`.xcf`) are located in `tiptoi-projects\GIMP`**.

> **The folders above can be found in `\tiptoi-projects\tttool\tttool-1.11\Sample_templates`**

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
Add your numeric dataset (e.g., iris-dataset.) to the `data/` folder.

### 2. Generate OID Codes
Use `tttool` to generate 20x70 mm OID codes or any size that suits your purposes:

```bash
./tttool oid-codes --code-dim 20x70mm src/project.yaml
```

### 3. Design Templates

Open a layout in **GIMP** (`tiptoi-projects/GIMP/`), align the OID codes next to visual elements, and export the final printable layout.

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