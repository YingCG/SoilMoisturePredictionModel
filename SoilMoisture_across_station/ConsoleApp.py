import pandas as pd

# Create a DataFrame with the provided data, including predicted soil temp and moisture
data = {
    "Location": [
        "Kaipara Heads @ Wallers", "Hoteo at Oldfields", "Tamahunga @ Quintals Rd", 
        "Tomarata at Briens Farm", "Ararimu @ Zanders", "Mt Albert Grammar Rainfall", 
        "Mangemangeroa @ Craigs", "Awhitu @ Brook Road", "Waitangi @ Diver Road", 
        "Whangamaire @ Culvert"
    ],
    "Soil Order": [
        "Brown", "Ultic", "Ultic", "Ultic", "Allophanic", "Ultic", 
        "Ultic", "Granular", "Granular", "Allophanic"
    ],
    "NZ Soil Classification": [
        "Red Hill sandy loam", "Typic Yellow Ultic", "Typic Yellow Ultic", 
        "Perch Gley or Densipan Ultic", "Typic Orthic Allophanic", "Mottled Yellow Ultic", 
        "Typic Yellow Ultic", "Typic Orthic Granular", "Typic Orthic Granular", 
        "Typic Orthic Allophanic"
    ],
    "Mean Annual Rainfall (mm)": [
        1054, 1347, 1561, 1172, 1352, 1242, 
        1198, 1372, 1280, 1329
    ],
    "Predicted Soil Moisture (%)": [
        35, 40, 45, 30, 33, 38, 
        42, 37, 39, 36
    ],
    "Predicted Soil Temperature (°C)": [
        18, 20, 21, 19, 22, 17, 
        16, 19, 20, 18
    ],
    "Pastoral Land Use": [
        "Drystock", "Lifestyle block", "Drystock", "Dairy", 
        "Drystock", "Mixed dairy and drystock", "Lifestyle block", 
        "Regional Park", "Dairy", "Lifestyle block"
    ],
    "Ecological District": [
        "Kaipara", "Rodney", "Rodney", "Rodney", 
        "Waitakere", "Tamaki", "Tamaki", "Awhitu", 
        "Manukau", "Manukau"
    ],
    # Other soil condition data as in previous example
}

df = pd.DataFrame(data)

# Function to suggest plants based on location and conditions
def suggest_plants(location):
    # Filter the DataFrame for the specified location
    location_data = df[df['Location'].str.contains(location, case=False)]
    
    if location_data.empty:
        print("No data found for the specified location.")
        return None

    print("\nConditions for the selected location:")
    for index, row in location_data.iterrows():
        print(f"Location: {row['Location']}")
        print(f"Soil Order: {row['Soil Order']}")
        print(f"Mean Annual Rainfall: {row['Mean Annual Rainfall (mm)']} mm")
        print(f"Predicted Soil Moisture: {row['Predicted Soil Moisture (%)']}%")
        print(f"Predicted Soil Temperature: {row['Predicted Soil Temperature (°C)']}°C")
        print("Suggested plants based on conditions:")
        
        # Suggestions based on predicted soil moisture and temperature
        moisture = row['Predicted Soil Moisture (%)']
        temperature = row['Predicted Soil Temperature (°C)']

        if moisture > 40 and temperature > 20:
            print("- Ferns, Canna lilies, and other moisture-loving plants.")
        elif moisture < 40 and temperature < 20:
            print("- Drought-resistant plants like succulents and lavender.")
        elif moisture > 40 and temperature < 20:
            print("- Shade-loving plants such as hostas or ferns.")
        elif moisture < 40 and temperature > 20:
            print("- Plants like rosemary or other herbs that tolerate drought.")
        
        print()  # Print a newline for better readability

def main():
    print("Welcome to the Plant Condition Suggestion App!")
    
    while True:
        # User input for plant name and location
        plant = input("Enter the plant you have (or type 'exit' to quit): ")
        
        if plant.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
            
        location = input("Enter your location: ")
        
        # Provide conditions and suggestions
        suggest_plants(location)

# Run the application
if __name__ == "__main__":
    main()
