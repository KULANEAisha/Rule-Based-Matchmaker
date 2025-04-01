# Rule-Based-Matchmaker
A rule-based compatibility scoring system for dating applications, implementing user profile management and intelligent match recommendations.


## Features 
-  **Profile Management** (Create/Update/Delete)
-  **Compatibility Scoring Algorithm**
-  Location-based matching
-  Age gap analysis
-  Interest-based recommendations
-  Gender preference handling

## System Design 
### Core Components
| Component | Description |
|-----------|-------------|
| **Profile Manager** | Handles user CRUD operations |
| **Rule Engine** | Implements scoring logic for: <br>- Age gap (±10yr penalty/reward) <br>- Location proximity <br>- Shared interests <br>- Gender preferences |
| **Match Generator** | Ranks matches by compatibility score |

### Scoring Rules
| Attribute | Scoring Logic |
|-----------|---------------|
| Shared Interests | +10 per common interest |
| Age Gap | ≤5yrs: +10 <br>6-10yrs: +5 <br>>10yrs: -5 |
| Location | Same city: +10 <br>50mi radius: +5 |
| Gender Match | Preference met: +10 <br>Not met: -5 |

## Installation 
```bash
git clone https://github.com/yourusername/APT3020-Matchmaking-System.git
cd APT3020-Matchmaking-System
