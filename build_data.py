#!/usr/bin/env python3
"""Builds data.json for the UAE medical-equipment-services comparison matrix.
Merges hand-verified matrix flags with the full raw scrape catalogs.
Flag values: 1 = present, 0.5 = present but partial/misconfigured (see note), 0 = not found, None = not recorded.
"""
import json

SRC = '/private/tmp/claude-501/-Users-pl-qabooswebsite/86d703ff-cab6-44e7-a8e0-fae21e138a48/tasks/wwkbrww14.output'
raw = json.load(open(SRC))['result']['catalogs']
raw_by_host = {}
for c in raw:
    host = c['url'].replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0]
    raw_by_host[host] = c

def F(v, note=None):
    return {"v": v, "n": note} if note else {"v": v}

companies = [
 dict(id="qaboos", name="Qaboos Best Medical & Laboratory Equipment Repairing Est.", short="Qaboos Best",
   url="https://ppplll123.github.io/qaboosbest-website/", category="direct", emirate="Dubai", us=True,
   features=dict(
     arabic=F(1, "Full bilingual: crawlable /ar/ page, RTL, reciprocal hreflang"),
     form=F(0.5, "mailto-based form — opens the visitor's email app; no server backend"),
     whatsapp=F(0), livechat=F(0),
     map=F(1, "Embedded map pinned to Boulevard Plaza Tower 2"),
     tel=F(1, "All phone numbers are tel: links"),
     faq=F(1, "7 Q&As in English and Arabic + FAQPage JSON-LD"),
     blog=F(0), careers=F(1, "Sales Officer vacancy + JobPosting JSON-LD"), social=F(0),
     schema=F(1, "MedicalBusiness + FAQPage + JobPosting"), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(1), amc=F(1), est=F(1), install=F(1), parts=F(1),
     training=F(0), radiation=F(0)),
   trust=dict(years="Licensed Feb 2025 (new establishment)", iso="—",
     testimonials="—", client_logos="—", oem_logos="—",
     other="Displays full DET professional license (No. 1475682) with verify link — the only site in this set showing a verifiable trade license"),
   notes=["License expiry shown as printed on the license document (19/02/2026)",
          "Contact form has no backend — it opens the visitor's mail client"]),

 dict(id="paramount", name="Paramount Medical Equipment Trading LLC", short="Paramount",
   url="https://paramountuae.com/", category="trading", emirate="Sharjah",
   features=dict(
     arabic=F(0), form=F(0.5, "Contact form present, but its captcha shortcode renders as raw unprocessed text"),
     whatsapp=F(1), livechat=F(1, "Tawk.to"),
     map=F(1), tel=F(None), faq=F(0),
     blog=F(1, "100+ posts, weekly cadence"), careers=F(0),
     social=F(0.5, "FB/IG/LinkedIn icons; LinkedIn footer link points to an /admin/ URL (broken for visitors)"),
     schema=F(0.5, "Single minimal Organization block (name + url only)"), shop=F(1, "WooCommerce shop, 21 products priced in AED")),
   services=dict(ppm=F(1), calibration=F(1), amc=F(1), est=F(0), install=F(1), parts=F(None),
     training=F(0), radiation=F(1, "Lead shielding, FANR consultation, radiation QA/QC")),
   trust=dict(years="Founded 2002 — '20+ years' counters", iso="ISO 9001 (text claim, no certificate shown)",
     testimonials="4 named doctors", client_logos="—", oem_logos="18 partner logos",
     other="WMC Excellence Award 2022; Arab Health / AEEDC exhibition track record"),
   notes=["Contact-form captcha shortcode renders as raw text", "LinkedIn footer link points to an /admin/ URL"]),

 dict(id="ihag", name="IHAG — Maintenance for Medical Equipment", short="IHAG",
   url="https://ihag.ae/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(1, "PHP contact/quote form"), whatsapp=F(0, "Number shown as plain text only"),
     livechat=F(0), map=F(0.5, "'Open Map' link only — no embed"), tel=F(0, "Phone shown as plain text"),
     faq=F(1, "6 Q&As"), blog=F(0), careers=F(0), social=F(0), schema=F(0), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(0.5, "X-ray QC tests; general calibration not listed"), amc=F(1),
     est=F(0), install=F(1), parts=F(0.5, "Medical equipment supplies"),
     training=F(1, "RPO (Radiation Protection Officer) course"), radiation=F(1, "FANR license management, shielding, X-ray QC")),
   trust=dict(years="—", iso="—", testimonials="—", client_logos="—", oem_logos="—",
     other="'100% work guaranteed'; 24/7 support; 250+ facilities counter"),
   notes=["Contact email is a hotmail.com address", "Privacy/terms footer links are dead '#' anchors"]),

 dict(id="adamsmed", name="Adamsmed Medical Equipment LLC", short="Adamsmed",
   url="https://adamsmed.ae/", category="trading", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(0.5, "Form renders as unconfigured 'Contact Form Demo (#4)' with generic field labels"),
     whatsapp=F(1), livechat=F(0), map=F(0.5, "Footer maps link only — no embed"), tel=F(1),
     faq=F(1, "14 Q&As across two pages"), blog=F(1, "At least one post"), careers=F(0), social=F(0),
     schema=F(1, "Organization, WebSite + SearchAction via Rank Math"), shop=F(1, "External store adamsmedonline.com")),
   services=dict(ppm=F(1), calibration=F(1), amc=F(1), est=F(0), install=F(1), parts=F(None),
     training=F(0), radiation=F(0)),
   trust=dict(years="—", iso="ISO 9001:2015 (text claim)", testimonials="—", client_logos="—",
     oem_logos="13+ named OEM partners with write-ups",
     other="Official Periodmed distributor (MENA); installations claimed across Asia/ME/Africa"),
   notes=["Contact form renders as an unconfigured demo", "'Download our Profile' brochure button links to '#'"]),

 dict(id="sultan", name="Sultan Medical Equipments Repair (BAB SULTAN EST)", short="Sultan Medical",
   url="https://sultanmedicalrepair.com/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(1, "Generic WPForms (name/email/message)"), whatsapp=F(0), livechat=F(0),
     map=F(0), tel=F(0, "Header phone is plain text"), faq=F(0), blog=F(0), careers=F(0), social=F(0),
     schema=F(0, "Also: empty homepage <title>, no meta description"), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(1), amc=F(0.5, "'Proactive maintenance plans' with priority service"),
     est=F(1), install=F(0), parts=F(1), training=F(0), radiation=F(0)),
   trust=dict(years="©2009 in footer (no explicit claim)", iso="—",
     testimonials="1, unattributed", client_logos="—", oem_logos="—",
     other="Counters: 500+ devices/month, 98% satisfaction, 90-day warranty, 365-day emergency line"),
   notes=["Homepage <title> tag is empty; no meta description"]),

 dict(id="raza", name="Raza Medical Equipment", short="Raza Medical",
   url="https://razamedicalequipment.com/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(0, "No contact form rendered despite form plugin installed"), whatsapp=F(0),
     livechat=F(0), map=F(0), tel=F(1, "Click-to-call in header"), faq=F(1, "3 questions"),
     blog=F(0, "Only default 'hello world' post"), careers=F(0), social=F(0), schema=F(0), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(0.5, "Mentioned in body copy, not a service card"), amc=F(0),
     est=F(0), install=F(0), parts=F(0), training=F(0), radiation=F(0)),
   trust=dict(years="—", iso="—", testimonials="2 named individuals", client_logos="—", oem_logos="—",
     other="'Certified technicians' claim (no certification named); 4-step working-process explainer; privacy policy page"),
   notes=["Imaging repair list includes MRI — a heavy claim for a small shop (as listed on their site)"]),

 dict(id="biomax", name="Biomax Medical & Laboratory Equipment Repairing Co LLC", short="Biomax",
   url="https://biomaxmedicalservices.com/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(1, "WPForms Lite"), whatsapp=F(0), livechat=F(0), map=F(0), tel=F(None),
     faq=F(0), blog=F(0, "Only default 'Hello world!' post"), careers=F(0),
     social=F(0.5, "Icons point to platform homepages, not actual profiles"),
     schema=F(0.5, "AIOSEO blocks, but Organization description is default 'My WordPress Blog'"), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(1), amc=F(1, "'Comprehensive maintenance plans'"), est=F(0),
     install=F(0), parts=F(0), training=F(0), radiation=F(0)),
   trust=dict(years="—", iso="—", testimonials="3 named (no organizations)", client_logos="—", oem_logos="—",
     other="'Certified repair specialists' claim (no certificates named); no email address displayed anywhere"),
   notes=["Schema description left as default 'My WordPress Blog'", "Social icons link to platform homepages"]),

 dict(id="meditron", name="Meditron Healthcare Technologies LLC (MHT)", short="Meditron",
   url="https://meditron.ae/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(0, "Contact page lists only email/WhatsApp/address"), whatsapp=F(1), livechat=F(0),
     map=F(1), tel=F(None), faq=F(0), blog=F(0, "/blog.html repurposed as Projects page"), careers=F(0),
     social=F(1, "Facebook, X, YouTube, Instagram"), schema=F(0.5, "Minimal Organization (name + url)"),
     shop=F(0.5, "Product catalog with search, no cart")),
   services=dict(ppm=F(1, "Per DHA/MOH/DOH/JCI guidelines"), calibration=F(1), amc=F(1), est=F(1),
     install=F(1, "Commissioning + turnkey clinic setup"), parts=F(1, "In-house workshop + spare parts stock"),
     training=F(1, "User training"), radiation=F(1, "X-ray QC per FANR by MOH-licensed physicist")),
   trust=dict(years="Established 2008", iso="—",
     testimonials="8+ named with facility names", client_logos="—", oem_logos="6",
     other="Strongest compliance framing in the set: DHA/MOH/DOH/JCI guidelines, DAC-approved calibration of test instruments, EST reports, validity stickers"),
   notes=[]),

 dict(id="vital", name="Vital Medical Equipments LLC", short="Vital Medical",
   url="https://vitalmedllc.com/", category="direct", emirate="Abu Dhabi",
   features=dict(
     arabic=F(0), form=F(1, "Basic enquiry form (PHP handler)"), whatsapp=F(1), livechat=F(0),
     map=F(0.5, "Embed shows generic Abu Dhabi city, not their Mussafah office"), tel=F(None), faq=F(0),
     blog=F(0), careers=F(0), social=F(0.5, "Single Facebook icon with empty href"), schema=F(0), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(0.5, "Within PPM scope"), amc=F(0), est=F(1),
     install=F(0.5, "Mentioned in passing"), parts=F(0), training=F(0), radiation=F(0)),
   trust=dict(years="Established 2013", iso="—", testimonials="—", client_logos="—", oem_logos="—",
     other="Names its test-instrument brands (Fluke Biomedical, BC Biomedical, Ohmic, Ophir); 13-segment 'industries we serve' list; breakdown support explicitly Mon–Fri 8–5 (no 24/7 claim)"),
   notes=["Contact emails are hotmail/gmail (no domain email)", "Map embed is a generic city view"]),

 dict(id="cyrix", name="CYRIX-TSL (Cyrix Healthcare / Technical Services Lab)", short="Cyrix-TSL",
   url="https://cyrix-tsl.com/", category="direct", emirate="Dubai + 5 offices (MENA)",
   features=dict(
     arabic=F(0, "/ar/ returns a byte-identical English copy (soft duplicate)"), form=F(1, "Get-a-Quote offcanvas form on every page, with reCAPTCHA"),
     whatsapp=F(0), livechat=F(0), map=F(0.5, "Per-office links only — no embed"), tel=F(None),
     faq=F(0), blog=F(1, "5 posts Jan–Feb 2026"), careers=F(0),
     social=F(0.5, "IG/X/LinkedIn — parent-company TSL accounts"), schema=F(0, "Only basic OG tags"),
     shop=F(1, "External store cyrixhealthcare.com")),
   services=dict(ppm=F(1), calibration=F(1), amc=F(1), est=F(0),
     install=F(1, "IQ/OQ/PQ qualification"), parts=F(0.5, "Equipment & consumables supply (incl. used/re-certified per footer)"),
     training=F(1, "Clinical application & training"), radiation=F(0)),
   trust=dict(years="Since 2011 (timeline back to 2004, India)", iso="—",
     testimonials="—", client_logos="~23 incl. government health bodies (Saudi MoH, Kuwait MoH, SEHA)",
     oem_logos="~40", other="Counters: 620+ certified professionals, 6,400+ clients; claims to be the only MENA company doing board-level biomedical repair"),
   notes=["Footer discloses equipment may be used/surplus/re-certified", "Social accounts belong to parent company TSL"]),

 dict(id="alwan", name="Alwan Alamal Medical & Laboratory Equipment Repairing Est", short="Alwan Alamal",
   url="https://alamalmedical.com/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(0.5, "Form has no action attribute (static HTML export) — submission likely non-functional"),
     whatsapp=F(0), livechat=F(0), map=F(1, "Umm Ramool location"),
     tel=F(0.5, "Header tel: dials a number not displayed anywhere on the site"), faq=F(0), blog=F(0),
     careers=F(0), social=F(0), schema=F(None), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(1), amc=F(0.5, "Preventive programs; no AMC/CMC naming"), est=F(1),
     install=F(0), parts=F(1, "Supplier of equipment & disposables"), training=F(1, "Training & technical assistance"),
     radiation=F(0)),
   trust=dict(years="'Over four years of experience'", iso="—", testimonials="—", client_logos="—", oem_logos="—",
     other="Counters: 50+ customers, 100+ equipments, 10+ employees; heavy dental device list; multilingual staff claim"),
   notes=["mailto link malformed (info@www.alamalmedical.com)", "Header tel: number doesn't match any displayed number"]),

 dict(id="alsarm", name="Alsarm Medical & Laboratory Equipment Repairing", short="Alsarm",
   url="https://alsarmmedical.com/", category="direct", emirate="UAE (no street address shown)",
   features=dict(
     arabic=F(0), form=F(1, "Elementor Pro form, all fields required"), whatsapp=F(1, "Chaty widget + all 5 'Get Quotation' buttons open WhatsApp"),
     livechat=F(0), map=F(0.5, "Footer map is a country-level UAE view; contact-page embed points to the London Eye, UK (template default)"),
     tel=F(0.5, "Phone channel via Chaty widget"), faq=F(0), blog=F(0), careers=F(0), social=F(0), schema=F(0), shop=F(0)),
   services=dict(ppm=F(0), calibration=F(0), amc=F(0), est=F(0), install=F(0), parts=F(0),
     training=F(0), radiation=F(0)),
   trust=dict(years="'15+ years' counter", iso="—", testimonials="3 named with organizations", client_logos="—", oem_logos="—",
     other="Niche focus: medical refrigeration/freezers, centrifuges, incubators, mortuary units; counters: 2K+ clients, 4.7 rating"),
   notes=["Contact-page map embed points to London Eye, London", "'Why choose us' copy references the construction industry (template leftover)", "Address shown only as 'United Arab Emirates'"]),

 dict(id="wadi", name="Wadi Al Hanan Medical & Laboratory Equipment Repairing Co.", short="Wadi Al Hanan",
   url="https://wadialhananmadica.tech/", category="direct", emirate="Dubai",
   features=dict(
     arabic=F(0), form=F(1, "On homepage, maintenance and support pages"), whatsapp=F(0), livechat=F(0),
     map=F(0.5, "Homepage embed OK (Business Bay); support-page embed points to Springfield, MA, USA"),
     tel=F(None), faq=F(0), blog=F(0), careers=F(0), social=F(0),
     schema=F(0.5, "WebSite type only"), shop=F(0)),
   services=dict(ppm=F(1), calibration=F(1), amc=F(0), est=F(0), install=F(0.5, "Parts installation"),
     parts=F(1, "Genuine parts supply"), training=F(0), radiation=F(0)),
   trust=dict(years="—", iso="—", testimonials="2 (reference Riyadh/Jeddah — placeholder-like)", client_logos="—", oem_logos="—",
     other="—"),
   notes=["Support page shows placeholder phone '1234567890' and a US placeholder address", "Testimonials reference Saudi cities"]),

 dict(id="arh", name="ARH — Al Reem Hospico LLC (شركة الريم هوسبيكو)", short="Al Reem Hospico",
   url="https://arh.ae/", category="adjacent", emirate="UAE (multiple offices)",
   features=dict(
     arabic=F(1, "Full first-class Arabic at /ar — RTL stylesheets, hreflang, all main pages translated (some EN remnants)"),
     form=F(1, "Enquiry form with type dropdown + CSRF"), whatsapp=F(0.5, "WhatsApp nav item leads to an empty page"),
     livechat=F(0), map=F(0.5, "Per-office links only"), tel=F(1, "tel:, mailto:, fax: links"),
     faq=F(0), blog=F(0), careers=F(0.5, "Careers page exists but is empty"),
     social=F(0.5, "Facebook OK; LinkedIn link is an /admin/ URL"),
     schema=F(0.5, "Present on every page but filled with leftover boilerplate text"), shop=F(0.5, "Product pages with downloadable PDF brochures")),
   services=dict(ppm=F(None), calibration=F(0), amc=F(None), est=F(0),
     install=F(1, "Supply, installation, commissioning, training, after-sales"), parts=F(None),
     training=F(1), radiation=F(0)),
   trust=dict(years="Since 1981; incorporated 1990 (UAE-UK JV); '40+ years' counter",
     iso="ISO 9001:2015 (since 2004), ISO 14001:2015, OHSAS 18001:2007",
     testimonials="—", client_logos="—", oem_logos="40+ international partners counter; 12 brands",
     other="Claims 80%+ UAE healthcare-engineering market share; AED 500M New Al Ain Hospital turnkey contract; hospital facility management & MEP — a different weight class (adjacent, not a like-for-like repair shop)"),
   notes=["Staff counter differs between Arabic (750+) and English (1250+) pages", "Webmail login links exposed in public header", "Footer reads 'Reem Hospital © 2021'"]),

 dict(id="urs", name="URS Testings Laboratory LLC", short="URS Labs",
   url="https://urslabs.com/", category="adjacent", emirate="Dubai",
   features=dict(
     arabic=F(1, "Dedicated parallel Arabic site at /arabic/ — translated nav, pages and services (some EN blocks remain); no visible cross-link from EN site"),
     form=F(1, "Contact Form 7"), whatsapp=F(1, "Separate numbers for EN and AR sites"), livechat=F(1, "Tawk.to"),
     map=F(None), tel=F(None), faq=F(None), blog=F(1, "Insights/blog incl. 2-3 Arabic posts"),
     careers=F(0.5, "Careers email only"), social=F(1, "FB, IG, LinkedIn, X"),
     schema=F(1, "WebSite, WebPage, Article, Organization, SearchAction"), shop=F(0)),
   services=dict(ppm=F(0), calibration=F(1, "Accredited calibration services"), amc=F(0), est=F(0),
     install=F(0), parts=F(0.5, "Supply of instruments + technical manpower"), training=F(1), radiation=F(0)),
   trust=dict(years="30+ years", iso="ISO/IEC 17025:2017 accredited (EIAC/DAC + ENAS) — certificates downloadable",
     testimonials="—", client_logos="Radisson, Shangri-La, Zulekha Hospital, Dubai Airport, JAFZA, Trakhees…",
     oem_logos="—", other="Testing laboratory (food/water/environment/chemical + calibration) — adjacent comparator, not a repair shop; approved by UAE government departments"),
   notes=[]),
]

