import os
import re

directory = '.'

# Define string replacements
replacements = {
    # Brand
    'Novus IP | Premium Patent Filing & IP Management': 'Car Service & Repair Center',
    'Novus IP | Client Dashboard': 'Car Service | Customer Dashboard',
    'Novus IP': 'Car Service',
    'Novus <span>IP</span>': 'Auto <span>Fix</span>',
    'Premium Patent Filing & IP Management': 'Expert Auto Repair & Maintenance',
    'Top-Tier IP Law Firm & SaaS': 'Top-Tier Auto Repair & Maintenance',
    'Secure Your Innovation <span class="text-gradient">Globally.</span>': 'Keep Your Vehicle <span class="text-gradient">Running smoothly.</span>',
    'Premium intellectual property management combining specialized legal expertise with an enterprise-grade tracking dashboard. Defend your assets effortlessly.': 'Premium auto repair services combining specialized mechanics with a customer dashboard. Keep your vehicle healthy effortlessly.',
    'Schedule Review': 'Book an Appointment',
    'Explore Practice Areas': 'Explore Our Services',
    'Patent Granted': 'Vehicles Serviced',
    'Global Reach': 'Years Experience',
    'US-2026-X892': '15,000+',
    '120+ Jurisdictions': '25+ Years',
    'Comprehensive Intellectual Property Solutions': 'Comprehensive Auto Repair Solutions',
    'Protecting innovations, brands, and inventions through strategic legal expertise.': 'Protecting your vehicle through strategic maintenance and repair expertise.',
    'Patent Filing': 'Oil Change',
    'Secure exclusive rights to your inventions with our rigorous patent prosecution and filing services.': 'Keep your engine running smoothly and efficiently with our quick and clean oil change services.',
    'Trademark Protection': 'Brake Repair',
    'Safeguard your brand identity, logos, and corporate assets from infringement across all markets.': 'Ensure your safety on the road with our comprehensive brake inspection and repair services.',
    'IP Strategy Consulting': 'AC Service',
    'Develop proactive strategies to commercialize your intellectual property and maximize portfolio ROI.': 'Stay cool during the summer with our professional AC inspection and recharge services.',
    'Global Registration': 'Tyre Rotation',
    'Navigate complex international jurisdictions with our streamlined global PCT filing network.': 'Maximize the life of your tires and improve vehicle handling with our tyre rotation service.',
    'Expertise Across <span class="text-gradient">All IP Domains</span>': 'Expertise Across <span class="text-gradient">All Auto Services</span>',
    'We provide end-to-end intellectual property services tailored for visionary tech companies, research institutions, and individual inventors.': 'We provide end-to-end car repair services tailored for everyday drivers, enthusiasts, and commercial fleets.',
    'Patent Drafting': 'Engine Diagnostics',
    'Meticulous drafting by technical experts ensuring maximum claim scope and defensibility globally.': 'Meticulous diagnostics by technical experts ensuring maximum engine performance and longevity.',
    'International PCT': 'Transmission Repair',
    'Streamlined international filing strategies via the Patent Cooperation Treaty.': 'Streamlined transmission repair and fluid changes to keep your gears shifting smoothly.',
    'High-end legal-tech platform for patent filing and intellectual property management.': 'Local car service center showcasing services and technician profiles publicly, with customer login.',
    
    # Dashboard specific
    'Patent Tracking': 'Service History',
    'Active Applications': 'Pending Appointments',
    'Granted Patents': 'Completed Services',
    'Pending Actions': 'Action Required',
    'Upcoming Renewals': 'Upcoming Maintenance',
    'Renewal Center': 'Reminders',
    'Filing Activity (YTD)': 'Service Activity (YTD)',
    'Notice of Allowance': 'Oil Change Completed',
    'Office Action Response Filed': 'Brake Pad Replacement',
    'Non-Final Rejection': 'Battery Check',
    'Active Portfolio': 'Vehicle Portfolio',
    'New Filing Request': 'New Appointment',
    'Neural Net Optimizer': 'Honda Civic 2019',
    'Quantum Routing Algorithm': 'Toyota Camry 2021',
    'Encrypted Data Storage': 'Ford F-150 2018',
    'Upcoming Annuity Payments': 'Upcoming Scheduled Maintenance',
    'Keep your patents alive by paying maintenance fees.': 'Keep your vehicle alive by performing scheduled maintenance.',
    '4th Year Maintenance Fee': '60,000 Mile Service',
    'Upload invention disclosures, signed declarations, or prior art.': 'Upload vehicle photos, insurance documents, or previous service records.',
    
    # Fonts
    'family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600': 'family=Roboto:wght@300;400;500;700&family=Oswald:wght@400;500;600;700',
    'Novus IP | ': 'Car Service | ',
}

image_replacements = {
    '1497215728101-856f4ea42174': '1517524008697-84bbe3c3fd98', # mechanic garage
    '1450101499163-c8848c66ca85': '1487754180451-c456f719a1fc', # oil change
    '1600880292203-757bb62b4baf': '1632732959827-0b16262b9a71', # brakes
    '1542744173-8e7e53415bb0': '1627916942118-2041db9fb9cd', # AC / tools
    '1581091226825-a6a2a5aee158': '1508353348842-8c9096700c28', # tire
    '1589829085413-56de8ae18c73': '1562259949-e8e7689d7828', # engine
    '1526304640581-d334cdbbf45e': '1493238792000-8113da705763', # transmission
    '1507679799987-c73779587ccf': '1486262715619-67b85e0b08d3', # other legal to auto
    '1555396273-367ea4eb4db5': '1494976388531-d1058494cdd8',
    '1585829365295-ab7cd400c167': '1494976388531-d1058494cdd8'
}

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Text replacements
            for old_text, new_text in replacements.items():
                content = content.replace(old_text, new_text)
                
            # Image replacements (replacing the unsplash ID part)
            for old_id, new_id in image_replacements.items():
                content = content.replace(old_id, new_id)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Conversion complete.")
