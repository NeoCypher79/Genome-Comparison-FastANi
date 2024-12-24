# Genome Comparison using FastANI

This repository provides a Python script for performing genome comparisons using the FastANI tool. The script takes genome files in `.fasta` or `.fna` formats from a directory and generates a pairwise comparison output in a tabular format, with enhanced readability using the pandas library.

---

## Prerequisites

To run the script, you need the following tools and libraries installed:

1. **FastANI**
   - Download FastANI from its [official GitHub repository](https://github.com/ParBLiSS/FastANI).
   - Follow the installation instructions provided in the FastANI repository.

2. **Python 3.x**
   - Install Python from [python.org](https://www.python.org/).

3. **Required Python Libraries**
   - `pandas`: Used for organizing and exporting results in a readable format.
   - Install it using:
     ```bash
     pip install pandas
     ```

---

## Setup

1. Clone this repository to your local system:
   ```bash
   git clone https://github.com/NeoCypher79/Genome-Comparison-FastANI.git
   ```
2. Navigate to the directory:
   ```bash
   cd Genome-Comparison-FastANI
   ```
3. Make sure the FastANI executable is accessible via the command line. You can verify this by running:
   ```bash
   fastANI --version
   ```

---

## Usage

1. **Prepare Input Files**
   - Place all genome files (`.fasta` or `.fna`) in a directory.

2. **Run the Script**
   - Execute the script by specifying the input directory and output file:
     ```bash
     python3 fastani_batch.py <input_directory> <output_file>
     ```
   - Example:
     ```bash
     python3 fastani_batch.py total_genomes fastani_results.tsv
     ```

3. **Output**
   - The script generates an output file in TSV (tab-separated values) format containing:
     - Query genome
     - Reference genome
     - ANI (%)
     - Fragments Mapped
     - Total Fragments
   - Additionally, the pandas library organizes the output for better readability and exports it as `fastani_results_pandas.tsv`.

---

## Example Output

An example output looks like this:

| Query           | Reference       | ANI (%) | Fragments Mapped | Total Fragments |
|-----------------|-----------------|---------|------------------|-----------------|
| genome1.fasta   | genome2.fasta   | 98.76   | 100              | 102             |
| genome1.fasta   | genome3.fasta   | 95.43   | 85               | 92              |

---

## Notes

- Ensure that FastANI is properly installed and accessible via the command line before running the script.
- Large genome datasets may take significant time to process.
- Redundant comparisons (e.g., comparing genome1 with genome2 and genome2 with genome1) are automatically avoided in the script.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

