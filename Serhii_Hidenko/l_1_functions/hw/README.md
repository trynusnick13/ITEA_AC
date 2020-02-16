# HW
You have `hw_start.py` file which has list of insights.
Create function for each exercise that:
1. Remove unused keys from insight like:
    * On root level remove:
        * period
        * count
        * total_count
        * page_id
    * On entities_affected -> entities level remove:
        * link
        * status
        * days_in_data
2. Remove keys which not fit the condition:
    * Remove each element from "table_columns" where "unit" not equal to "EUR"
    * Remove each element from "metric_sums" where "unit_key" not equal to "EUR"
3. Get all insights objectives into list of strings result: `["objective_1", "objective_2"]`
4. Get all insights objectives into dict result: `[{"objective": "objective_1"}, {"objective": "objective_2"},]`
5. Get all insights campaign_id into dict result: `[{"campaign_id": "123"}, {"campaign_id": "113"},]`
5. Get all unique insights objectives
6. Get all insights "metric_sums" and calculate sum and average 
for all elements of "metric_sums" list (sum, sum_level, sum_general) 
result:`{
"all_sum": sum of all insights of (sum, sum_level, sum_general) metric sums
"all_average": average of all insights of (sum, sum_level, sum_general) metric sums
}`
7. Sort list of insights by "type", "api", "report_name" and "objective"
8. If "report_name" equal "device" make this value uppercase
9. If "page_id" equal "(not set)" replace it by None
10. Calculate summary by formulas (if root "period" > 4 or None set default root "period" as 7):
    * root "api" == 1 formula: (sum * sum_level / sum_general) / period
    * root "api" == 2 formula: (sum * sum_level^2 / sum_general) / period
    * root "api" == 3 formula: (sum_level / sum_general) / period
    * root "api" == 4 formula: (sum_level * 100) / period
For each "metric_sums" you should add "summary" key which must be calculated based on "api" key on root level of insight
result:
```"metric_sums": [
            {
                "metric_name": "spend",
                "sum": 144.75208000000003,
                "sum_level": 394.1299989999985,
                "sum_general": 12705.189997000707,
                "unit": "EUR",
                "metric_name_frontend": "spend",
                "profit": 0.0,
                "frontend_metric_name_key": "spend",
                "unit_key": "EUR",

                "summary": "result_value"
            },
```
11. Merge all entities from entities ("entities_affected" -> "entities") into one list of dicts if "spend_sum" of entity > 200
result: 
```[
{
    "id": "6145532618172",
    "data_connector_id": 5693,
    "account_id": "act_111127989083608",
    "metric": 0.1730125739514349,
    "spend_sum": 235.124088,
    "first_date_from_data": "2019-12-11",
    "days_in_data": 7,...
},
{
    "id": "6145532618172",
    "data_connector_id": 5693,
    "account_id": "act_111127989083608",
    "metric": 0.1730125739514349,
    "spend_sum": 235.124088,
    "first_date_from_data": "2019-12-11",
    "days_in_data": 7,...
},
...
]
```

Create python programs using:
* Different data types
* Conditionals
* Handling exceptions
* Loop operators
* Comprehensions
* Args Kwargs
* Recursion
* Lambda
* Closures

For improve your programming skills use:
1. https://codeforces.com
2. https://www.codewars.com
3. https://leetcode.com
4. https://checkio.org