# attach raw catalogs
host_map = {
 "paramount": "paramountuae.com", "ihag": "ihag.ae", "adamsmed": "adamsmed.ae",
 "sultan": "sultanmedicalrepair.com", "raza": "razamedicalequipment.com",
 "biomax": "biomaxmedicalservices.com", "meditron": "meditron.ae", "vital": "vitalmedllc.com",
 "cyrix": "cyrix-tsl.com", "alwan": "alamalmedical.com", "alsarm": "alsarmmedical.com",
 "wadi": "wadialhananmadica.tech", "arh": "arh.ae", "urs": "urslabs.com",
}
for comp in companies:
    if comp["id"] == "qaboos":
        comp["raw"] = {
            "name": comp["name"], "url": comp["url"], "reachable": True,
            "nav_sections": ["Home", "About Us", "Services", "Careers", "FAQ", "License", "Contact", "العربية (/ar/)"],
            "services_listed": ["Biomedical equipment repair", "Preventive maintenance (PPM)",
                "Calibration & performance verification", "Laboratory analyzer servicing",
                "Imaging & diagnostic maintenance", "Patient monitoring servicing",
                "Installation, testing & commissioning", "Annual Maintenance Contracts (AMC/CMC)",
                "Electrical safety testing (EST)", "Spare parts sourcing & supply",
                "Equipment inspection & reports", "Emergency breakdown support"],
            "trust_signals": ["Full Dubai DET professional license table (No. 1475682, CR 1265308) with verification link",
                "No invented claims: no testimonials, client logos, ISO badges or years-in-business counters (licensed Feb 2025)"],
            "site_features": ["Crawlable Arabic page /ar/ with reciprocal hreflang", "Bilingual FAQ (7 Q&As)",
                "Google Maps embed", "tel: click-to-call links", "JSON-LD: MedicalBusiness, FAQPage, JobPosting",
                "Open Graph + Twitter cards", "sitemap.xml + robots.txt + favicon", "mailto-based contact form (no backend)"],
            "arabic_support": "full bilingual — separate crawlable /ar/ page, lang=ar dir=rtl, reciprocal hreflang",
            "brands_serviced": [], "standout_items": ["Only site in this set displaying a verifiable trade license"],
        }
    else:
        comp["raw"] = raw_by_host[host_map[comp["id"]]]
    comp["services_count"] = len(comp["raw"].get("services_listed", []))

