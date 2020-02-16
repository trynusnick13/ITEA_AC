# HW
1. Develop metaclass for BaseInsight class from lesson 2 hw. 
    * Set attribute to class depend on api parameter:
        * If api == 1 set period attribute value == 3;
        * If api == 2 set period attribute value == 7;
        * If api == 3 set period attribute value == 10;
        * In other cases set period attribute value == 30;
    * Print each value of "network"(FB, Google...) dependent insight;
2. Give BaseInsight class functionality:
    * Define method for calculate sum of all attributes inside MetricSummary class.
    * Calculate sum of `metrics` for BaseInsight (MetricSummary instances attributes) if `metric` value > 30.
    * Define len magic method like len of `metrics`.
3. Define methods for BaseInsight that:
    * Get attribute value by `name`.
    * Print attribute value by `name`.
    * Define `property` for currency, unit, and print value.
    * Make method that return `report_name` uppercase.
    * Get api_name for network dependent insight by class name.
4. Define ABC AbstractInsight for BaseInsight with main methods.
5. Write decorator which save result of function call and time of execution 
into txt file (filename that you set) and decorate three methods inside BaseInsight.

6. Add print to console transactions values (write method for this action) 
and remove _copy_of_transactions from class instance in Account class.
Get from ../l_3_oop/8_context_manager_account.py
Note:
For each class, method and function write docstrings ;)
