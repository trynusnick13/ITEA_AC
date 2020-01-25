import timeit
import json
import copy
from collections import OrderedDict

import ujson
import msgpack

dataset = {
    "dimensions": [
        {"name": "dimension:campaign_id", "value": "6130250628865"}
    ],
    "metric": 5.432732558139534,
    "metric_avg": 45.14786447022595,
    "dimensions_count": 1,
    "metric_name": "cpa",
    "metric_sums": [
        {
            "metric_name": "spend",
            "sum": 934.4300000000001,
            "sum_general": 43974.01999400004,
            "unit": "currency",
        },
        {
            "metric_name": "impressions",
            "sum": 85408.0,
            "sum_general": 2569337.0,
            "unit": "",
        },
        {
            "metric_name": "action_link_click",
            "sum": 1083.0,
            "sum_general": 26752.0,
            "unit": "",
        },
        {
            "metric_name": "action_offsite_conversion",
            "sum": 172.0,
            "sum_general": 974.0,
            "unit": "",
        },
        {
            "metric_name": "action_offsite_conversion_value",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "action_post_engagement",
            "sum": 6879.0,
            "sum_general": 29241.0,
            "unit": "",
        },
        {
            "metric_name": "action_rsvp",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "action_like",
            "sum": 1.0,
            "sum_general": 2.0,
            "unit": "",
        },
        {
            "metric_name": "action_leadgen.other",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "action_app_install",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "video_10_sec_watched_actions_video_view",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "video_p100_watched_actions_video_view",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "action_mobile_app_install",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "action_app_custom_event.fb_mobile_purchase",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "action_app_custom_event.fb_mobile_purchase_value",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "action_landing_page_view",
            "sum": 953.0,
            "sum_general": 7031.0,
            "unit": "",
        },
        {"metric_name": "reach", "sum": 0.0, "sum_general": 0.0, "unit": ""},
        {
            "metric_name": "estimated_ad_recallers",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "website_purchase_conversion_value",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "action_onsite_conversion.messaging_first_reply",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {"metric_name": "clicks", "sum": 0.0, "sum_general": 0.0, "unit": ""},
        {
            "metric_name": "conversions",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "cpm",
            "sum": 57.783306094311186,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "cpc",
            "sum": 4.318533293174071,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "cpe",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "ctr",
            "sum": 0.06685483940815358,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "cpa",
            "sum": 28.509837763012182,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "conversionRate",
            "sum": 0.7892168164945768,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "engagementRate",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "impressionsPerUser",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "costPerRecall",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "recallRate",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "costPerEventResponse",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "conversionRateIntoRespondtents",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "costPerLead",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "leadConversionRate",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "costPerPageLike",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "conversionIntoPageLikers",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "costPerThousandPeopleReached",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "costPerVideoView",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "costPerFullVideoView",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "conversionTo10SecViews",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "costPerInstall",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "conversionToInstalls",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {"metric_name": "roas", "sum": 0.0, "sum_general": 0.0, "unit": ""},
        {
            "metric_name": "conversionFromInstallsToInAppPurchases",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "mobileRoas",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "averagePurchase",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "costPerInAppPurchases",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "aov",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {"metric_name": "arpu", "sum": 0.0, "sum_general": 0.0, "unit": "%"},
        {
            "metric_name": "costPerMessagingConversation",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "currency",
        },
        {
            "metric_name": "messagingConversationRate",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {"metric_name": "asr", "sum": 0.0, "sum_general": 0.0, "unit": "%"},
        {
            "metric_name": "first replies",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "",
        },
        {
            "metric_name": "conversion to full video view",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "conversionToFullVideoView",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
        {
            "metric_name": "conversionToVideoView",
            "sum": 0.0,
            "sum_general": 0.0,
            "unit": "%",
        },
    ],
    "metric_summary": {
        "cpa": {
            "metric": 5.432732558139534,
            "metric_average": 45.14786447022595,
            "threshold_value": 0.0,
            "timeseries": OrderedDict(
                [
                    ("2019-09-05", 7.952500000000001),
                    ("2019-09-06", 5.438285714285714),
                    ("2019-09-07", 5.036666666666671),
                    ("2019-09-08", 4.4658139534883725),
                    ("2019-09-09", 5.616571428571425),
                ]
            ),
            "timeseries_significance": OrderedDict(
                [
                    ("2019-09-05", True),
                    ("2019-09-06", True),
                    ("2019-09-07", True),
                    ("2019-09-08", True),
                    ("2019-09-09", True),
                ]
            ),
            "is_outlier": True,
            "sign": 1,
            "mean": 45.14786447022595,
        },
        "conversionRate": {
            "metric": 0.15881809787626963,
            "metric_average": 0.03640849282296651,
            "threshold_value": 0.0,
            "timeseries": OrderedDict(
                [
                    ("2019-09-05", 0.10582010582010581),
                    ("2019-09-06", 0.14957264957264957),
                    ("2019-09-07", 0.18571428571428572),
                    ("2019-09-08", 0.19724770642201836),
                    ("2019-09-09", 0.15086206896551724),
                ]
            ),
            "timeseries_significance": OrderedDict(
                [
                    ("2019-09-05", True),
                    ("2019-09-06", True),
                    ("2019-09-07", True),
                    ("2019-09-08", True),
                    ("2019-09-09", True),
                ]
            ),
            "is_outlier": True,
            "sign": 1,
            "mean": 0.03640849282296651,
        },
        "cpc": {
            "metric": 0.8628162511542012,
            "metric_average": 1.643765699536486,
            "threshold_value": 0.0,
            "timeseries": OrderedDict(
                [
                    ("2019-09-05", 0.8415343915343916),
                    ("2019-09-06", 0.8134188034188033),
                    ("2019-09-07", 0.9353809523809531),
                    ("2019-09-08", 0.8808715596330275),
                    ("2019-09-09", 0.847327586206896),
                ]
            ),
            "timeseries_significance": OrderedDict(
                [
                    ("2019-09-05", True),
                    ("2019-09-06", True),
                    ("2019-09-07", True),
                    ("2019-09-08", True),
                    ("2019-09-09", True),
                ]
            ),
            "is_outlier": True,
            "sign": 1,
            "mean": 1.643765699536486,
        },
        "ctr": {
            "metric": 0.012680310977894342,
            "metric_average": 0.010412024580660303,
            "threshold_value": 0.0,
            "timeseries": OrderedDict(
                [
                    ("2019-09-05", 0.015953405925550772),
                    ("2019-09-06", 0.014080269570972984),
                    ("2019-09-07", 0.014029930518439338),
                    ("2019-09-08", 0.01400668208686713),
                    ("2019-09-09", 0.008784551306323362),
                ]
            ),
            "timeseries_significance": OrderedDict(
                [
                    ("2019-09-05", True),
                    ("2019-09-06", True),
                    ("2019-09-07", True),
                    ("2019-09-08", True),
                    ("2019-09-09", True),
                ]
            ),
            "is_outlier": True,
            "sign": 1,
            "mean": 0.010412024580660303,
        },
        "cpm": {
            "metric": 10.94077838141626,
            "metric_average": 17.114928868420172,
            "threshold_value": 0.0,
            "timeseries": OrderedDict(
                [
                    ("2019-09-05", 13.425339748459526),
                    ("2019-09-06", 11.45315602623503),
                    ("2019-09-07", 13.123329770176385),
                    ("2019-09-08", 12.338087895142637),
                    ("2019-09-09", 7.443392654297609),
                ]
            ),
            "timeseries_significance": OrderedDict(
                [
                    ("2019-09-05", True),
                    ("2019-09-06", True),
                    ("2019-09-07", True),
                    ("2019-09-08", True),
                    ("2019-09-09", True),
                ]
            ),
            "is_outlier": True,
            "sign": 1,
            "mean": 17.114928868420172,
        },
    },
    "api": 1,
    "period": 14,
    "entities_affected": {
        "entities": [
            {
                "id": "6130250628865",
                "metric": 5.432732558139534,
                "spend_sum": 934.43,
                "overspend": 7765.432688878863,
                "threshold_action_num": 0.0,
                "level_fields": [],
                "metrics": {
                    "roas": 0.0,
                    "aov": 0.0,
                    "cpa": 5.432732558139534,
                    "conversionRate": 0.15881809787626963,
                    "cpc": 0.8628162511542012,
                    "ctr": 0.012680310977894342,
                    "cpm": 10.94077838141626,
                    "spend": 934.43,
                    "impressions": 85408.0,
                    "reach": 0.0,
                    "estimated_ad_recallers": 0.0,
                    "website_purchase_conversion_value": 0.0,
                    "action_link_click": 1083.0,
                    "action_post_engagement": 6879.0,
                    "action_offsite_conversion": 172.0,
                    "action_offsite_conversion_value": 0.0,
                    "action_rsvp": 0.0,
                    "action_like": 1.0,
                    "action_leadgen.other": 0.0,
                    "action_app_install": 0.0,
                    "video_10_sec_watched_actions_video_view": 0.0,
                    "video_p100_watched_actions_video_view": 0.0,
                    "action_mobile_app_install": 0.0,
                    "action_app_custom_event.fb_mobile_purchase": 0.0,
                    "action_app_custom_event.fb_mobile_purchase_value": 0.0,
                    "action_landing_page_view": 953.0,
                    "action_onsite_conversion.messaging_first_reply": 0.0,
                },
                "report_type": "fb",
                "metric_signs": {
                    "cpa": 2,
                    "conversionRate": 2,
                    "cpc": 2,
                    "ctr": 2,
                    "cpm": 2,
                },
                "data_connector_id": 5268,
            }
        ],
        "type": "campaign_id",
        "is_csv_export_supported": True,
        "count": 1,
        "total_count": 8,
        "threshold_action_value": 0.0,
    },
    "report_name": "advertiser_hour",
    "objective": ["CONVERSIONS"],
    "page_id": "(not set)",
    "optimal_start_date": "2019-08-11",
    "sign": 1,
    "id": "1cd03f32ff355fde892e669ee8371b61",
    "data_connector_id": 5268,
    "report_type": "fb",
}

if __name__ == "__main__":
    print("copy.deepcopy(dataset)")
    print(
        timeit.timeit(
            "copy.deepcopy(dataset)",
            setup="from __main__ import copy, dataset",
            number=10000,
        )
    )
    print("json.loads(json.dumps(dataset))")
    print(
        timeit.timeit(
            "json.loads(json.dumps(dataset))",
            setup="from __main__ import json, dataset",
            number=10000,
        )
    )
    print("ujson.loads(ujson.dumps(dataset))")
    print(
        timeit.timeit(
            "ujson.loads(ujson.dumps(dataset))",
            setup="from __main__ import ujson, dataset",
            number=10000,
        )
    )
    print("msgpack.unpackb(msgpack.packb(dataset))")
    print(
        timeit.timeit(
            "msgpack.unpackb(msgpack.packb(dataset))",
            setup="from __main__ import msgpack, dataset",
            number=10000,
        )
    )
