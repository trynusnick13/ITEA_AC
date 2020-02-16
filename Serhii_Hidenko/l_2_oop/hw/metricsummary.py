class MetricSummary:

    def __init__(self, metric=None, metric_level=None, metric_average=None, is_outlier=None, true_sign=None, sign=None,
                 mark=None, unit=None, metric_name_frontend=None, mark_key=None, metric_name_frontend_key=None,
                 unit_key=None):

        self.metric = metric
        self.metric_level = metric_level
        self.metric_average = metric_average
        self.is_outlier = is_outlier
        self.true_sign = true_sign
        self.sign = sign
        self.mark = mark
        self.unit = unit
        self.metric_name_frontend = metric_name_frontend
        self.mark_key = mark_key
        self.metric_name_frontend_key = metric_name_frontend_key
        self.unit_key = unit_key
