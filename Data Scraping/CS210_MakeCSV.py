import json
import csv

def fetch_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return None

# Example usage:
file_path = "/Users/ecemcakalli/Desktop/burcu_deneme/JSONS/M13.json"
json_data = fetch_json_data(file_path)

# Assuming `json_data` contains your JSON data
matches = json_data.get('data', {}).get('matches', [])

# Specify the CSV file name
csv_file_name = 'JSON13.csv'

# Open CSV file for writing
with open(csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write header row with each header in a separate column
    csv_writer.writerow(['Date', 'Playtime', 'Rank', 'Season', 'Result', 'Map', 'Agent', 'Rounds Won', 'Rounds Lost', 'Kills', 'Deaths', 'Assists', 'Headshots', 'Headshot Percentage', 'Damage', 'Received Damage', 'Kill Death Ratio'])

    # Write data rows
    for match in matches:
        season_name = match.get('metadata', {}).get('seasonName', '')
        map_name = match.get('metadata', {}).get('mapName', '')
        result = match.get('metadata', {}).get('result', '')
        date = match.get('metadata', {}).get('timestamp', '')

        agent_name = match['segments'][0]['metadata']['agentName']
        play_time = match['segments'][0]['stats']['playtime']['displayValue']  
        rounds_won = match['segments'][0]['stats']['roundsWon']['value']  
        rounds_lost = match['segments'][0]['stats']['roundsLost']['value']        
        kills_value = match['segments'][0]['stats']['kills']['value']        
        deaths_value = match['segments'][0]['stats']['deaths']['value']        
        assists_value = match['segments'][0]['stats']['assists']['value']        
        damage_value = match['segments'][0]['stats']['damage']['value']   
        damage_received_value = match['segments'][0]['stats']['damageReceived']['value']  
        headshots_value = match['segments'][0]['stats']['headshots']['value']  
        m_rank = match['segments'][0]['stats']['rank']['metadata']['tierName']
        headshot_percentage = match['segments'][0]['stats']['headshotsPercentage']['value']  
        kd_ratio = match['segments'][0]['stats']['kdRatio']['value']  

        # Write a row for each match with each data in a separate column
        csv_writer.writerow([date, play_time, m_rank, season_name, result, map_name, agent_name, rounds_won, rounds_lost, kills_value, deaths_value, assists_value, headshots_value, headshot_percentage, damage_value, damage_received_value, kd_ratio])

print(f'CSV file "{csv_file_name}" has been created successfully.')
