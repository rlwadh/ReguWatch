# ReguWatch — Daily Summary
Date (UTC): 2025-11-05

## Changes today

### Issue #11
**Page:** [https://www.iso.org/insights/standards-world](https://www.iso.org/insights/standards-world)
**Changes:** Text

**Full text diff:**
```
--- Issue #11 (old)
+++ Issue #11 (new)
@@ -192,8 +192,8 @@
         let begin = 0 + 3;
         const cat = 'standards-world';
         const pageSize = 8;
-        const button = jQuery("#more-a1e5e64a-8c87-47b3-bc39-f22c43db97da");
-        let buttonWrapper = jQuery("#btn-more-wrapper-a1e5e64a-8c87-47b3-bc39-f22c43db97da");
+        const button = jQuery("#more-1a5d523e-c9ee-4194-aa9f-613f2729e246");
+        let buttonWrapper = jQuery("#btn-more-wrapper-1a5d523e-c9ee-4194-aa9f-613f2729e246");
         if (buttonWrapper.length === 0) buttonWrapper = button;
         var nextItems;
         button.click(function () {
@@ -204,9 +204,9 @@
                 url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-news/section-latest-news/latest-news.html.ajax',
                 type: 'GET',
                 data: {
-                    'nb-a1e5e64a-8c87-47b3-bc39-f22c43db97da': pageSize,
-                    'offset-a1e5e64a-8c87-47b3-bc39-f22c43db97da': begin,
-                    'cat-a1e5e64a-8c87-47b3-bc39-f22c43db97da': cat,
+                    'nb-1a5d523e-c9ee-4194-aa9f-613f2729e246': pageSize,
+                    'offset-1a5d523e-c9ee-4194-aa9f-613f2729e246': begin,
+                    'cat-1a5d523e-c9ee-4194-aa9f-613f2729e246': cat,
                     'tag': ''
                 },
                 statusCode : {
@@ -298,8 +298,8 @@
         let begin = 0 + 3;
         const cat = 'standards-world';
         const pageSize = 8;
-        const button = jQuery("#more-1c646ffc-c1f8-48b8-9e91-9c72d074db13");
-        let buttonWrapper = jQuery("#btn-more-wrapper-1c646ffc-c1f8-48b8-9e91-9c72d074db13");
+        const button = jQuery("#more-6e7f9a1d-d8d1-4168-a1ee-7d0055461959");
+        let buttonWrapper = jQuery("#btn-more-wrapper-6e7f9a1d-d8d1-4168-a1ee-7d0055461959");
         if (buttonWrapper.length === 0) buttonWrapper = button;
         var nextItems;
         button.click(function () {
@@ -310,9 +310,9 @@
                 url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-members/section-latest-members/latest-members.html.ajax',
                 type: 'GET',
                 data: {
-                    'nb-1c646ffc-c1f8-48b8-9e91-9c72d074db13': pageSize,
-                    'offset-1c646ffc-c1f8-48b8-9e91-9c72d074db13': begin,
-                    'cat-1c646ffc-c1f8-48b8-9e91-9c72d074db13': cat,
+                    'nb-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': pageSize,
+                    'offset-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': begin,
+                    'cat-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': cat,
                     'tag': ''
                 },
                 statusCode : {
```
