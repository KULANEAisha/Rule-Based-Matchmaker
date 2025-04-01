class ProfileManager:
    def _init_(self):
        self.profiles = {}
        self.next_id = 1

    def add_profile(self, name, age, gender, interests, location, gender_preference):
        profile_id = self.next_id
        self.profiles[profile_id] = {
            'id': profile_id,
            'name': name,
            'age': age,
            'gender': gender,
            'interests': set(interests),
            'location': location,
            'gender_preference': set(gender_preference)
        }
        self.next_id += 1
        return profile_id

    def remove_profile(self, profile_id):
        if profile_id in self.profiles:
            del self.profiles[profile_id]

    def get_profile(self, profile_id):
        return self.profiles.get(profile_id)

    def get_all_profiles(self):
        return list(self.profiles.values())


class Matchmaker:
    def _init_(self, profile_manager, weights=None, max_age_gap=20):
        self.profile_manager = profile_manager
        self.weights = weights or {'age': 20, 'interests': 30, 'location': 10}
        self.max_age_gap = max_age_gap

    def _check_gender_compatibility(self, profile_a, profile_b):
        return (profile_b['gender'] in profile_a['gender_preference'] and 
                profile_a['gender'] in profile_b['gender_preference'])

    def calculate_compatibility(self, profile_a, profile_b):
        if not self._check_gender_compatibility(profile_a, profile_b):
            return 0

        age_diff = abs(profile_a['age'] - profile_b['age'])
        age_score = (1 - min(age_diff/self.max_age_gap, 1)) * self.weights['age']

        common_interests = len(profile_a['interests'] & profile_b['interests'])
        total_interests = len(profile_a['interests'] | profile_b['interests'])
        interest_score = (common_interests/total_interests) * self.weights['interests'] if total_interests > 0 else 0

        location_score = self.weights['location'] if profile_a['location'] == profile_b['location'] else 0

        return round(age_score + interest_score + location_score, 2)

    def find_matches(self, target_id, top_n=3):
        target = self.profile_manager.get_profile(target_id)
        if not target:
            return []

        scores = []
        for profile in self.profile_manager.get_all_profiles():
            if profile['id'] == target_id:
                continue
            score = self.calculate_compatibility(target, profile)
            scores.append((profile, score))

        scores.sort(key=lambda x: x[1], reverse=True)  # Sorting in descending order
        return scores[:top_n]


if _name_ == "_main_":
    pm = ProfileManager()
    pm.add_profile("Ali", 34, "male", ["reading", "hiking", "swimming"], "Nairobi", ["female"])
    pm.add_profile("Bob", 45, "male", ["vlogging", "cooking"], "Cairo", ["female"])
    pm.add_profile("Ann", 56, "female", ["mountain_climbing", "travel"], "New York", ["male"])
    pm.add_profile("David", 33, "male", ["reading", "yoga"], "Tokyo", ["female"])
    pm.add_profile("Janet", 22, "female", ["cooking", "racing", "travel"], "Seoul", ["male"])
    pm.add_profile("Lisa", 29, "female", ["singing", "dancing", "swimming"], "Madrid", ["male"])
    pm.add_profile("Ethan", 27, "male", ["gaming", "coding", "reading"], "London", ["female"])
    pm.add_profile("Sophie", 31, "female", ["painting", "hiking", "cooking"], "Paris", ["male"])
    pm.add_profile("Mason", 40, "male", ["fishing", "travel", "sports"], "Sydney", ["female"])
    pm.add_profile("Emma", 24, "female", ["writing", "yoga", "dancing"], "Berlin", ["male"])
    pm.add_profile("Liam", 35, "male", ["photography", "running", "cycling"], "Toronto", ["female"])
    pm.add_profile("Olivia", 28, "female", ["gardening", "baking", "knitting"], "Amsterdam", ["male"])
    pm.add_profile("Noah", 32, "male", ["camping", "surfing", "reading"], "Cape Town", ["female"])
    pm.add_profile("Isabella", 30, "female", ["shopping", "blogging", "cooking"], "Dubai", ["male"])
    pm.add_profile("James", 38, "male", ["golf", "cooking", "travel"], "Singapore", ["female"])
    pm.add_profile("Ava", 26, "female", ["acting", "music", "fashion"], "Los Angeles", ["male"])
    pm.add_profile("Benjamin", 29, "male", ["swimming", "fitness", "reading"], "Rome", ["female"])
    
    matchmaker = Matchmaker(pm, max_age_gap=15)
    
    print("Top matches for Ali:")
    for match, score in matchmaker.find_matches(4):  # Using correct profile ID
        print(f"- {match['name']}: {score}/60 points")
