# ReguWatch — Daily Summary
Date (UTC): 2026-05-17

## Changes today

### Issue #11
**Page:** [https://www.iso.org/insights/standards-world](https://www.iso.org/insights/standards-world)
**Changes:** Text

**Full text diff:**
```
--- Issue #11 (old)
+++ Issue #11 (new)
@@ -208,7 +208,7 @@
             if (nextItems != null)
                 buttonWrapper.before(nextItems)
             jQuery.ajax({
-                url: '/cms/live/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-news/section-latest-news/latest-news.html.ajax',
+                url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-news/section-latest-news/latest-news.html.ajax',
                 type: 'GET',
                 data: {
                     'nb-1a5d523e-c9ee-4194-aa9f-613f2729e246': pageSize,
@@ -314,7 +314,7 @@
             if (nextItems != null)
                 buttonWrapper.before(nextItems)
             jQuery.ajax({
-                url: '/cms/live/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-members/section-latest-members/latest-members.html.ajax',
+                url: '/cms/render/live/en/sites/isoorg/home/insights-news/news/standards-world/pagecontent/section-latest-members/section-latest-members/latest-members.html.ajax',
                 type: 'GET',
                 data: {
                     'nb-6e7f9a1d-d8d1-4168-a1ee-7d0055461959': pageSize,
```
