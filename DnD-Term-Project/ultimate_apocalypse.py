# CHICAGO_NIGHTMARE_CAMPAIGN.py - COMPLETE VERSION
import folium
from branca.element import Element
import pandas as pd
from folium.plugins import TimestampedGeoJson
import random
from datetime import datetime, timedelta

# ====================
# 1. D&D GAME SETUP
# ====================
m = folium.Map(location=[41.8781, -87.6298],
               zoom_start=13,
               tiles="CartoDB dark_matter",
               control_scale=True)

# ====================
# 2. D&D GAME ENGINE
# ====================
dnd_js = """
<script>
// D&D Character Sheet
const character = {
    stats: {
        str: 10,
        dex: 14,
        con: 12,
        int: 8,
        wis: 13,
        cha: 10
    },
    skills: {
        athletics: 2,
        acrobatics: 4,
        medicine: -1,
        survival: 3,
        intimidation: 0,
        perception: 3,
        stealth: 4,
        persuasion: 0
    },
    inventory: []
};

// Dice roller
function roll(dice) {
    return Math.floor(Math.random() * dice) + 1;
}

function d20() {
    return roll(20);
}

function skillCheck(skill, dc) {
    const roll = d20() + (character.skills[skill] || 0);
    const success = roll >= dc;
    return {roll, success, message: `${success ? 'Success' : 'Failure'} (${roll} vs DC ${dc})`};
}

// Game state
let supplies = 100;
let health = 100;
let daysSurvived = 0;
let completedQuests = 0;

// Update UI
function updateStats() {
    document.getElementById('supplies').innerText = supplies;
    document.getElementById('health').innerText = health;
    document.getElementById('days').innerText = daysSurvived;
    document.getElementById('quests').innerText = completedQuests;
}

// Combined D&D and Survival Mechanics
function scavenge() {
    const check = skillCheck('survival', 12);
    const found = check.success ? roll(10) + 5 : roll(3);
    supplies += found;
    updateStats();
    return `${check.message}\\nFound ${found} supplies!`;
}

function fightZombies(count) {
    let results = [];
    let damageTaken = 0;
    
    for(let i = 0; i < count; i++) {
        const attackRoll = roll(20) + 3; // Zombie attack bonus
        if(attackRoll > 10 + character.stats.dex) { // Simple AC calculation
            const damage = roll(6);
            health -= damage;
            damageTaken += damage;
            results.push(`Zombie #${i+1} hits for ${damage}!`);
        } else {
            results.push(`Zombie #${i+1} misses!`);
        }
    }
    
    updateStats();
    if(health <= 0) {
        return results.join('\\n') + `\\nTotal damage: ${damageTaken}\\nGAME OVER!`;
    }
    return results.join('\\n') + `\\nTotal damage: ${damageTaken}`;
}

function completeQuest(reward, danger) {
    const result = fightZombies(danger);
    if(health > 0) {
        completedQuests++;
        supplies += reward;
        updateStats();
        return `${result}\\nQUEST COMPLETE! +${reward} supplies`;
    }
    return result;
}

// Day cycle
setInterval(() => {
    daysSurvived++;
    supplies = Math.max(0, supplies - 10);
    if(supplies <= 0) health -= 5;
    updateStats();
    
    // Random encounters
    if(roll(20) >= 18) {
        const zombies = roll(4);
        alert(`AMBUSH! ${zombies} zombies attack!\\n` + fightZombies(zombies));
    }
}, 30000); // 30 sec = 1 day

// Save system
function saveGame() {
    localStorage.setItem('apocalypseSave', 
        JSON.stringify({
            supplies: supplies,
            health: health,
            days: daysSurvived,
            quests: completedQuests,
            character: character
        }));
    return "Game saved!";
}

function loadGame() {
    const saved = JSON.parse(localStorage.getItem('apocalypseSave'));
    if(saved) {
        supplies = saved.supplies;
        health = saved.health;
        daysSurvived = saved.days;
        completedQuests = saved.quests;
        if(saved.character) Object.assign(character, saved.character);
        updateStats();
        return "Loaded saved game!";
    }
    return "No save found";
}

// Initialize
window.onload = function() {
    loadGame();
    updateStats();
};
</script>
"""

dnd_ui = """
<div style="position: fixed; 
            top: 10px; 
            right: 10px; 
            z-index: 1000;
            background: rgba(0,0,0,0.8);
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-family: 'Times New Roman', serif;">
    <h3 style="margin:0 0 5px 0; border-bottom:1px solid #666;">ADVENTURER'S LOG</h3>
    <p>❤️ HP: <span id="health">100</span>/100</p>
    <p>🎒 Supplies: <span id="supplies">100</span></p>
    <p>📅 Days: <span id="days">0</span></p>
    <p>⚔️ Quests: <span id="quests">0</span></p>
    <button onclick="alert('D20 Roll: ' + d20())" 
            style="background: #8B0000; color: white; border: none; padding: 3px 8px; margin:2px;">
        Roll D20
    </button>
    <button onclick="alert(saveGame())" 
            style="background: #444; color: white; border: none; padding: 3px 8px; margin:2px;">
        Save Game
    </button>
    <button onclick="alert('STR:' + character.stats.str + ' DEX:' + character.stats.dex)" 
            style="background: #333; color: white; border: none; padding: 3px 8px; margin:2px;">
        Stats
    </button>
</div>
"""

