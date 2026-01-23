# ReguWatch — Daily Summary
Date (UTC): 2026-01-23

## Changes today

### Issue #11
**Page:** [https://www.iso.org/insights/standards-world](https://www.iso.org/insights/standards-world)
**Changes:** Text & Links

**Full text diff:**
```
--- Issue #11 (old)
+++ Issue #11 (new)
@@ -1 +1,724 @@
-[ERROR fetching https://www.iso.org/insights/standards-world]: 403 Client Error: Forbidden for url: https://www.iso.org/insights/standards-world
+
+Skip to main content
+
+
+
+
+
+
+Applications
+
+
+
+OBP
+
+
+
+English
+
+
+español
+français
+русский
+
+
+
+
+
+
+
+
+
+
+
+
+Menu
+
+
+
+Standards
+Sectors
+Health
+IT & related technologies
+Management & services
+Security, safety & risk
+Transport
+Energy
+Diversity & inclusion
+Environmental sustainability
+Food & agriculture
+Materials
+Building & construction
+Engineering
+About ISO
+Insights & news
+Insights
+All insights
+Healthcare
+Artificial intelligence
+Climate change
+Transport
+
+Cybersecurity
+Quality management
+Renewable energy
+Occupational health and safety
+News
+Expert talk
+Standards world
+Media kit
+Resources
+ISO 22000 explained
+ISO 9001 explained
+ISO 14001 explained
+ISO 42001 explained
+ISO 45001 explained
+Taking part
+Store
+
+
+
+
+Search
+
+
+
+
+Cart
+
+
+
+
+
+
+
+
+
+
+News from the standards world
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+23 November 2025
+
+
+
+
+
+ISO at COP30 - Key outcomes and highlights
+
+At COP30 in Belém – in the heart of the Amazon – ISO and its partners showcased the power of International Standards to turn climate ambition into measurable action. Across two weeks of high-level discussions and interactive sessions, the Standards Pavilion became the hub for collaboration, knowledge …
+
+
+
+
+
+
+
+
+
+
+Institutional news
+
+
+
+
+
+
+
+
+
+
+
+
+
+12 January 2026
+
+
+
+
+Message from ISO President Dr Khaled Soufi
+
+
+
+
+
+
+
+
+
+
+
+
+12 December 2025
+
+
+
+
+Ten Emmys and counting: SC 29 honoured again for shaping the future of multimedia standards
+
+
+
+
+
+
+
+
+
+
+
+
+11 December 2025
+
+
+
+
+International Standards at the heart of development: ISO joins the World Bank in launching the World Development Report 2025
+
+
+
+
+
+Load more
+
+jQuery(document).ready(function () {
+        let begin = 0 + 3;
+        const cat = 'standards-world';
+        const pageSize = 8;
+        const button = jQuery("#more-1a5d523e-c9ee-4194-aa9f-613f2729e246");
+        let buttonWrapper = jQuery("#btn-more-wrapper-1a5d523e-c9ee-4194-aa9f-613f2729e246");
+        if (buttonWrapper.length === 0) buttonWrapper = button;
+        var nextItems;
+        button.click(function () {
+            button.hide()
+            if (nextItems != null)
+                buttonWrapper.before(nextItems)
+            jQuery.ajax({
+                url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-news/section-latest-news/latest-news.html.ajax',
+                type: 'GET',
+                data: {
+                    'nb-1a5d523e-c9ee-4194-aa9f-613f2729e246': pageSize,
+                    'offset-1a5d523e-c9ee-4194-aa9f-613f2729e246': begin,
+                    'cat-1a5d523e-c9ee-4194-aa9f-613f2729e246': cat,
+                    'tag': ''
+                },
+                statusCode : {
+                    200 : function () {
+                        begin += pageSize;
+                        button.show()
+                    },
+                    204 : function () {
+                        console.log("nothing more")
+                    }
+                },
+                success: function (result) {
+                    // test if any youtube frames were injected and bind them to youtube.js
+                    if ((typeof initYouTubeVideos === "function") && ($('.youtube-frame').length)) { initYouTubeVideos(); }
+                    nextItems = result
+                },
+                error: function () {
+                    console.log("error")
+                }
+            })
+        });
+        button.trigger("click")
+    })
+
+
+
+
+Latest from our community
+
+
+
+
+
+
+
+
+
+
+19 January 2026
+
+
+
+
+From mining scars to sustainable futures: ISO 24419-1 drives renewal in Peru
+
+
+
+
+
+
+
+
+
+
+
+
+12 August 2025
+
+
+
+
+How ISO is shaping sustainable cities
+
+
+
+
+
+
+
+
+
+
+
+
+17 June 2025
+
+
+
+
+Singapore sets benchmark with carbon-neutral tradeshows
+
+
+
+
+
+Load more
+
+jQuery(document).ready(function () {
+        let begin = 0 + 3;
+        const cat = 'standards-world';
+        const pageSize = 8;
+        const button = jQuery("#more-6e7f9a1d-d8d1-4168-a1ee-7d0055461959");
+        let buttonWrapper = jQuery("#btn-more-wrapper-6e7f9a1d-d8d1-4168-a1ee-7d0055461959");
+        if (buttonWrapper.length === 0) buttonWrapper = button;
+        var nextItems;
+        button.click(function () {
+            button.hide()
+            if (nextItems != null)
+                buttonWrapper.before(nextItems)
+            jQuery.ajax({
+                url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-members/section-latest-members/latest-members.html.ajax',
+                type: 'GET',
+                data: {
+                    'nb-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': pageSize,
+                    'offset-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': begin,
+                    'cat-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': cat,
+                    'tag': ''
+                },
+                statusCode : {
+                    200 : function () {
+                        begin += pageSize;
+                        button.show()
+                    },
+                    204 : function () {
+                        console.log("nothing more")
+                    }
+                },
+                success: function (result) {
+                    // test if any youtube frames were injected and bind them to youtube.js
+                    if ((typeof initYouTubeVideos === "function") && ($('.youtube-frame').length)) { initYouTubeVideos(); }
+                    nextItems = result
+                },
+                error: function () {
+                    console.log("error")
+                }
+            })
+        });
+        button.trigger("click")
+    })
+
+
+
+
+Latest publications
+
+
+
+
+
+
+
+
+
+
+The critical role of consumer voices in shaping standards for emerging technologies – Guide for NSBs
+
+This guide supports National Standards Bodies (NSBs) in shaping Critical Emerging Technology (CET) standards that serve society effectively, with a focus on involving consumer stakeholders in areas like AI. While primarily aimed at leaders and engagement officers in developing countries, it is relevant …
+
+
+
+
+
+
+
+
+
+
+
+
+
+Building better standards through effective consumer stakeholder engagement – Guide for NSBs
+
+This guide is intended for National Standards Bodies (NSBs), especially leaders and stakeholder-engagement officers in developing countries, but it is useful for any NSB aiming to strengthen the consumer voice in standards. Recognizing that NSBs vary in size, resources, and priorities, the recommendations …
+
+
+
+
+
+
+
+
+
+
+
+
+
+ISO policy brief: The role of the ISO system in supporting countries to implement their Nationally Determined Contributions(NDCs) and National Adaptation Plans (NAPs)
+
+This document is designed to help ISO members engage effectively with policymakers on climate action. It shows how International Standards can support countries in meeting their Nationally Determined Contributions (NDCs) and National Adaptation Plans (NAPs), and how quality infrastructure underpins credible, …
+
+
+
+
+
+
+
+
+
+
+
+
+
+ISO policy brief: Harnessing international standards for responsible AI development and governance
+
+This policy brief explains how consensus-based international standards transform high-level AI principles into practical requirements for the development of safe, transparent, trustworthy and responsible AI systems. Mapping the global policy landscape, it demonstrates how international standards support …
+
+
+
+
+
+
+
+New and popular standards
+
+
+
+
+
+
+
+
+
+
+International Standard
+
+ISO 17298:2025
+
+
+
+Biodiversity — Considering biodiversity in the strategy and operations of organizations — Requirements and guidelines
+
+Reference number
+ISO 17298:2025
+
+
+
+Edition 1
+2025-10
+
+© ISO 2026
+
+
+
+
+
+
+
+
+
+
+ISO 17298:2025
+
+
+Biodiversity — Considering biodiversity in the strategy and operations of organizations — Requirements and guidelines
+
+
+
+
+
+
+
+
+
+
+
+International Workshop Agreement
+
+
+
+
+
+
+
+IWA 49:2025
+
+
+Child-friendly multidisciplinary and interagency response services for children who are victims of violence — Requirements and recommendations
+
+
+
+
+
+
+
+
+
+
+
+
+
+International Standard
+
+ISO/IEC 27701:2025
+
+
+
+Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance
+
+Reference number
+ISO/IEC 27701:2025
+
+
+
+Edition 2
+2025-10
+
+© ISO 2026
+
+
+
+
+
+
+
+
+
+
+ISO/IEC 27701:2025
+
+
+Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+Draft
+International Standard
+
+ISO/UNDP DIS 53002
+
+
+
+Management systems for the United Nations Sustainable Development Goals SDGs — Implementation guidance
+
+Reference number
+ISO/UNDP DIS 53002
+
+
+
+Edition 1
+
+© ISO 2026
+
+
+Draft
+International Standard
+
+
+
+
+
+
+
+ISO/UNDP DIS 53002
+
+
+Management systems for the United Nations Sustainable Development Goals SDGs — Implementation guidance
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+Insights & news
+
+News
+
+Standards world
+
+
+
+Sitemap
+
+
+
+
+
+
+Standards
+Benefits
+Popular standards
+Conformity assessment
+SDGs
+Sectors
+Health
+IT & related technologies
+Management & services
+Security, safety & risk
+Transport
+Energy
+Environmental sustainability
+Materials
+About ISO
+What we do
+Structure
+Members
+Events
+Strategy
+Insights & news
+Insights
+All insights
+Healthcare
+Artificial intelligence
+Climate change
+Transport
+News
+Expert talk
+Standards world
+Media kit
+Resources
+ISO 22000 explained
+ISO 9001 explained
+ISO 14001 explained
+ISO 42001 explained
+ISO 45001 explained
+Taking part
+Who develops standards
+Deliverables
+Get involved
+Collaborating to accelerate effective climate action
+Resources
+Drafting standards
+Store
+Store
+Publications and products
+
+
+
+
+
+
+
+
+ISO name and logo
+Privacy Notice
+Copyright
+Cookie policy
+Media kit
+Jobs
+Help and support
+
+Making lives
+easier
+,
+safer
+and
+better
+.
+
+
+Sign up
+
+for email updates
+
+
+
+
+
+
+
+
+
+
+
+
+© All Rights Reserved
+
+All ISO publications and materials are protected by copyright and are subject to the user’s acceptance of ISO’s conditions of copyright. Any use, including reproduction requires our written permission. All copyright requests should be addressed to
+copyright@iso.org
+.
+
+With the exception of the content available through the
+ISO Open data
+page and subject to the terms contained therein, no ISO content may be used for any machine learning and/or artificial intelligence and/or similar technologies, including but not limited to accessing or using it to (i) train data for large language or similar models, or (ii) prompt or otherwise enable artificial intelligence or similar tools to generate responses.
+
+We are committed to ensuring that our website is accessible to everyone. If you have any questions or suggestions regarding the accessibility of this site, please
+contact us
+.
+
+
+
+
+
+
+
+Add to cart
+
+
+
+
+
+
+
+
+
+
+
+
+
+
```

**Added links (all):**
- https://login.iso.org
- https://twitter.com/isostandards
- https://www.facebook.com/isostandards
- https://www.flickr.com/photos/isostandards
- https://www.instagram.com/isostandards
- https://www.iso.org/ClimateAction.html
- https://www.iso.org/about
- https://www.iso.org/about/members
- https://www.iso.org/benefits-of-standards.html
- https://www.iso.org/conformity-assessment.html
- https://www.iso.org/contact-iso.html
- https://www.iso.org/contents/news/2025/06/singapore-carbon-neutral.html
- https://www.iso.org/contents/news/2025/08/iso-shaping-sustainable-cities.html
- https://www.iso.org/contents/news/2025/11/iso-at-cop30.html
- https://www.iso.org/contents/news/2025/12/sc-29-celebrates-another-emmy.html
- https://www.iso.org/contents/news/2026/01/from-mining-to-sustainable-futur.html
- https://www.iso.org/cookies.html
- https://www.iso.org/copyright.html
- https://www.iso.org/deliverables-all.html
- https://www.iso.org/developing-standards.html
- https://www.iso.org/drafting-standards.html
- https://www.iso.org/es/home/insights-news/news/standards-world.html
- https://www.iso.org/events.html
- https://www.iso.org/fr/home/insights-news/news/standards-world.html
- https://www.iso.org/get-involved.html
- https://www.iso.org/home.html
- https://www.iso.org/home/insights-news/insights/transport.html
- https://www.iso.org/home/insights-news/news/dossier-medias.html
- https://www.iso.org/home/insights-news/resources/iso-14001-explained.html
- https://www.iso.org/home/insights-news/resources/iso-22000-explained.html
- https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html
- https://www.iso.org/home/insights-news/resources/iso-45001-explained-what-it-is.html
- https://www.iso.org/home/insights-news/resources/iso-9001-explained.html
- https://www.iso.org/insights
- https://www.iso.org/insights/filtered-list-artificial-intelligence
- https://www.iso.org/insights/filtered-list-climate-change
- https://www.iso.org/insights/filtered-list-healthcare
- https://www.iso.org/insights/filtered-list-information-security
- https://www.iso.org/insights/filtered-list-occupational-health-and-safety
- https://www.iso.org/insights/filtered-list-quality-management
- https://www.iso.org/insights/filtered-list-renewable-energy
- https://www.iso.org/insights/standards-world
- https://www.iso.org/insights/subscribe
- https://www.iso.org/insights/thought-leadership
- https://www.iso.org/iso-name-and-logo.html
- https://www.iso.org/media-kit.html
- https://www.iso.org/news/2025/12/world-development-report-2025
- https://www.iso.org/news/2026/01/message-from-iso-president
- https://www.iso.org/obp/ui/en/
- https://www.iso.org/open-data.html
- https://www.iso.org/popular-standards.html
- https://www.iso.org/privacy.html
- https://www.iso.org/publication-list.html
- https://www.iso.org/publication/PUB100496.html
- https://www.iso.org/publication/PUB100498.html
- https://www.iso.org/publication/PUB100501.html
- https://www.iso.org/publication/PUB100502.html
- https://www.iso.org/resources.html
- https://www.iso.org/ru/home/insights-news/news/standards-world.html
- https://www.iso.org/sdg
- https://www.iso.org/sectors/building-construction
- https://www.iso.org/sectors/diversity-inclusion
- https://www.iso.org/sectors/energy
- https://www.iso.org/sectors/engineering
- https://www.iso.org/sectors/environment
- https://www.iso.org/sectors/food-agriculture
- https://www.iso.org/sectors/health
- https://www.iso.org/sectors/it-technologies
- https://www.iso.org/sectors/management-services
- https://www.iso.org/sectors/materials
- https://www.iso.org/sectors/security-safety-risk
- https://www.iso.org/sectors/transport
- https://www.iso.org/standard/17298
- https://www.iso.org/standard/27701
- https://www.iso.org/standard/89302.html
- https://www.iso.org/standard/92708.html
- https://www.iso.org/standards.html
- https://www.iso.org/store.html
- https://www.iso.org/strategy2030.html
- https://www.iso.org/structure.html
- https://www.iso.org/webstore/checkout?memberId=ISO&guilang=en
- https://www.iso.org/what-we-do.html
- https://www.iso.org/who-develops-standards.html
- https://www.iso.org/working-with-iso.html
- https://www.linkedin.com/company/isostandards
- https://www.vimeo.com/isostandards
- https://www.youtube.com/ISO
