import json
import base64

def process_manifest():
    try:
        # Input prompts
        input_filename = input("Enter the input file name (with extension): ").strip()
        search_string = input("Enter the string to search for: ").strip()
        replace_string = input("Enter the string to replace with: ").strip()
        output_filename = input("Enter the output file name (with extension): ").strip()
        
        # Read input file
        with open(input_filename, 'r') as infile:
            file_content = infile.read()
        
        # Parse JSON content
        data = json.loads(file_content)
        
        # Extract and decode the 'manifest' field
        manifest_b64 = data.get("configuration", {}).get("manifest")
        if not manifest_b64:
            print("Error: No 'manifest' field found in the input file.")
            return
        
        manifest_decoded = base64.b64decode(manifest_b64).decode('utf-8')
        
        # Replace string in the decoded manifest
        updated_manifest = manifest_decoded.replace(search_string, replace_string)
        print(f"Replaced {search_string} with {replace_string}")

        # TEST - Output a sample with the decoded string
        print(f"New manifest text is {updated_manifest}")

        # Re-encode the modified manifest
        updated_manifest_b64 = base64.b64encode(updated_manifest.encode('utf-8')).decode('utf-8')
        
        # Update the data
        data["configuration"]["manifest"] = updated_manifest_b64
        
        # Write to the output file
        with open(output_filename, 'w') as outfile:
            json.dump(data, outfile)
        
        print(f"Manifest updated and written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except json.JSONDecodeError:
        print("Error: Input file is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_manifest()
