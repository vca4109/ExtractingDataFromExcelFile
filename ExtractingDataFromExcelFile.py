import pandas as pd
import warnings
import os  # Import os module to check file existence

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Define input and output file paths
uploaded_file_name = 'ABC.xlsx'  
sheet_name = 'Deliverables'
output_file_path = 'ABC_Extracted_Data_26-03-2024.xlsx'

# Define columns to extract (zero-based index)
columns_to_extract = [1, 8, 17, 13, 22, 13, 10, 14, 18, 23, 26, 28, 25, 37, 100, 100, 10, 2, 14, 100, 10, 100, 100, 2, 14, 100, 100, 100, 8, 2, 10, 14] 

try:
    # Read Excel file
    df = pd.read_excel(uploaded_file_name, sheet_name=sheet_name)

    # Extract selected columns
    selected_columns_data = df.iloc[:, columns_to_extract]

    # Convert to DataFrame
    result_df = pd.DataFrame(selected_columns_data)

    # Save to new Excel file
    result_df.to_excel(output_file_path, index=False)

    # Check if the file was created successfully
    if os.path.exists(output_file_path):
        print("✅ Download Successful! File saved as:", output_file_path)
    else:
        print("❌ Unsuccessful: File not created.")

except FileNotFoundError:
    print(f"⚠️ Error: '{uploaded_file_name}' not found. Please check the file path.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")
