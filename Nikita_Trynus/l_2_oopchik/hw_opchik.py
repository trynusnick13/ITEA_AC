from Yurii_Khomych.l_1_functions.hw_start import *
from Nikita_Trynus.l_1_functions.insights_hw import *


class BaseInsight:
    # I need more attributes
    def __init__(self, metric_name=None, api=None, report_name=None, objective=None, unit=None, currency=None,
                 id=None, validator_insight_type=None, metrics={}):
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = metrics

    def __str__(self):
        return f'{self.metric_name}{self.api}{self.report_name}{self.objective}{self.unit}{self.currency}{self.id}{self.validator_insight_type}'

    def check_api(self):
        if not (self.api in [i for i in range(1, 5)]):
            raise ValueError('Inappropriate api')

    def __eq__(self, other):
        return self.api == other.api

    def __ne__(self, other):
        return self.objective != other.objective

    def __gt__(self, other):
        return self.id_1 > other.id_1

    # def __setattr__(self, key, value):
    #     if key not in vars(BaseInsight):


# Здесь через метаклассы создаю метрик_самм, но на этом этапе я не могу инициализировать так, как ты просил
# Поэтому дальше я создаю свой метакласс и переопределяю как он будет работать
list_of_metric_summary = get_all(insights, [], 'metric_summary')
needed_dict = dict(zip(list_of_metric_summary[0]['cpc'].keys(), [None] * len(list_of_metric_summary[0]['cpc'].keys())))
MetricSummary = type('MetricSummary', (), needed_dict)


class AttributeInitType(type):
    def __call__(self, *args, **kwargs):
        obj = type.__call__(self, *args)

        for key in kwargs:
            setattr(obj, key, kwargs[key])

        return obj


class MetricSummary(metaclass=AttributeInitType):
    pass


FacebookInsight = type('FacebookInsight', (BaseInsight,), {'dimensions_dict': None, 'dimensions': None})
GoogleInsight = type('GoogleInsight', (BaseInsight,), {'actions': None})
TwitterInsight = type('TwitterInsight', (BaseInsight,), {'first_date': None, 'last_date': None})
SnapchatInsight = type('SnapchatInsight', (BaseInsight,), {'weight': None, 'type': None})


def aapis(key):
    objects = {
        1: FacebookInsight(),
        2: GoogleInsight(),
        3: TwitterInsight(),
        4: SnapchatInsight(),
    }
    return objects[key]


def insight_builder(dict_from_insights):
    if dict_from_insights.get('api', None) is None:
        return None
    else:
        temp_obj = aapis(dict_from_insights['api'])
        for key in dict_from_insights.keys():
            if key in vars(BaseInsight()) or key in vars(type(temp_obj)):
                setattr(temp_obj, key, dict_from_insights[key])
            elif key == 'metric_summary':
                temp_obj.metrics.update(dict_from_insights[key])

        return temp_obj


for i in insights:
    a = insight_builder(i)
    print(insight_builder(i))
