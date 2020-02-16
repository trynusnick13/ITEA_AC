# HW
You have `hw_start.py` file which has list of insights.
Create programs that:
1. Remove unused keys from insight like:
    * period
    * count
    * total_count
    * page_id
    * entities_affected -> entities -> :
        * link
        * status
        * days_in_data
2. Remove keys which not fit the condition:
    * Remove each element from "table_columns" where "unit" not equal to "EUR"
    * Remove each element from "metric_sums" where "unit_key" not equal to "EUR"
3. Get all insights objectives into list of strings
4. Get all insights objectives into dict
5. Get all insights campaign_id into dict and list of values
5. Get all unique insights objectives
6. Get all insights "metric_sums" and calculate sum and average for (sum, sum_level, sum_general)
7. Sort list of insights by "type", "api", "report_name" and "objective"
8. If "report_name" equal "device" make this value uppercase
9. If "page_id" equal "(not set)" replace it by None

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