m.get_root().html.add_child(Element(dnd_ui))
m.get_root().html.add_child(Element(dnd_js))

# ====================
# 3. PULSING ZOMBIE ZONES
# ====================
pulse_css = """
<style>
    .pulse-area {
        animation: pulse 2s infinite;
        transform-origin: center;
        cursor: pointer;
    }
    @keyframes pulse {
        0% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.03); }
        100% { opacity: 0.8; transform: scale(1); }
    }
    .dnd-popup {
        font-family: 'Times New Roman', serif;
        background: #1e1e1e;
        color: #f8f8f8;
        border: 2px solid #8B0000;
        padding: 10px;
        border-radius: 5px;
    }
    .dnd-popup h3 {
        color: #8B0000;
        margin-top: 0;
        border-bottom: 1px solid #444;
        padding-bottom: 5px;
    }
    .dnd-popup button {
        background: #8B0000;
        color: white;
        border: none;
        padding: 5px 10px;
        margin: 5px 2px;
        border-radius: 3px;
        cursor: pointer;
    }
</style>
"""
m.get_root().html.add_child(Element(pulse_css))


# ====================
# 4. STORY CAMPAIGN (Timed Events)
# ====================
def generate_story_features():
    outbreak_start = datetime.now() - timedelta(days=14)
    features = []

    # Week 1: Initial Outbreak
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [-87.9073, 41.9742]
        },
        "properties": {
            "time": (outbreak_start + timedelta(hours=1)).isoformat(),
            "popup": """<div class="dnd-popup">
                <h3>DAY 1: Patient Zero</h3>
                <p><em>O'Hare Airport overrun</em></p>
                <p>DC 15 Medicine check to identify virus origin</p>
                <button onclick="alert(skillCheck('medicine', 15).message)">
                    Attempt Check
                </button>
            </div>""",
            "icon": "biohazard",
            "iconstyle": {
                "color": "#ff0000"
            }
        }
    })

    # Week 2: Downtown Collapse
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [-87.6298, 41.8781]
        },
        "properties": {
            "time": (outbreak_start + timedelta(days=7)).isoformat(),
            "popup": """<div class="dnd-popup">
                <h3>DAY 7: Quarantine Fails</h3>
                <p><em>Military cordon broken</em></p>
                <p>DC 14 Stealth to avoid patrols</p>
                <button onclick="alert(skillCheck('stealth', 14).message)">
                    Sneak Past
                </button>
            </div>""",
            "icon": "ban",
            "iconstyle": {
                "color": "#ff0000"
            }
        }
    })

    # Week 3: Last Stand
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [-87.6049, 41.8919]
        },
        "properties": {
            "time": (outbreak_start + timedelta(days=14)).isoformat(),
            "popup": """<div class="dnd-popup">
                <h3>DAY 14: Final Evacuation</h3>
                <p><em>Boats overloaded at Navy Pier</em></p>
                <p>DC 12 Persuasion to secure passage</p>
                <button onclick="alert(skillCheck('persuasion', 12).message)">
                    Convince Captain
                </button>
            </div>""",
            "icon": "ship",
            "iconstyle": {
                "color": "#ffffff"
            }
        }
    })

    return {"type": "FeatureCollection", "features": features}


TimestampedGeoJson(
    generate_story_features(),
    period="P1D",
    add_last_point=True,
    auto_play=True,
    loop=False,
    max_speed=10,
    loop_button=True,
).add_to(m)

# ====================
# 5. REAL-TIME DATA (With D&D Encounters)
# ====================
try:
    crime_data = pd.read_json(
        "https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=100")
    print("Loaded real Chicago crime data!")
    for _, crime in crime_data.iterrows():
        if not pd.isna(crime['latitude']) and not pd.isna(crime['longitude']):
            folium.CircleMarker(
                location=[crime['latitude'], crime['longitude']],
                radius=random.randint(2, 5),
                color='red',
                fill=True,
                tooltip=
                f"Zombie Attack: {crime.get('primary_type', 'Unknown')}",
                popup=f"""<div class="dnd-popup" style="width:200px">
                    <h3>🔥 {random.choice(['Gunfight', 'Screams', 'Blood Trail'])}</h3>
                    <p>DC 12 Perception to spot danger</p>
                    <button onclick="alert(skillCheck('perception', 12).message + '\\n' + 
                        (skillCheck('perception', 12).success ? 
                        scavenge() : fightZombies(2))">
                        Investigate
                    </button>
                </div>""").add_to(m)
