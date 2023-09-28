import streamlit as st
import requests

# Function to fetch rosters data
def fetch_rosters_data(league_id):
    url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f'Failed to retrieve data: {response.text}')
        return None

def main():
    st.title("Fantasy Football Trade Suggester")

    league_id = st.text_input("Enter your Sleeper League ID:")
    if league_id:
        rosters_data = fetch_rosters_data(league_id)
        if rosters_data:
            st.write("Rosters data imported successfully!")
            user_id = st.text_input("Enter your Sleeper User ID to view your team:")
            if user_id:
                user_roster = next((roster for roster in rosters_data if roster['owner_id'] == user_id), None)
                if user_roster:
                    st.write(f"Team Name: {user_roster['metadata']['team_name']}")
                    st.write(f"Players: {user_roster['players']}")
                else:
                    st.write("No roster found for the provided User ID.")

if __name__ == "__main__":
    main()
