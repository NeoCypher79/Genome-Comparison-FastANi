import os
import subprocess
import pandas as pd

def run_fastani(directory, output_file):
    files = [f for f in os.listdir(directory) if f.endswith(('.fasta', '.fna'))]
    total_files = len(files)

    # Create an empty list to store the results
    results = []

    # Use nested loops to compare each file only once
    for i in range(total_files):
        query = os.path.join(directory, files[i])
        
        # Only compare the current query file with files after it in the list
        for j in range(i + 1, total_files):  
            reference = os.path.join(directory, files[j])
            
            # Run FastANI and capture the output
            result = subprocess.run(
                ['fastANI', '--query', query, '--ref', reference, '-o', 'temp_output.txt'],
                capture_output=True, text=True
            )

            # Parse the FastANI output
            with open('temp_output.txt') as temp:
                for line in temp:
                    # Split the FastANI output into components
                    query_file, reference_file, ani, fragments_mapped, total_fragments = line.strip().split('\t')
                    # Append the parsed data to the results list
                    results.append({
                        "Query": query_file,
                        "Reference": reference_file,
                        "ANI (%)": float(ani),
                        "Fragments Mapped": int(fragments_mapped),
                        "Total Fragments": int(total_fragments)
                    })
            
            # Optional: Print progress
            print(f"Compared: {files[i]} vs {files[j]}")

    # Convert results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Save the DataFrame to a TSV file
    df.to_csv(output_file, sep='\t', index=False)

    print(f"\nResults saved to {output_file}")

# Example usage:
run_fastani('total genome', 'fastani_results.tsv')
