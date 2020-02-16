# HW

1. Develop class BaseInsight based on insights from lesson 1 hw.
    * Get main keys ("metric_name", "api", "report_name", "objective", "unit", "currency", "id", "validator_insight_type") for base class attributes.
    * Write method that check "api" in 1,2,3,4 else raise Error
    * -- Define magic methods for comparing insights. (Compare insight by "api", "objective", "id")
    * Create attribute `metrics` which is dict of metric_name and MetricSummary class instances with it's own attributes. (Use "metric_summary" key)
        * Write method in BaseInsight that create MetricSummary instances from passed "metric_summary" keys and add it to `metrics` dict.
        self.metrics = `{"cpc": MetricSummary(metric_name, metric...)}`...
   
2. For each "api" key create it's own Insight class with additional attributes:
    * api == 1 -> FacebookInsight ("dimensions_dict", "dimensions");
    * api == 2 -> GoogleInsight ("actions");
    * api == 3 -> TwitterInsight ("first_date", "last_date");
    * api == 4 -> SnapchatInsight ("weight", "type");

3. Write final function insight_builder for get only needed keys
from each insight for create Insight network related instances list.
    * -- Make copy of each insight and create each insight only 
    from prepared dicts (remove unnecessary keys from insight).