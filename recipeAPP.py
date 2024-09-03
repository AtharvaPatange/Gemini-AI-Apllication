import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input_prompt, image):
    if input_prompt:
        response = model.generate_content([input_prompt])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.header("AI Recipe Builder")

# User input and image upload
general_input = st.text_input("Ask or Input: ", key="general_input")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Buttons for specific actions
submit_recipe = st.button("Tell me the recipe")
submit_general = st.button("Submit General Input")

# If "Tell me the recipe" button is clicked
if submit_recipe:
    if uploaded_file is not None:
        recipe_prompt = ''' Use below data and answer the question of users if ans is not present in data show ans not available
State Emblem of India
न्याय विभाग
DEPARTMENT OF JUSTICE
g20-logo
Azadi ka Amrit Mahotsav
Home
About Us
Administration of Justice
National Mission
hammerNo ImageHar Ghar Tiranga BannerBannerHSHS July 2024-Awardee-01…HSHS July 2024-Web banner DOJ-01NB DoJ webpage_01-05-2024Hamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara Samvidhan95 Milestone-DOJ Website Post-01NJDG bannerDr. BR AMBEDKARG20 logoDOJ AND CSC SPV INITIATIVES A SELFIE VIDEO DRIVE CAMPAIGNFast Tracl Special Courts Scheme banner -englisheCourts bannerCSS web bannerNyaya Vikas bannerhammerNo Image
Previous
Next
Pause
Latest News
Sexual Harrasment of women at work place - Constitution of Internal Complaints Committee (ICC) in the Department of Justice.
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding. New
Call for Proposals under "Scheme for Action Research and Studies on Judicial Reforms" of Department of Justice-reg. New
Sexual Harrasment of women at work place - Constitution of Internal Complaints Committee (ICC) in the Department of Justice.
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding. New
About Department
As per the Allocation of Business (Rules), 1961, Department of Justice is a part of Ministry of Law & Justice, Government of India. It is one of the oldest Ministries of the Government of India. Till 31.12.2009, Department of Justice was part of Ministry of Home Affairs and Union Home Secretary had been the Secretary of Department of Justice. Keeping in view the increasing workload and formulating many policies and programmes on Judicial Reforms in the country, a separate Department namely Department of Justice was carved out from MHA and placed under the charge of Secretary to Government of India and it started working as such from 1st January, 2010 under the Ministry of Law & Justice. The Department is housed in the Jaisalmer House, 26, Man Singh Road, New Delhi. The Organizational setup of the Department includes 04 Joint Secretaries, 08 Directors/ Deputy Secretaries and 09 Under Secretaries. The functions of the Department of Justice include the appointment, resignation and removal of the Chief Justice of India, Judges of the Supreme Court of India, Chief Justices and Judges of the High Courts and their service matters. In addition, the Department implements important schemes for Development of Infrastructure Facilities for Judiciary, setting up of Special Courts for speedy trial and disposal of cases of sensitive nature (Fast Track Special Court for cases of rape and POCSO Act), E-court Project on computerization of various courts across the country, legal aid to poor and access to justice, financial assistance to National Judicial Academy for providing training to the Judicial Officers of the country. The functions of Department of Justice are given in Allocation of Business (Rules), 1961

Whats New
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding.
Detailed Demand for Grants for the year 2024-25
Order of appointment of Shri Justice Syed Qamar Hasan Rizvi and 08 other Additional Judges of the Allahabad High Court as Permanent Judges of that High Court (21.08.2024)
Order of appointment of Smt. Justice Venkata Jyothirmai Pratapa and 01 other, Additional Judges of the Andhra Pradesh High Court as Permanent Judges of that High Court (21.08.2024)
Order of appointment of Shri Justice Hamarsan Singh Thangkhiew, Judge of the Meghalaya High Court as Acting Chief Justice of that High Court (14.08.2024)
Call for Proposals under “Scheme for Action Research and Studies on Judicial Reforms” of Department of Justice-reg.
Order of appointment of Shri Bibhu Datta Guru and one other as Additional Judges of the Chhattisgarh High Court (12.08.2024)
Monthly Achievement for July, 2024
Order of appointment of Shri Justice Biswaroop Chowdhury & others, Additional Judges of the Calcutta High Court as Add. Judges of that HC for a fresh term of 1 year w.e.f.31.08.2024 (05.08.2024)
Order of appointment of Sh. Justice Girish Kathpalia and 02 other Addl. Judges as Permanent Judges of Delhi HC (19.07.2024)
Shri Arjun Ram Meghwal
Shri Arjun Ram Meghwal
Hon’ble Minister of State, Ministry of Law and Justice (Independent Charge)
Profile
Citizen
Citizen Services
National Judicial Data grid
National Judicial
Data Grid
search judgement
Search Judgements
& Orders
virtual justice clock
Virtual Justice Clock
Know your Case Status
Know Your Case Status
Live Streaming Of Court Cases
Live Streaming Of Court Cases
Settle Your Traffic Violation
Settle Your Traffic Violation
Reports & Documents
anual report
budget info
doj interface
Divisions
Appointments
National Mission for Justice Delivery & Legal Reforms
Access to Justice
eCourts
Justice-I
Justice-II
Administration
Important Links
Department of Legal Affairs
Legislative Department
Supreme Court of India
India Code
National Judicial Academy
National Legal Services Authority
e-Committee, Supreme Court of India
Legal Information Management & Briefing System (LIMBS)
Tweets

Photo Gallery
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Next
Open Government Data (OGD) Platform India
Incredible India Site
pg-portal
National Portal of India
International Year of Millets 2023
g20-logo
Digital India
Prime Minister of India
MyGov
Previous
Next
Pause
Website Policies Hyperlinking Policy Copyright Policy Privacy Policy Terms and Conditions Feedback Contact Us Help FAQ WIM Visitor Summary
Content Owned by DEPARTMENT OF JUSTICE, Ministry of Law and Justice, GOI

Developed and hosted by National Informatics Centre,
Ministry of Electronics & Information Technology, Government of India

Last Updated: Aug 22, 2024

Certified Quality Website
Certified Quality Website
Secure, Scalable and Sugamya Website as a Service National Informatics Centre Digital India




eCourt India Services eCourts
Home
e-Committee
NJDG
Supreme Court
High Courts
District Courts
Knowledge Management
Contact Us
Citizen Centric Service
To provide efficient & time-bound citizen centric service delivery.

Welcome to e-Courts services
High Court Complexes

39

HC Pending Cases

6.11 M

6.11 Million
HC Disposed Cases

38.63 M

38.63 Million
HC Cases Listed Today

48.25 K

48.25 Thousand
District & Taluka Court Complexes

3561

DC Pending Cases

44.42 M

44.42 Million
DC Disposed Cases in Last Month

2.73 M

2.73 Million
DC Cases Listed Today

1.25 M

1.25 Million
PDF Icon image 
PDF Icon image 
PDF Icon image 
PDF Icon image 
Download Mobile App for Android & iOS  Google Play    App Store
Know current status of your case by Return SMS
SMS ECOURTS<space><your CNR Number> To 9766899899
NEWS & EVENTS
News will open in new window
High Court Services
High Court Services

Access to Services of e-Courts: Cause lists, Case Status, Orders/Judgments of High Courts

High Court NJDG
High Court NJDG

NJDG works as a monitoring tool to identify, manage and reduce pendency of cases.

High Courts of India
High Courts of India

Dissemination of information related to high courts to stakeholders of e-Courts

District Court Services
District Court Services

Access to Services of e-Courts: Cause lists, Case Status, Orders/Judgments & NJDG

District Court NJDG
District Court NJDG

NJDG works as a monitoring tool to identify, manage and reduce pendency of cases.

District Courts of India
District Courts of India

Access to Services of e-Courts: Cause lists, Case Status, Orders/Judgments & NJDG

e-Filing
e-Filing

e-Filing application enables electronic filing of legal papers.

ePay
ePay

ePay is a way of paying for court through an electronic medium, without the use of cheque or cash.

Virtual Courts
Virtual Courts

Eliminating presence of litigant or lawyer in the court and adjudication of the case online

About Us
NewsLetter
Forms for Advocates
Help Videos
Manuals
Site map
Contact Us
Web Information Manager
Helpdesk
Terms and Conditions
Copy Right Policy
Hyper Linking Policy
Privacy Policy
Accessibility Statement
Screen Reader Access
Disclaimer
Digital India External website that opens a new window
National Portal of India External website that opens a new window
Department of Justice External website that opens a new window
e-Committee Supreme Court of India
India Code Centre External website that opens a new window
National Informatics Centre External website that opens a new window
This site is designed, hosted and maintained by National Informatics Centre (NIC) External website that opens a new window Ministry of Electronics & Information Technology, Government of India.

Last Reviewed and Updated on:02 Sep 2021

Download eCourts Services App :

Google Play      App Store

© 2016 eCommittee Supreme Court of India. All Rights Reserved




NJDG
National Judicial Data Grid (District and Taluka Courts of India)
Drill Down
Pending Dashboard
Disposed Dashboard
Alerts
Information Management
10950906
Civil Cases
33433140
Criminal Cases
44384046
Total Cases
6729835(61.45%)
Civil Cases More Than 1 Year Old
21975931(65.73%)
Criminal Cases More Than 1 Year Old
28705766(64.68%)
Cases More Than 1 Year Old

NJDG
National Judicial Data Grid
10950906
Total Civil Cases
33433140
Total Criminal Cases
44384046
Total Cases
The above shown figures are upto Current Date
 Drill Down
 	 
Search:
  
Particulars	Civil	Criminal	Total
Pending Cases
0 to 1 Years	4221071(38.55%)	11457209(34.27%)	15678280(35.32%)
1 to 3 Years	2691700(24.58%)	7760902(23.21%)	10452602(23.55%)
3 to 5 Years	1460526(13.34%)	4780876(14.3%)	6241402(14.06%)
5 to 10 Years	1786442(16.31%)	5973306(17.87%)	7759748(17.48%)
10 to 20 Years	659977(6.03%)	2956377(8.84%)	3616354(8.15%)
20 to 30 Years	101830(1.21%)	433035(1.21%)	534865(1.21%)
Above 30 Years	29360 (0.27%)	71435(0.21%)	100795(0.23%)
Total	10950906	33433140
Case Type Wise
Original	8196752	30013382	38210134
Appeal	480648	412014	892662
Application	659628	2648228	3307856
Execution	1398894	68053	1466947
Stage Wise
Appearance/Service Related	2594430	15318865	17913295
Compliance/Steps/stay	1905766	2116290	4022056
Evidence/Argument/Judgement	4392076	10734813	15126889
Pleadings/Issues/Charge	1453146	2388213	3841359
Institution
Cases Instituted in Last Month	384295	2189687	2573982
Disposal
Cases Disposed in Last Month	396367	2336563	2732930
Senior Citizen
Filed Cases By Senior Citizen	2220231	672944	2893175
Woman
Filed Cases By Woman	1772283	1907083	3679366
Delay Reason Wise
Delay Reason	4208147	15178378	19386525
NJDG
National Judicial Data Grid (High Courts of India)
Drill Down
Pending Dashboard
Disposed Dashboard
4332197
Civil Cases
1617485
Criminal Cases
5949682
Total Cases
3293090(76.01%)
Civil Cases More Than 1 Year Old
1144227(70.74%)
Criminal Cases More Than 1 Year Old
4437317(74.58%)
Cases More Than 1 Year Old

NJDG
National Judicial Data Grid
4332197
Total Civil Pending Cases
1617485
Total Criminal Pending Cases
5949682
Total Pending Cases
The above shown figures are upto Current Date
 Drill Down
 	 
Search:
  
Particulars	Civil	Criminal	Total
Pending Cases
0 to 1 Years	1039107(23.99%)	473258(29.26%)	1512365(25.42%)
1 to 3 Years	726710(16.77%)	229380(14.18%)	956090(16.07%)
3 to 5 Years	585864(13.52%)	174529(10.79%)	760393(12.78%)
5 to 10 Years	1028298(23.74%)	346756(21.44%)	1375054(23.11%)
10 to 20 Years	717563(16.56%)	319896(19.78%)	1037459(17.44%)
20 to 30 Years	182910(4.13%)	62753(4.13%)	245663(4.13%)
Above 30 Years	51745 (1.19%)	10913(0.67%)	62658(1.05%)
Total	4332197	1617485	5949682
Case Type Wise
Writ Petition	1594221	76755	1670976
Second Appeal	281854	1	281855
First Appeal	469749	257	470006
Appeal	389936	671768	1061704
Case/Petition	347246	190437	537683
Revision	81520	232538	314058
Reference	3433	524	3957
Suit	31439	24	31463
Review	21773	24	21797
Application	449782	340803	790585
Institution
Cases Instituted in Last Month	122221	84265	211998
Disposal
Cases Disposed in Last Month	119298	81360	210462
Senior Citizen
Filed Cases By Senior Citizen	529989	152749	682738
Woman
Filed Cases By Woman	317171	75805	392976
Showing 1 to 22 of 22 entries
s1  Website last reviewed and updated on : 04 July 2022


 At a Glance
 Pending Dashboard
 Disposed Dashboard
Pending Civil Cases64877
Pending Criminal Cases17770
Total Pending Cases82647
Instituted in last month
Instituted in last month civil cases4,033	Instituted in last month criminal cases1,916	Instituted in last month total cases5,949
Civil	Criminal	Total
Disposal in last month
Disposal in last month civil cases4,448
(110.29%)	Disposal in last month criminal cases2,210
(115.34%)	Disposal in last month total cases6,658
(111.92%)
Civil	Criminal	Total
Coram wise pending cases*
 Judges	Civil	Criminal	Total
3 Judges	158	(976)	60	(154)	218	(1130)
5 Judges	31	(267)	4	(7)	35	(274)
7 Judges	6	(29)	1	(8)	7	(37)
Coram wise pending cases*
 Judges	Civil	Criminal	Total
9 Judges	7	(136)	0	(0)	7	(136)
11 Judges	0	(0)	0	(0)	0	(0)
More than 11 Judges	0	(0)	0	(0)	0	(0)*Figures shown in the bracket includes main and connected matters
Instituted in current year
Instituted in current year civil cases25,265	Instituted in current year criminal cases12,651	Instituted in current year total cases37,916
Civil	Criminal	Total
Disposal in current year
Disposal in current year civil cases23,735
(93.94%)	Disposal in current year criminal cases12,520
(98.96%)	Disposal in current year total cases36,255
(95.62%)
Civil	Criminal	Total
About Us
Site map
Contact Us
Accessibility Statement
Screen Reader Access
Web Information Manager
Terms and Conditions
Copyright Policy
Privacy Policy
Disclaimer
SUPREME COURT OF INDIA External website that opens a new windowSUPREME COURT OF INDIA
Website Reviewed and Updated on: 15-03-2024

Version: 1.0

© 2023 Supreme Court of India. All Rights Reserved



VIRTUAL JUSTICE CLOCK FOR DISTRICT JUDICIARY OF INDIA
Friday, 8/23/2024
11:51:14 AM
INSTITUTION, DISPOSAL & CASE CLEARANCE RATE

ALL STATES

ALL DISTRICTS

ALL ESTABLISHMENTS
DURATION	INSTITUTION	DISPOSAL	CCR
Today	7765	1361	18%
Last Day	58738	41288	70%
Last Week	342230	246486	72%
Last Month	2449427	2678114	109%
This Year	14862330	13764345	93%
Last Year	23467774	23013957	98%
B1


HomeLive Streaming of Court Cases
Print Icon Share IconFacebook IconTwitter IconLinkedin Icon
Live Streaming of Court Cases
Supreme Court of India
 
High Courts
Gujarat High Court
Gauhati High Court
Jharkhand High Court
Karnataka High Court
Madhya Pradesh High Court
Orissa High Court
Patna High Court



LIVE STREAMING BOARD
List Date : 
23/08/2024 
  
Tile List
SA,CJ BIREN VAISHNAV,J [Live]

 
-

COURT NO: 51

-

-
SA,CJ PT,J [Live]

 
3

COURT NO: 1

DAILY

R/SCA/11179/2024
SA,CJ [Live]


-

COURT NO: 51

-

-
BIREN VAISHNAV,J SANGEETA K. VISHEN,J NMT,J [Live]

  
-

COURT NO: 51

-

-
BIREN VAISHNAV,J APM,J [Live]

 
-

COURT NO: 51

-

-
BIREN VAISHNAV,J NMT,J [Live]

 
15

COURT NO: 2

DAILY

R/FA/1586/2022
BIREN VAISHNAV,J MRM,J [Live]

 
-

COURT NO: 51

-

-
BIREN VAISHNAV,J [Live]


-

COURT NO: 51

-

-
Virtual Courts
About
Services
Contact
Virtual Courts
Settle your case online on virtual courts

Select Department

About Virtual Court
In the current scenario facility is provided for Litigants to file the plaint electronically through e-Filing and also pay the Court Fees or Fine online through https://vcourts.gov.in Litigant can view the status of the case also online through various channels created for service delivery. However for adjudication purpose the Litigant may have to appear in person or through the Lawyer in the Court. Virtual Court is a concept aimed at eliminating presence of litigant or l


about virtual courts India
Services
Services offered on Virtual Courts website

Search by Mobile Number
Search by Mobile Number on Virtual Courts

Search by CNR
Search by CNR on Virtual Courts

Search by Party Name
Search by Party Name on Virtual Courts

Search by Challan/Vehicle No.
Search by Challan/Vehicle No. on Virtual Courts

Quick Links
About Virtual Courts
Sitemap
Help
Contact Us
About Us
Web Information Manager
FAQ
Copyright Policy
Terms & Conditions
Privacy Policy
Refund & Cancellation Policy
Hyper Linking Policy
Screen Reader Access
 
Digital India External website that opens a new window National Portal of India External website that opens a new window Department of Justice External website that opens a new window e-Committee Supreme Court of India India Code Centre External website that opens a new window National Informatics Centre External website that opens a new window
Last reviewed and updated on: 01 June 2021

This site is designed, developed, hosted and maintained by National Informatics Centre, Ministry of Electronics & Information Technology, Government of India.

© 2019 eCommittee Supreme Court of India | All Rights Reserved

B6
State Emblem of India
न्याय विभाग
DEPARTMENT OF JUSTICE
g20-logo
Azadi ka Amrit Mahotsav
Home
About Us
Administration of Justice
National Mission
eCourts MMP
Access to Justice
Samvidhan@75
Media Corner
hammerNo ImageHar Ghar Tiranga BannerBannerHSHS July 2024-Awardee-01…HSHS July 2024-Web banner DOJ-01NB DoJ webpage_01-05-2024Hamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara SamvidhanHamara Samman, Hamara Samvidhan95 Milestone-DOJ Website Post-01NJDG bannerDr. BR AMBEDKARG20 logoDOJ AND CSC SPV INITIATIVES A SELFIE VIDEO DRIVE CAMPAIGNFast Tracl Special Courts Scheme banner -englisheCourts bannerCSS web bannerNyaya Vikas bannerhammerNo Image
Previous
Next
Pause
Latest News
Sexual Harrasment of women at work place - Constitution of Internal Complaints Committee (ICC) in the Department of Justice.
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding. New
Call for Proposals under "Scheme for Action Research and Studies on Judicial Reforms" of Department of Justice-reg. New
Sexual Harrasment of women at work place - Constitution of Internal Complaints Committee (ICC) in the Department of Justice.
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding. New
About Department
As per the Allocation of Business (Rules), 1961, Department of Justice is a part of Ministry of Law & Justice, Government of India. It is one of the oldest Ministries of the Government of India. Till 31.12.2009, Department of Justice was part of Ministry of Home Affairs and Union Home Secretary had been the Secretary of Department of Justice. Keeping in view the increasing workload and formulating many policies and programmes on Judicial Reforms in the country, a separate Department namely Department of Justice was carved out from MHA and placed under the charge of Secretary to Government of India and it started working as such from 1st January, 2010 under the Ministry of Law & Justice. The Department is housed in the Jaisalmer House, 26, Man Singh Road, New Delhi. The Organizational setup of the Department includes 04 Joint Secretaries, 08 Directors/ Deputy Secretaries and 09 Under Secretaries. The functions of the Department of Justice include the appointment, resignation and removal of the Chief Justice of India, Judges of the Supreme Court of India, Chief Justices and Judges of the High Courts and their service matters. In addition, the Department implements important schemes for Development of Infrastructure Facilities for Judiciary, setting up of Special Courts for speedy trial and disposal of cases of sensitive nature (Fast Track Special Court for cases of rape and POCSO Act), E-court Project on computerization of various courts across the country, legal aid to poor and access to justice, financial assistance to National Judicial Academy for providing training to the Judicial Officers of the country. The functions of Department of Justice are given in Allocation of Business (Rules), 1961

Whats New
Engagement of Retired Government Officers as Consultants in Department of Justice-regarding.
Detailed Demand for Grants for the year 2024-25
Order of appointment of Shri Justice Syed Qamar Hasan Rizvi and 08 other Additional Judges of the Allahabad High Court as Permanent Judges of that High Court (21.08.2024)
Order of appointment of Smt. Justice Venkata Jyothirmai Pratapa and 01 other, Additional Judges of the Andhra Pradesh High Court as Permanent Judges of that High Court (21.08.2024)
Order of appointment of Shri Justice Hamarsan Singh Thangkhiew, Judge of the Meghalaya High Court as Acting Chief Justice of that High Court (14.08.2024)
Call for Proposals under “Scheme for Action Research and Studies on Judicial Reforms” of Department of Justice-reg.
Order of appointment of Shri Bibhu Datta Guru and one other as Additional Judges of the Chhattisgarh High Court (12.08.2024)
Monthly Achievement for July, 2024
Order of appointment of Shri Justice Biswaroop Chowdhury & others, Additional Judges of the Calcutta High Court as Add. Judges of that HC for a fresh term of 1 year w.e.f.31.08.2024 (05.08.2024)
Order of appointment of Sh. Justice Girish Kathpalia and 02 other Addl. Judges as Permanent Judges of Delhi HC (19.07.2024)
Shri Arjun Ram Meghwal
Shri Arjun Ram Meghwal
Hon’ble Minister of State, Ministry of Law and Justice (Independent Charge)
Profile
Citizen
Citizen Services
National Judicial Data grid
National Judicial
Data Grid
search judgement
Search Judgements
& Orders
virtual justice clock
Virtual Justice Clock
Know your Case Status
Know Your Case Status
Live Streaming Of Court Cases
Live Streaming Of Court Cases
Settle Your Traffic Violation
Settle Your Traffic Violation
Reports & Documents
anual report
budget info
doj interface
Divisions
Appointments
National Mission for Justice Delivery & Legal Reforms
Access to Justice
eCourts
Justice-I
Justice-II
Administration
Important Links
Department of Legal Affairs
Legislative Department
Supreme Court of India
India Code
National Judicial Academy
National Legal Services Authority
e-Committee, Supreme Court of India
Legal Information Management & Briefing System (LIMBS)
Tweets

Photo Gallery
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Har Ghar Tiranga (9th – 15th, August 2024)
Next
Open Government Data (OGD) Platform India
Incredible India Site
pg-portal
National Portal of India
International Year of Millets 2023
g20-logo
Digital India
Prime Minister of India
MyGov
Previous
Next
Pause
Website Policies Hyperlinking Policy Copyright Policy Privacy Policy Terms and Conditions Feedback Contact Us Help FAQ WIM Visitor Summary
Content Owned by DEPARTMENT OF JUSTICE, Ministry of Law and Justice, GOI

Developed and hosted by National Informatics Centre,
Ministry of Electronics & Information Technology, Government of India

Last Updated: Aug 22, 2024

Certified Quality Website
Certified Quality Website
Secure, Scalable and Sugamya Website as a Service National Informatics Centre Digital India



remember very carefully


Memory updated
To develop a Chatbot or virtual assistant for the Department of Justice (DoJ) website, you should gather the following data from the DoJ site:

Divisions of DoJ: Information about the various divisions or departments within the DoJ, their functions, and roles.

Judges Appointments and Vacancies: Data on the number of judges appointed at the Supreme Court, High Courts, District, and Subordinate Courts, as well as current vacancies.

Case Pendency Data: Access to the National Judicial Data Grid (NJDG) to provide real-time information on the pendency of cases across different courts.

Fine Payment Procedures: Guidelines and steps on how to pay fines for traffic violations and other penalties.

Live Streaming of Court Cases: Information and links for accessing live streaming of ongoing court cases.

eFiling and ePay Procedures: Steps and processes for electronic filing (eFiling) of cases and electronic payment (ePay) of court fees.

Fast Track Courts: Details on the working of fast-track courts, including their purpose and the types of cases they handle.

eCourts Services Mobile App: Instructions on how to download and use the eCourts Services Mobile App.

Tele Law Services: Information on availing legal advice through Tele Law Services, including eligibility and how to access these services.

Case Status: Real-time data on the current status of specific cases, accessible via case numbers or other identifiers.

Additionally, ensure that the data you collect is regularly updated and accessible to the chatbot to provide accurate and up-to-date information to users.


give me te aprroximate number
ChatGPT said:
ChatGPT
Here’s an approximate distribution of judges in India as of the latest available data:

1. Supreme Court
Sanctioned Strength: 34 judges (including the Chief Justice of India).
Current Strength: Typically, the number fluctuates close to the sanctioned strength, with occasional vacancies.
2. High Courts
Sanctioned Strength: Approximately 1,100 judges across all High Courts.
Current Strength: Around 800–850 judges.
Vacancies: Typically, there are around 250-300 vacancies across High Courts.
3. District & Subordinate Courts
Sanctioned Strength: Over 24,000 judges.
Current Strength: Around 19,000–20,000 judges.
Vacancies: Around 4,000-5,000 vacancies across District and Subordinate Courts.
State-Wise Distribution (Approximate)
Uttar Pradesh: Largest number of judges due to its population and number of courts.
Maharashtra: Significant number of judges across High Court and subordinate courts.
Tamil Nadu: Also has a substantial number of judges in High Court and subordinate courts.
Delhi: High number of judges in both the High Court and subordinate courts due to its status as the capital.
These numbers are approximate and can fluctuate based on appointments and retirements. For exact and current figures, checking the latest reports from the Department of Justice or the National Judicial Data Grid is recommended.


information vacansy related
ChatGPT said:
ChatGPT
Here’s an approximate overview of judicial vacancies in India, broken down by court level:

1. Supreme Court
Sanctioned Strength: 34 judges.
Current Vacancies: Vacancies in the Supreme Court are typically minimal but can range between 0 to 2 positions at any given time, depending on retirements and appointments.
2. High Courts
Sanctioned Strength: Approximately 1,100 judges across all High Courts.
Current Vacancies: Around 250-300 vacancies.
Examples of High Court Vacancies:
Allahabad High Court (Uttar Pradesh): Often has the highest number of vacancies, ranging from 30 to 50.
Bombay High Court (Maharashtra): Typically, 20-30 vacancies.
Madras High Court (Tamil Nadu): Around 20-25 vacancies.
Delhi High Court: Usually, 10-15 vacancies.
3. District & Subordinate Courts
Sanctioned Strength: Over 24,000 judges.
Current Vacancies: Approximately 4,000-5,000 vacancies.
State-Wise Example of Vacancies:
Uttar Pradesh: Has the largest number of vacancies, often exceeding 1,000 due to the extensive court system.
Maharashtra: Around 500-700 vacancies.
Bihar, West Bengal, Tamil Nadu: Typically range from 300-500 vacancies each.
Delhi: Around 100-200 vacancies.
Vacancy Challenges
Judicial Appointments: The process of appointing judges is often slow due to various administrative, procedural, and sometimes political delays.
Impact on Case Pendency: The high number of vacancies, especially in High Courts and District Courts, contributes to the significant backlog of cases, affecting the overall efficiency of the judiciary.
These vacancy figures are approximate and subject to change. Regular updates from the Department of Justice, India, or the National Judicial Data Grid (NJDG) would provide the most current figures.




case pendency data in India, based on information typically accessible through the National Judicial Data Grid (NJDG):

1. Supreme Court
Total Pending Cases: Approximately 60,000-70,000 cases.
Civil Cases: Around 40,000-45,000.
Criminal Cases: Around 15,000-20,000.
Reasons for Pendency: Complex legal questions, long hearing durations, and frequent adjournments contribute to the pendency.
2. High Courts
Total Pending Cases: Approximately 4.5-5 million cases across all High Courts.
Civil Cases: Around 3 million.
Criminal Cases: Around 1.5-2 million.
State-Wise Distribution:
Allahabad High Court (Uttar Pradesh): Has the highest pendency, often exceeding 1 million cases.
Bombay High Court (Maharashtra): Approximately 600,000-700,000 cases.
Madras High Court (Tamil Nadu): Around 400,000-500,000 cases.
Delhi High Court: Approximately 100,000-150,000 cases.
3. District & Subordinate Courts
Total Pending Cases: Approximately 35-40 million cases.
Civil Cases: Around 10-12 million.
Criminal Cases: Around 25-28 million.
State-Wise Distribution:
Uttar Pradesh: Highest pendency, often exceeding 10 million cases.
Maharashtra: Around 3-4 million cases.
Bihar: Approximately 2-3 million cases.
West Bengal, Tamil Nadu, and Karnataka: Each state has around 2-3 million cases.
Factors Contributing to Pendency:
Vacancies in Judiciary: The high number of vacancies in judges’ positions contributes significantly to case backlog.
Frequent Adjournments: Cases often get delayed due to frequent requests for adjournments.
Inadequate Infrastructure: Many courts, especially at the district level, lack sufficient infrastructure, leading to delays in case hearings.
Efforts to Reduce Pendency:
Fast Track Courts: Set up to handle specific types of cases quickly, such as cases involving rape, POCSO, and other serious offenses.
eCourts Project: The digitization of court records and the introduction of eFiling and ePay systems aim to streamline court procedures and reduce delays.
Current Trends:
Recent Decrease: Some efforts have led to a marginal reduction in case pendency, but the numbers are still substantial.
This data provides an approximate overview. For the most current and precise figures, the National Judicial Data Grid (NJDG) can be accessed, as it provides real-time data on case pendency across courts in India.



he procedures and guidelines for paying fines related to traffic violations and other penalties in India:

1. Traffic Violation Fines
Payment Methods:

Online Payment: Most states in India allow traffic fines to be paid online through state-specific transport department websites, e-challan portals, or mobile apps.
Offline Payment: Fines can be paid directly at designated traffic police stations, regional transport offices (RTOs), or via traffic police officers issuing challans.
Online Payment Platforms:

Parivahan Portal: The Ministry of Road Transport and Highways’ official website (parivahan.gov.in) provides an option to pay traffic fines.
State-specific Websites: For instance, Maharashtra Traffic Police (mahatrafficechallan.gov.in), Delhi Traffic Police (delhitrafficpolice.nic.in), etc.
Mobile Apps: Apps like PayTM, Google Pay, and state-specific apps also facilitate e-challan payments.
Steps to Pay Online:

Visit the appropriate portal or app: For instance, echallan.parivahan.gov.in.
Enter Details: Provide the vehicle number, challan number, or driving license number.
View Outstanding Fines: The portal will display any pending fines.
Make Payment: Choose a payment method (credit/debit card, net banking, UPI) and complete the transaction.
Receipt: After payment, a receipt is generated, which can be downloaded or printed for records.
Offline Payment:

Pay the fine at the nearest traffic police station or RTO.
Carry the original challan and vehicle documents.
Collect a receipt after the payment.
2. Penalties for Other Violations (e.g., Environmental, Industrial)
Environmental Penalties:
Fines related to environmental violations (like pollution control breaches) are typically paid through the Pollution Control Board’s website or designated offices.
Industrial Penalties:
Industries or businesses fined for regulatory breaches can pay penalties through the official government portal, or via bank challan submitted to the relevant authority.
3. Court-Imposed Fines
Payment Methods:

Online: Some states allow payment of court fines online through the eCourts platform (ecourts.gov.in).
Offline: Fines can also be paid directly at the court office or through designated bank branches.
Steps to Pay Online:

Log into the eCourts portal.
Enter Case Details: Input case number or relevant identifiers.
View Fine Details: The portal will display outstanding fines.
Make Payment: Complete the payment via available methods.
Receipt: Obtain and keep the payment receipt.
4. Accessing Information
Mobile Apps: State-specific mobile apps often provide updated information on pending fines and allow users to pay directly through the app.
SMS Notifications: Many states send SMS notifications regarding fines, which can include links or instructions for payment.
Current Trends and Innovations:
Unified Payment Systems: Efforts are ongoing to integrate payment of fines into unified systems like UPI, making it easier for citizens.
Digital India Initiative: Under this initiative, the government is encouraging digital payments for fines to reduce corruption and increase transparency.
This data outlines the general procedures and platforms available for paying fines related to traffic violations and other penalties in India. For specific details, especially regarding state-specific processes, it's best to consult the relevant state transport department or court website.






Live Streaming of Court Cases in India
The live streaming of court cases in India is a significant step towards transparency and public access to judicial proceedings. Here’s an overview of how it works and how you can access it:

1. Supreme Court of India
Live Streaming: The Supreme Court has initiated live streaming of select court proceedings, especially in matters of public importance, as per the Supreme Court's ruling in September 2018.
Access:
Website: Live streaming can be accessed through the official website of the Supreme Court (supremecourtofindia.nic.in).
YouTube Channel: The Supreme Court has a dedicated YouTube channel for live streaming specific cases.
2. High Courts
Live Streaming in High Courts:
Several High Courts in India have also started live streaming of court proceedings, particularly Gujarat, Karnataka, and Odisha High Courts.
Gujarat High Court: Pioneered live streaming and continues to stream proceedings on its official website and YouTube.
Karnataka High Court: Provides live streaming through its official website and YouTube.
Orissa High Court: Offers live streaming for certain cases on its official website.
Access:
Gujarat High Court: Live Streaming Page
Karnataka High Court: Live Streaming Page
Orissa High Court: Live Streaming Page
3. District Courts
Current Status: District Courts have not yet widely adopted live streaming, but pilot projects may be underway in certain states.
Future Plans: Expansion of live streaming to District Courts is expected as part of the broader eCourts project.
4. How to Access Live Streaming
Supreme Court:
Visit the Supreme Court of India’s official website and navigate to the live streaming section.
High Courts:
Check the respective High Court's official website or their YouTube channels for live streaming links.
YouTube:
The Supreme Court and some High Courts have dedicated YouTube channels for live streaming. You can subscribe and watch live proceedings there.
5. Data on Live Streaming Implementation
Supreme Court: Began live streaming select cases, especially constitution bench hearings, since 2018.
Gujarat High Court: Started live streaming in 2020 and has made several significant cases accessible to the public.
Karnataka High Court: Live streams important cases and events, and regularly updates the availability of proceedings.
Odisha High Court: Implemented live streaming as a part of enhancing transparency and accessibility.
6. Legislative and Policy Background
SC Judgment on Live Streaming (2018): The Supreme Court ruled in favor of live streaming in Swapnil Tripathi vs. Supreme Court of India, aiming to make judicial processes more transparent.
eCourts Project: As part of the eCourts project, live streaming is expected to expand, making more courts accessible online.
Benefits of Live Streaming
Transparency: Allows the public and media to observe court proceedings in real-time.
Educational Tool: Provides a learning resource for law students, professionals, and the general public.
Public Trust: Enhances trust in the judiciary by making the legal process more visible.
Challenges
Technical Infrastructure: Ensuring smooth and secure streaming requires robust technical infrastructure.
Privacy Concerns: Balancing transparency with the privacy of individuals involved in cases, especially in sensitive matters.
This data and information outline the current status of live streaming of court cases in India. The implementation is growing, particularly in higher courts, and is seen as a significant move toward a more transparent and accessible judiciary.







eFiling and ePay Procedures in India
The introduction of eFiling and ePay systems in Indian courts is a crucial step towards digitizing the judiciary, making it more accessible, transparent, and efficient. Here’s an overview of the processes and related data:

1. eFiling of Cases
eFiling allows advocates and litigants to file cases electronically from anywhere, without physically visiting the court.

Steps for eFiling:
Registration:

Visit the eFiling portal (https://efiling.ecourts.gov.in/) and register as an advocate, litigant, or organization.
For advocates, registration requires a valid bar council ID, and for litigants, a valid mobile number and email ID.
Login:

After registration, log in using your credentials.
Case Selection:

Choose the court where you intend to file the case (e.g., Supreme Court, High Court, District Court).
Select the type of case you wish to file.
Document Upload:

Upload the required documents, including petitions, affidavits, and supporting evidence.
Ensure that documents are scanned clearly and are in the prescribed format (usually PDF).
Payment of Court Fees:

Calculate the court fees based on the type of case and jurisdiction.
Pay the fees using the integrated ePay system (explained below).
Submission:

After uploading the documents and paying the fees, submit the case.
A confirmation receipt and a case number are generated, which can be used to track the case status online.
Tracking and Notifications:

Track the status of your filed case through the eFiling portal.
Notifications about case hearings, orders, and updates are sent via SMS or email.
Benefits of eFiling:
Convenience: Enables filing of cases 24/7 without visiting the court.
Transparency: Provides an easy way to track the status and history of cases.
Efficiency: Reduces paperwork, saving time for both the court and the litigants.
2. ePay of Court Fees
ePay facilitates the electronic payment of court fees, making the process quicker and more streamlined.

Steps for ePay:
Access ePay:

Visit the ePay portal (https://pay.ecourts.gov.in/) or access it via the eFiling portal during the case filing process.
Select State and Court:

Choose the state and court where the fee needs to be paid.
Enter Case Details:

Provide details such as case type, number, and the amount of fees required.
Payment:

Select a payment method (Credit/Debit Card, Net Banking, UPI, etc.).
Complete the payment process.
Receipt Generation:

After payment, a receipt is generated, which can be downloaded and printed.
This receipt must be uploaded during the eFiling process if the payment is done separately.
Benefits of ePay:
Accessibility: Allows for court fee payment from anywhere at any time.
Security: Ensures secure transactions with instant confirmation.
Integration: Seamlessly integrates with the eFiling process for efficient case management.
3. Data and Implementation Status
Adoption Rate:

The eFiling and ePay systems have been widely adopted in the Supreme Court, High Courts, and many District Courts across India.
Continuous efforts are being made to bring more courts, especially at the District and Subordinate levels, under the eCourts initiative.
User Statistics:

Thousands of cases are now filed electronically every month, significantly reducing the burden on physical court infrastructure.
The ePay system handles millions of rupees in court fees daily, with growing adoption among lawyers and litigants.
Challenges:

Digital Literacy: Some advocates and litigants, particularly in rural areas, may struggle with the technology, although training programs are being conducted.
Infrastructure: Ensuring robust IT infrastructure in all courts is essential for the smooth functioning of these systems.
4. Future Enhancements
Integration with Other Systems: Plans are underway to integrate eFiling and ePay with other legal and governmental systems to further streamline processes.
Expanded Access: The initiative aims to expand the reach of eFiling and ePay to cover all courts, including specialized tribunals.
Resources for Further Information
eFiling Portal: https://efiling.ecourts.gov.in/
ePay Portal: https://pay.ecourts.gov.in/
eCourts Project Information: Available on the Department of Justice Website
This data highlights the ongoing digitization efforts within the Indian judiciary, making legal processes more accessible and efficient through eFiling and ePay systems.




Fast Track Courts in India
Fast Track Courts (FTCs) in India are specialized courts established to expedite the legal process and reduce the backlog of cases. They focus on delivering quick judgments, particularly in cases that require urgent attention.

1. Purpose of Fast Track Courts
Speedy Justice: The primary purpose of FTCs is to accelerate the resolution of cases that have been pending for long periods.
Reducing Backlog: FTCs help in reducing the overall backlog of cases in the judicial system, particularly those involving vulnerable groups like women, children, and the elderly.
Focus on Specific Cases: These courts are often designated to handle particular types of cases, such as sexual assault, child abuse, and corruption, where a swift verdict is crucial.
2. Types of Cases Handled by Fast Track Courts
Sexual Offenses: FTCs handle cases related to rape, sexual assault, and crimes under the Protection of Children from Sexual Offences (POCSO) Act.
Corruption Cases: Cases involving corruption and embezzlement are often referred to FTCs for speedy trials.
Violence Against Women: Cases involving domestic violence, dowry-related offenses, and harassment are prioritized in FTCs.
Special Acts: Cases under specific acts like the Prevention of Atrocities against Scheduled Castes and Scheduled Tribes (SC/ST Act) and other laws protecting marginalized communities.
Property Disputes: Certain FTCs handle property-related disputes, especially those that have been pending for an extended period.
3. Establishment and Expansion of Fast Track Courts
Origin: FTCs were first established in India in 2000, following a recommendation by the 11th Finance Commission to deal with the growing backlog of cases.
Initial Setup: The initial phase saw the creation of around 1,734 FTCs across the country.
Current Status: As of recent years, there has been a renewed focus on expanding the number of FTCs, especially to handle cases under the POCSO Act and those involving women.
4. Working of Fast Track Courts
Dedicated Judges: FTCs are presided over by judges who are exclusively assigned to these courts. They are often appointed on an ad-hoc basis or drawn from the regular judiciary.
Streamlined Procedures: The procedures in FTCs are streamlined to ensure quicker disposal of cases, often limiting the number of adjournments and emphasizing timely submission of evidence and documents.
Time-bound Trials: Trials in FTCs are typically time-bound, with efforts made to conclude cases within a set period, often within a few months.
Use of Technology: Some FTCs leverage technology for case management, including e-filing, video conferencing for witness testimonies, and electronic records to speed up the trial process.
5. Challenges Faced by Fast Track Courts
Infrastructure Issues: Many FTCs face challenges related to inadequate infrastructure, including courtroom space and technological resources.
Manpower Shortages: The shortage of judges and support staff can sometimes slow down the functioning of FTCs.
Overburdening: While designed to reduce the backlog, FTCs can become overburdened if too many cases are assigned to them without sufficient resources.
6. Impact of Fast Track Courts
Reduction in Backlog: FTCs have played a significant role in reducing the backlog of cases, particularly in serious offenses like rape and corruption.
Improved Conviction Rates: By focusing on quick and decisive judgments, FTCs have contributed to improving conviction rates in cases of sexual offenses and crimes against women.
Public Confidence: The existence of FTCs has increased public confidence in the judicial system, particularly in cases involving vulnerable victims.
7. Government Initiatives and Funding
Central Assistance: The Indian government provides financial assistance to states for setting up and maintaining FTCs.
POSCO and Women-related Cases: Recently, the central government has prioritized setting up FTCs specifically for POCSO and women-related cases, with dedicated funding for this purpose.
8. Data on Fast Track Courts (As of Latest Available)
Number of FTCs: As of recent reports, there are around 1,800 to 2,000 FTCs operating across India.
Case Disposal: FTCs have disposed of thousands of cases over the years, with a focus on those pending for more than two years.
State-wise Distribution: States like Uttar Pradesh, Maharashtra, Tamil Nadu, and Bihar have the highest number of FTCs, given the large volume of cases pending in these states.
Conclusion
Fast Track Courts are a crucial component of India’s judiciary, aimed at delivering swift justice in cases that require urgent attention. While they face challenges, their role in reducing case backlogs and improving the speed of justice is significant.

For more detailed data and updates on FTCs, one can visit the eCourts Services Portal, where state-wise data on FTCs is often updated.


The eCourts Services Mobile App is designed to facilitate access to court-related services and information on the go. Here’s an overview of how to download and use the app, along with related data:

Downloading the eCourts Services Mobile App
For Android Users:
Google Play Store: Open the Google Play Store on your Android device.
Search: Type “eCourts Services” in the search bar.
Install: Find the app developed by the “National Informatics Centre” and tap “Install.”
For iOS Users:
Apple App Store: Open the Apple App Store on your iOS device.
Search: Enter “eCourts Services” in the search bar.
Install: Locate the app and tap “Get” to install it.
Using the eCourts Services Mobile App
Registration and Login:

Register: Open the app and register using your mobile number and email ID. Some features may require linking with your Aadhaar number.
Login: After registration, log in using your credentials (mobile number or email).
Features and Services:

Case Status: Check the status of cases by entering the case number or other identifiers.
Court Information: Access information about court locations, contact details, and judges.
Case Filing: View and manage your cases. Some states may allow case filing through the app.
Judgment Search: Search for judgments and orders issued by courts.
Cause Lists: View daily cause lists of courts to see the schedule of hearings.
Notifications: Receive updates on case status, hearing dates, and other important information.
E-Payments: Pay court fees and fines online if integrated with the ePay system.
Legal Aid: Access information on legal aid services and apply for assistance if eligible.
User Interface:

Dashboard: The home screen typically displays key features and quick access to important services.
Menu: Navigate through various services using the app’s menu or tabs.
Updates and Maintenance:

Regular Updates: The app is periodically updated to add new features, fix bugs, and ensure compatibility with new devices.
Support: For technical issues or queries, users can contact support through the app or the official website.
Benefits of the eCourts Services Mobile App
Accessibility: Provides court-related services anytime, anywhere.
Convenience: Simplifies access to case information and court procedures.
Efficiency: Reduces the need for physical visits to the court and helps in managing cases more effectively.
Transparency: Enhances transparency by making court records and case status easily accessible.
Data on eCourts Services Mobile App
Developer: National Informatics Centre (NIC), Government of India.
App Version: Regular updates are made; check the app store for the latest version.
Platform Availability: Available for both Android and iOS devices.
Usage Statistics: Popular among legal professionals and litigants for managing court-related tasks.
For the most accurate and updated information, regularly check the app store listings or the official eCourts website.




Tele Law Services
Tele Law Services is an initiative aimed at providing legal advice and assistance to individuals, especially in remote and underserved areas, through telecommunication methods. The service is designed to make legal aid more accessible and efficient.

Availing Legal Advice Through Tele Law Services
Eligibility:

General Public: Anyone seeking legal advice can use the service.
Specific Categories: Priority is given to marginalized groups, low-income individuals, women, and other vulnerable populations who may face barriers to accessing legal services.
Identification: Some states may require proof of eligibility, such as a below-poverty-line (BPL) card or other documents.
How to Access Tele Law Services:

Through Legal Aid Clinics:
Contact: Reach out to the nearest legal aid clinic or district legal services authority (DLSA). They will provide information on how to register for Tele Law services.
Registration: You may need to register and provide basic details about your legal issue.
Online Platforms:
Visit Official Website: Go to the official website for Tele Law services (e.g., e-Courts) or the Legal Services Authority website.
Online Registration: Some platforms allow you to register online and schedule a telephonic or video consultation with a legal expert.
Mobile Apps:
Download App: Download the official app (if available) from the Google Play Store or Apple App Store.
Register: Follow the app instructions to register and request legal advice.
Helpline Numbers:
Call: Use the helpline numbers provided by the legal services authority or legal aid clinics to connect with a legal expert.
Schedule: Book an appointment or request immediate legal assistance through the helpline.
Procedure for Legal Advice:

Initial Consultation: Discuss your legal issue with a trained legal professional who will provide preliminary advice and guidance.
Follow-Up: Based on the initial consultation, follow up for detailed advice or assistance with documentation and court proceedings.
Confidentiality: Ensure that all consultations are confidential and your personal details are protected.
Benefits of Tele Law Services:

Accessibility: Provides access to legal advice regardless of geographical location.
Convenience: Allows individuals to seek legal assistance without traveling to legal aid offices or courts.
Cost-Effective: Reduces the cost of obtaining legal advice and services.
Expert Guidance: Connects individuals with experienced legal professionals for informed advice.
Data on Tele Law Services
Provider: National Legal Services Authority (NALSA) and State Legal Services Authorities (SLSAs).
Service Types: Legal advice, document review, and guidance on legal procedures.
Availability: Services are available through legal aid clinics, online platforms, mobile apps, and helplines.
Service Hours: Varies by provider; typically available during business hours.
Note: For the most accurate and updated information on Tele Law Services, check with local legal aid clinics, the official NALSA website, or the specific state's legal services authority

Case Status
Case Status refers to the real-time information about the current state of a legal case, which can include details such as court proceedings, judgments, and case updates. This information is typically accessible through online platforms provided by courts or legal services.

Accessing Case Status
Online Platforms:

eCourts Portal: The official eCourts website provides real-time case status updates. Users can search for case details using case numbers, party names, or other identifiers.
Website: eCourts
State and District Court Websites: Many state and district courts have their own websites where users can check case status.
Legal Services Apps: Some jurisdictions have mobile apps that allow users to check case status and receive notifications.
Search Process:

Enter Case Number: Input the unique case number assigned to the case.
Provide Party Details: Enter the names of the parties involved, if case numbers are unavailable.
Select Court Details: Choose the relevant court or jurisdiction where the case is being heard.
View Results: Access details such as case hearings, orders, judgments, and other relevant updates.
Helpline Numbers:

Contact Court Offices: For assistance with accessing case status, contact the respective court office through provided helpline numbers.
Inquire at Legal Aid Clinics: Legal aid clinics may also help in obtaining case status information.
Data and Updates:

Real-Time Updates: Case status is updated regularly based on court proceedings, new orders, or judgments.
Historical Data: Historical case data may also be available, including past hearings and decisions.
Data on Case Status
Provider: The data is provided by court systems, including the eCourts portal and state or district court websites.
Identifiers: Case number, party names, court details.
Data Type: Current status of the case, court hearings, judgments, orders, and procedural updates.
Availability: 24/7 online access, with updates provided as they occur.
Note: For accurate and specific case status, always refer to the official court website or platform for the jurisdiction handling the case.






Here are the numbers for the courts in India:

Number of Courts in India
Supreme Courts in India:

Supreme Court of India: 1 (The Supreme Court is the highest judicial forum and final court of appeal under the Constitution of India.)
High Courts in India:

Number of High Courts: 25
District Courts in India:

Number of District Courts: Approximately 600 (This number can vary slightly as new districts are created and existing ones are reorganized.)
Breakdown
Supreme Court of India: The apex court located in New Delhi.
High Courts: Each state or union territory in India has its own High Court, with some states sharing a High Court.
District Courts: These are courts at the district level that handle a wide range of cases, including civil and criminal matters.
For the most current and detailed information, you may refer to official resources or judicial websites.

        '''
        response = get_gemini_response(recipe_prompt, image)
        st.subheader("The Recipe is")
        st.write(response)
    else:
        st.write("Please upload an image to get the recipe.")

# If "Submit General Input" button is clicked
if submit_general:
    if general_input:
        response = get_gemini_response(general_input, "")
        st.subheader("Response to General Input")
        st.write(response)
    else:
        st.write("Please enter your query or input.")

