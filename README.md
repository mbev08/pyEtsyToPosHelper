# pyRainPOStoEtsy
___
## Object of Application
#### Run inventory checks between third party POS and Etsy.
1. Ability to configure app for any third party POS (not just Rain).
2. Ability to declare conversion rules for accurate inventory comparisons. 
3. Ability to declare rules to alert end-user of thresholds and other scenarios upon generating results.
___
## Todo List
1. Aggregate 'etsy' and 'rainpos' modules into a single module.
   1. Redesign module so it is more akin to Builder/Factory design patterns
      1. Done: Csv <set/get/validate> config, 
   2. Create default 'etsy' config
   3. 
2. Create a Config file so end-user can edit Etsy API if needed.
   1. YAML probably...
3. Refactor 'InventoryCompare', as it probably needs it.. can't remember.
   1. Is 'InventoryCompare.entity_handler' necessary? Probably not
   2. Redesign 'compare', as it does not conform to flexibility of having custom rules/thresholds.
4. Review 'reporter' 
   1. Can this be renamed? 'report_generator'? More direct.
   2. Looks like it's generally sound logic, but just review and try to make more flexible for custom reports. 
5. Create a simple (Desktop) GUI
   1. Allows end-user to:
      1. Configure
         1. Etsy API creds & paths
         2. Existing Third Party POS creds & paths
         3. Comparison alert rules/thresholds
         4. Report headers and maybe custom reports.
      2. Direct .CSV drop to input data for comparison
      3. Direct output of results/report
         1. Visualization of results?? 
         2. Export .CSV option
6. Create a simple SPA via django
   1. See objectives of #5

