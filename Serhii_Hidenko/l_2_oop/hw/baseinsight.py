from Serhii_Hidenko.l_2_oop.hw.metricsummary import MetricSummary


class BaseInsight:

    def __init__(self, metric_name=None, api=None, report_name=None, objective=None, unit=None, currency=None,
                 validator_insight_type=None, metric_summary=None, **kwargs):

        self.api = api

        # Check is api a correctly
        self._check_api_is_correct()

        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = kwargs["id"] if "id" in kwargs else None
        self.validator_insight_type = validator_insight_type

        # Create dict of metrics
        self.metrics = self._create_metrics(metric_summary)

    def _check_api_is_correct(self):
        """Check is api attribute a valid value"""

        valid_values = (1, 2, 3, 4)

        if self.api not in valid_values:
            raise ValueError(f"Incorrect value [{self.api}] for attribute api")

    @staticmethod
    def _create_metrics(metrics) -> dict:
        """
        Filter the values in metrics dict and replace it on MetricSummary instances
        :param metrics: List of dict where each element is some metric
        :type metrics: list
        :return: Dict of MetricSummary instances
        :rtype: dict
        """

        if not isinstance(metrics, dict):
            return {}

        metric_attributes = [attr for attr in dir(MetricSummary()) if not attr.startswith("__")
                             and not attr.endswith("__") and not attr.startswith("_")]

        for key, params in metrics.items():
            metrics[key] = MetricSummary(**dict(filter(lambda param: param[0] in metric_attributes, params.items())))

        return metrics
