


import instaloader
import requests
import json
from datetime import datetime

class InstagramAccountTracer:
    def __init__(self, username, password):
        self.L = instaloader.Instaloader()
        self.username = username
        self.password = password
        self.target_profile = None

    def login(self):
        try:
            self.L.login(username=self.username, password=self.password)
            print("✅ Login Successful!")
            return True
        except Exception as e:
            print(f"❌ Login Failed: {e}")
            return False

    def extract_account_details(self, target_username):
        try:
            # Fetch profile using Instaloader
            profile = instaloader.Profile.from_username(self.L.context, target_username)
            
            # Comprehensive account details extraction
            account_details = {
                "Basic Information": {
                    "Username": profile.username,
                    "Full Name": profile.full_name,
                    "Bio": profile.biography,
                    "External URL": profile.external_url,
                    "Account Type": "Private" if profile.is_private else "Public"
                },
                "Engagement Metrics": {
                    "Followers Count": profile.followers,
                    "Following Count": profile.followees,
                    "Total Posts": profile.mediacount,
                    "Is Business Account": profile.is_business_account,
                    "Is Verified": profile.is_verified
                },
                "Advanced Insights": {
                    "Account Creation Estimate": self.estimate_account_age(profile),
                    "Profile Picture URL": profile.profile_pic_url,
                    "Mutual Connections": self.get_mutual_connections(profile)
                }
            }
            
            return account_details

        except instaloader.exceptions.ProfileNotExistsException:
            print(f"❌ Profile {target_username} does not exist.")
            return None
        except Exception as e:
            print(f"❌ Error extracting details: {e}")
            return None

    def estimate_account_age(self, profile):
        try:
            # Estimate account creation time based on earliest post
            posts = self.L.get_posts(profile)
            earliest_post = next(posts)
            return earliest_post.date_utc.strftime("%Y-%m-%d")
        except:
            return "Unable to determine"

    def get_mutual_connections(self, profile):
        try:
            # Get mutual followers (limited to first 50 for privacy)
            mutual_followers = []
            for follower in profile.get_followers():
                if len(mutual_followers) < 50:
                    mutual_followers.append(follower.username)
                else:
                    break
            return mutual_followers
        except:
            return []

    def advanced_profile_investigation(self, target_username):
        # Additional investigation techniques
        investigation_results = {
            "IP_Geolocation": self.get_ip_geolocation(target_username),
            "Social_Media_Footprint": self.check_cross_platform_presence(target_username)
        }
        return investigation_results

    def get_ip_geolocation(self, username):
        # Simulated IP geolocation (Note: Actual implementation requires paid services)
        try:
            response = requests.get(f"https://ipapi.co/json/?username={username}")
            return response.json() if response.status_code == 200 else "Unable to trace"
        except:
            return "Geolocation service unavailable"

    def check_cross_platform_presence(self, username):
        # Check other social media platforms (simulated)
        platforms = {
            "Twitter": f"https://twitter.com/{username}",
            "Facebook": f"https://facebook.com/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}"
        }
        return platforms

    def save_report(self, details):
        filename = f"instagram_profile_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(details, f, indent=4)
        print(f"📄 Report saved as {filename}")

def main():
    # Get credentials securely
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # Initialize tracer
    tracer = InstagramAccountTracer(username, password)

    # Login
    if tracer.login():
        # Get target username
        target_username = input("Enter the suspicious messenger's Instagram username: ")

        # Extract account details
        account_details = tracer.extract_account_details(target_username)
        
        if account_details:
            # Print detailed report
            print("\n🕵️ Detailed Account Investigation Report:")
            print(json.dumps(account_details, indent=2))

            # Advanced investigation
            advanced_results = tracer.advanced_profile_investigation(target_username)
            print("\n🌐 Advanced Investigation:")
            print(json.dumps(advanced_results, indent=2))

            # Save report
            tracer.save_report({
                "Account_Details": account_details,
                "Advanced_Investigation": advanced_results
            })

            # Safety recommendations
            print("\n🛡️ Safety Recommendations:")
            print("1. Do not engage with suspicious accounts")
            print("2. Report the account to Instagram")
            print("3. Block the user")
            print("4. Never share personal information")

if __name__ == "__main__":
    main()