out = {
  "meta": {
    "title": "UAE Medical & Laboratory Equipment Services — Public Website Comparison",
    "captured": "2026-06-11",
    "method": "Each company's publicly accessible website was visited and cataloged on 11 June 2026 (homepage + key inner pages, English and Arabic versions where present). Trust figures (years, counters, certifications) are reproduced AS CLAIMED on each company's own site and are not independently verified.",
    "disclaimer": "This comparison is compiled exclusively from publicly available information on the companies' own websites. No affiliation with or endorsement by any listed company is implied. Websites change frequently — data reflects a single capture date and may be outdated or contain errors. All trademarks and brand names belong to their respective owners. Corrections are welcome.",
    "companies_count": len(companies),
  },
  "columns": {
    "features": [
      ["arabic", "Arabic website"], ["form", "On-page contact/quote form"], ["whatsapp", "WhatsApp chat"],
      ["livechat", "Live chat"], ["map", "Google Maps embed"], ["tel", "Click-to-call (tel:)"],
      ["faq", "FAQ section"], ["blog", "Blog / news"], ["careers", "Careers page"],
      ["social", "Social media links"], ["schema", "Structured data (JSON-LD)"], ["shop", "Online shop / catalog"]
    ],
    "services": [
      ["ppm", "Preventive maintenance (PPM)"], ["calibration", "Calibration"], ["amc", "AMC / CMC contracts"],
      ["est", "Electrical safety testing"], ["install", "Installation & commissioning"],
      ["parts", "Spare parts supply"], ["training", "User training"], ["radiation", "Radiation / FANR services"]
    ]
  },
  "companies": companies,
}
json.dump(out, open('/Users/pl/qaboos-market-matrix/data.json', 'w'), ensure_ascii=False, indent=1)
print("data.json written:", len(companies), "companies")
for c in companies:
    print(" -", c["id"], "| services_count:", c["services_count"], "| raw keys:", len(c["raw"]))
