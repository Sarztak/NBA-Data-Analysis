import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define past to present name changes
# Each tuple is (old_team, new_team)
changes = [
    ("Philadelphia Ers", "Philadelphia 76ers"),
    ("Charlotte Bobcats", "Charlotte Hornets"),
    ("New Orleans Hornets", "New Orleans Pelicans"),
    ("New Jersey Nets", "Brooklyn Nets"),
    ("Seattle Supersonics", "Oklahoma City Thunder"),
    ("New Orleans/Oklahoma City Hornets", "New Orleans Pelicans"),
    ("Vancouver Grizzlies", "Memphis Grizzlies"),
    ("Washington Bullets", "Washington Wizards"),
    ("Kansas City Kings", "Sacramento Kings"),
    ("San Diego Clippers", "Los Angeles Clippers"),
    ("New Orleans Jazz", "Utah Jazz"),
    ("Buffalo Braves", "San Diego Clippers"),
    ("New York Nets", "Brooklyn Nets"),
    ("San Diego Sails", "San Diego Conquistadors"),
    ("Spirits Of St Louis", "St. Louis Hawks"),
    ("Utah Stars", "Utah Jazz"),
    ("Virginia Squires", "Washington Bullets"),
    ("Kansas City-Omaha Kings", "Sacramento Kings"),
    ("Memphis Sounds", "Memphis Grizzlies"),
    ("San Diego Conquistadors", "San Diego Rockets"),
    ("Capital Bullets", "Washington Bullets"),
    ("Carolina Cougars", "Charlotte Hornets"),
    ("Denver Rockets", "Denver Nuggets"),
    ("Memphis Tams", "Memphis Grizzlies"),
    ("Baltimore Bullets", "Washington Wizards"),
    ("Dallas Chaparrals", "San Antonio Spurs"),
    ("Cincinnati Royals", "Sacramento Kings"),
    ("The Floridians", "Miami Floridians"),
    ("Memphis Pros", "Memphis Grizzlies"),
    ("Pittsburgh Condors", "Pittsburgh Pipers"),
    ("San Diego Rockets", "Houston Rockets"),
    ("San Francisco Warriors", "Golden State Warriors"),
    ("Texas Chaparrals", "Dallas Mavericks"),
    ("Los Angeles Stars", "Los Angeles Lakers"),
    ("Miami Floridians", "Miami Heat"),
    ("New Orleans Buccaneers", "New Orleans Pelicans"),
    ("Pittsburgh Pipers", "Washington Bullets"),
    ("Washington Capitols", "Washington Wizards"),
    ("Houston Mavericks", "Houston Rockets"),
    ("Minnesota Pipers", "Minnesota Timberwolves"),
    ("Oakland Oaks", "Golden State Warriors"),
    ("Anaheim Amigos", "Los Angeles Lakers"),
    ("Minnesota Muskies", "Minnesota Timberwolves"),
    ("New Jersey Americans", "New Jersey Nets"),
    ("St Louis Hawks", "Atlanta Hawks"),
    ("Chicago Zephyrs", "Washington Wizards"),
    ("Syracuse Nationals", "Philadelphia 76ers"),
    ("Chicago Packers", "Milwaukee Bucks"),
    ("Philadelphia Warriors", "Golden State Warriors"),
    ("Minneapolis Lakers", "Los Angeles Lakers"),
    ("Fort Wayne Pistons", "Detroit Pistons"),
    ("Rochester Royals", "Sacramento Kings"),
    ("Milwaukee Hawks", "Atlanta Hawks"),
    ("Indianapolis Olympians", "Indiana Pacers"),
    ("Tricities Blackhawks", "Atlanta Hawks"),
    ("Anderson Packers", "Chicago Stags"),
    ("Chicago Stags", "Chicago Bulls"),
    ("Sheboygan Red Skins", "Washington Bullets"),
    ("St Louis Bombers", "St. Louis Hawks"),
    ("Waterloo Hawks", "Atlanta Hawks"),
    ("Indianapolis Jets", "Indiana Pacers"),
    ("Providence Steamrollers", "Boston Celtics"),
    ("Cleveland Rebels", "Cleveland Cavaliers"),
    ("Detroit Falcons", "Detroit Pistons"),
    ("Pittsburgh Ironmen", "Washington Wizards"),
    ("Toronto Huskies", "Toronto Raptors")
]

# Add edges to the graph
for old, new in changes:
    G.add_edge(old, new)

# Plotting the graph
plt.figure(figsize=(15, 20))
pos = nx.spring_layout(G, seed=42)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("NBA Team Name Changes from Past to Present", fontsize=16)
plt.show()