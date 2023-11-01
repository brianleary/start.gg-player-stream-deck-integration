import requests
import json

url = 'https://api.start.gg/gql/alpha'

# GraphQL query (update tournament link)
payload = """
query StreamQueueOnTournament {
  tournament(slug: "tournament/api-test-tournament-4") {
    id
    streamQueue {
      stream {
        streamSource
        streamName
      }
      sets {
        slots {
          entrant {
            name
          }
        }
      }
    }
  }
}
"""
headers = {'Authorization': 'Bearer API_TOKEN', 'content-type': 'application/json'}

# Make request
r = requests.post(url=url, json={"query": payload}, headers=headers)
result = r.json()

# Prints for checking results
#print("response status code: ", r.status_code)
#print(json.dumps(result, indent=2))

# Get names from JSON result
names = result["data"]["tournament"]["streamQueue"][0]["sets"][0]["slots"]
name1 = names[0]["entrant"]["name"]
name2 = names[1]["entrant"]["name"]

# Put names in files
f = open("C:\\Users\\User\\OneDrive\\Documents\\Streaming\\Smash Controls\\LeftPlayerName.txt", "w")
f.write(name1)
f.close()

f = open("C:\\Users\\User\\OneDrive\\Documents\\Streaming\\Smash Controls\\RightPlayerName.txt", "w")
f.write(name2)
f.close()