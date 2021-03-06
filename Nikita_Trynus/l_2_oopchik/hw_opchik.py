from abc import (
    ABCMeta,
    abstractmethod
)

from Nikita_Trynus.l_1_functions.insights_hw import *
from Nikita_Trynus.l_3_opchik.save_time_in_txt import time_of_the_execution


class AbstractInsight(metaclass=ABCMeta):
    @abstractmethod
    def check_api(self):
        pass

    @abstractmethod
    def sum_of_metrics(self):
        pass


class BaseInsight(AbstractInsight):
    # I need more attributes
    def __init__(self, metric_name=None, api=None, report_name=None, objective=None, unit=None, currency=None,
                 id=None, validator_insight_type=None, metrics={}):
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self._unit = unit
        self._currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self._metrics = metrics

    def __str__(self):
        return f'{self.metric_name}{self.api}{self.report_name}{self.objective}{self.unit}{self.currency}{self.id}{self.validator_insight_type}'

    @time_of_the_execution()
    def check_api(self):
        if not (self.api in [i for i in range(1, 5)]):
            raise ValueError('Inappropriate api')

    @time_of_the_execution()
    def sum_of_metrics(self):
        sum_of_fields = 0
        for value_1 in self.metrics.values():
            for value_2 in value_1:
                if isinstance(value_1[value_2], int) or isinstance(value_1[value_2], float):
                    sum_of_fields += value_1[value_2]
        return sum_of_fields

    def sum_of_metrics_if_metric_gt_30(self):
        sum_of_fields = 0
        for value_1 in self.metrics.values():
            for value_2 in value_1:
                if value_1[value_2] > 30:
                    if isinstance(value_1[value_2], int) or isinstance(value_1[value_2], float):
                        sum_of_fields += value_1[value_2]
                else:
                    return None

        return sum_of_fields

    @property
    def currency(self):
        print(f'Returning currnecy ')
        return self._currency

    @currency.setter
    def currency(self, value):
        print(f'Setting currnecy ')
        self._currency = value

    @property
    def unit(self):
        print(f'Returning unit ')
        return self._unit

    @unit.setter
    def set_unit(self, value):
        print(f'Setting unit ')
        # setattr(self, 'unit', unit_1)
        self._unit = value

    def upper_case(self):

        return self.report_name.upper()

    def __len__(self):
        return len(self.metrics)

    def __eq__(self, other):
        return self.api == other.api

    def __ne__(self, other):
        return self.objective != other.objective

    def __gt__(self, other):
        return self.id_1 > other.id_1

    def to_dict(self):
        dict_to_write = {}
        for key, value in self.metrics.items():
            dict_to_write.update({key: value.__dict__})

        return dict_to_write

    def from_dict(self, dict_to_read):
        for name, value in dict_to_read.items():
            self.metrics.update({name: MetricSummary(**value)})

    # todo:
    #  get, set, and del item for metrics attribute.m

    @property
    def metrics(self):
        print(f'Returning metrics ')
        return self._metrics

    @metrics.setter
    def set_metrics(self, dict_to_set={}):
        if not dict_to_set:
            self.metrics = {}
        else:
            print(f'Setting setting ')
            for name, value in dict_to_set.items():
                self.metrics.update({name: MetricSummary(**value)})

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
        # temp_obj.metrics = {}
        for key in dict_from_insights.keys():
            if key in vars(BaseInsight()) or key in vars(type(temp_obj)):
                setattr(temp_obj, key, dict_from_insights[key])
            elif key == 'metric_summary':
                for name, value in dict_from_insights[key].items():
                    temp_obj.metrics.update({name: MetricSummary(**value)})
                    # a = {name: MetricSummary(**value)}

                    print({name: MetricSummary(**value)})
                    print(MetricSummary(**value).__dict__)

        return temp_obj


if __name__ == '__main__':
    for i in insights:
        a = insight_builder(i)
        print(insight_builder(i))