except Exception as e:
    print(f"Using simulated data (API error: {str(e)})")
    for _ in range(50):
        folium.CircleMarker(
            location=[
                41.8781 + random.uniform(-0.05, 0.05),
                -87.6298 + random.uniform(-0.05, 0.05)
            ],
            radius=random.randint(1, 4),
            color='red',
            fill=True,
            popup=f"""<div class="dnd-popup" style="width:200px">
                <h3>🚨 Zombie Ambush</h3>
                <p>DC 10 Acrobatics to escape</p>
                <button onclick="alert(skillCheck('acrobatics', 10).message + '\\n' + 
                    (skillCheck('acrobatics', 10).success ? 
                    collectSupplies(15) : fightZombies(3))">
                    React
                </button>
            </div>""").add_to(m)

# ====================
# 6. SAFE HOUSES (With D&D Rest Mechanics)
# ====================
safe_houses = [{
    "name": "Wrigley Field",
    "coords": [41.9484, -87.6555],
    "supplies": 250,
    "defense": "CON Save DC 10 vs Exhaustion"
}, {
    "name": "UIC Research Lab",
    "coords": [41.8747, -87.6498],
    "supplies": 180,
    "defense": "INT Check DC 12 for Research Bonus"
}]

for house in safe_houses:
    folium.Marker(location=house["coords"],
                  popup=f"""<div class="dnd-popup" style="width:250px">
            <h3>🛡️ {house['name']}</h3>
            <p><b>Defense:</b> {house['defense']}</p>
            <p><b>Supplies:</b> {house['supplies']}</p>
            <button onclick="alert(scavenge())">
                Search for Supplies
            </button>
            <button onclick="alert('Long Rest: ' + 
                (skillCheck('constitution', 10).message + 
                '\\nHealth restored to full!')">
                Take Long Rest
            </button>
        </div>""",
                  icon=folium.Icon(color="green", icon="home",
                                   prefix="fa")).add_to(m)

# ====================
# 7. QUESTS (With CR Ratings)
# ====================
quests = [{
    "name": "Antidote Run",
    "coords": [41.8919, -87.6049],
    "cr": 3,
    "reward": 80,
    "desc": "Retrieve cure from Navy Pier hospital"
}, {
    "name": "L Train Massacre",
    "coords": [41.8807, -87.6278],
    "cr": 5,
    "reward": 120,
    "desc": "Clear zombies from underground tunnels"
}]

for quest in quests:
    folium.Marker(location=quest["coords"],
                  popup=f"""<div class="dnd-popup" style="width:250px">
            <h3>⚔️ {quest['name']} (CR {quest['cr']})</h3>
            <p><em>{quest['desc']}</em></p>
            <p>Reward: {quest['reward']} supplies</p>
            <button onclick="alert(completeQuest({quest['reward']}, {quest['cr']*2}))">
                Accept Quest
            </button>
        </div>""",
                  icon=folium.Icon(color="orange",
                                   icon="exclamation",
                                   prefix="fa")).add_to(m)

# ====================
# 8. FACTIONS (With Alignment)
# ====================
factions = {
    "The Survivors": {
        "coords": [41.8919, -87.6049],
        "alignment": "LG",
        "quest": "Bring medical supplies (Persuasion DC 12)"
    },
    "The Raiders": {
        "coords": [41.8807, -87.6278],
        "alignment": "CE",
        "quest": "Steal ammunition (Intimidation DC 14)"
    }
}

for name, data in factions.items():
    folium.Marker(location=data["coords"],
                  popup=f"""<div class="dnd-popup" style="width:250px">
            <h3 style="color:{'#1E90FF' if data['alignment'][0]=='L' else '#FF4500'}">{name}</h3>
            <p>Alignment: {data['alignment']}</p>
            <p>Quest: {data['quest']}</p>
            <button onclick="alert(skillCheck(
                data['alignment'][1]=='G' ? 'persuasion' : 'intimidation', 
                data['alignment'][0]=='L' ? 12 : 14
            ).message)">
                Interact
            </button>
        </div>""",
                  icon=folium.Icon(
                      color='blue' if data['alignment'][0] == 'L' else 'red',
                      icon='users',
                      prefix='fa')).add_to(m)

# ====================
# 9. ATMOSPHERIC EFFECTS
# ====================
folium.Circle(location=[41.9, -87.65],
              radius=2000,
              color='#ff0000',
              fill=True,
              fill_opacity=0.2,
              opacity=0.3).add_to(m)

# ====================
# 10. FINAL TOUCHES
# ====================
folium.LayerControl().add_to(m)
m.save("CHICAGO_NIGHTMARE_CAMPAIGN.html")

print("""
🎲 D&D APOCALYPSE CAMPAIGN READY 🎲

=== HOW TO PLAY ===
1. Open CHICAGO_NIGHTMARE_CAMPAIGN.html in browser
2. Click timeline ▶️ button to start outbreak story
3. Interact with locations:
   - 🏥 Safe Houses: Rest and resupply
   - ⚔️ CR-Rated Quests: High-risk missions
   - 🔴 Zombie Zones: Dangerous encounters
   - 👥 Factions: Alignment-based interactions

=== D&D MECHANICS ===
- Roll D20 for skill checks (click button)
- Combat uses attack rolls vs AC
- Supplies work like rations (10/day)
- Long rests restore health (with CON saves)

=== TIPS ===
- Save often (top-right button)
- Complete quests for critical supplies
- Watch for random zombie attacks
- Different factions require different approaches
""")
