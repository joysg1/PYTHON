
import matplotlib.pyplot as plt

def get_country_temps(data_source="sample"):  # Optional: Specify data source
  if data_source == "sample":
    countries = [
        "Burkina Faso", "Mali", "Niger", "Chad", "Algeria", "Ethiopia",
        "Sudan", "Eritrea", "Djibouti", "Somalia", "Kenya", "Uganda",
        # ... (more countries)
    ]
    # Sample average temperatures (replace with actual data)
    average_temps = [27.5, 28.2, 29.1, 28.8, 26.4, 23.4, 29.2, 26.1, 31.2, 27.8, 25.4, 24.8,
                     # ... (more temperatures)
    ]
  else:
    # Implement code to fetch data from your chosen source
    # ...
    pass
  return countries, average_temps

try:
  # Get country and temperature data
  countries, average_temps = get_country_temps()

  # Filter countries and temperatures between 25 and 30°C
  filtered_countries = [country for country, temp in zip(countries, average_temps) if 25 <= temp < 30]
  filtered_temps = [temp for temp in average_temps if 25 <= temp < 30]

  # Check if there are any countries within the temperature range
  if not filtered_countries:
    print("No countries found with average temperatures between 25°C and 30°C.")
    exit()

  # Create the plot
  plt.figure(figsize=(10, 6))  # Adjust figure size for potentially fewer countries

  # Create bars and add labels with loop
  bars = plt.bar(filtered_countries, filtered_temps, color='purple')  # Purple bars
  for bar, temp in zip(bars, filtered_temps):
    plt.text(bar.get_x() + bar.get_width() / 2, temp + 0.2, f"{temp:.1f}°C", ha='center')  # Add labels

  plt.xlabel("Countries")
  plt.ylabel("Average Temperature (°C)")
  plt.title("Countries with Average Temp Between 25°C and 30°C (Sample Data)")

  # Customize the plot (optional)
  plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
  plt.grid(axis='y', linestyle='--', alpha=0.6)

  # Display the plot
  plt.tight_layout()
  plt.subplots_adjust(bottom=0.3)  # Adjust space for x-axis labels

  plt.show()
except Exception as e:
  print(f"An error occurred: {e}")
