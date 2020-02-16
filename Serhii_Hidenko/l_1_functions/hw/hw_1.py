from Serhii_Hidenko.source.hw_start import insights


def recursive_remove_unused(dict_block, unused) -> dict:
    """
    Recursive removes from `dict_block` keys from `unused`
    :param dict_block: Dictionary for analyze
    :type dict_block: dict
    :param unused: Dictionary to remove
    :type unused: dict
    :return: Result dictionary
    :rtype: dict
    """

    result_dict = {}

    for item_key, item_value in dict_block.items():

        if item_key not in unused.keys():
            result_dict[item_key] = item_value
        else:
            if unused[item_key] is None:
                pass
            elif isinstance(unused[item_key], dict):

                if isinstance(item_value, dict):
                    result_dict[item_key] = recursive_remove_unused(item_value, unused=unused[item_key])
                elif isinstance(item_value, list):

                    sub_list = []

                    for list_item in item_value:
                        sub_list.append(recursive_remove_unused(list_item, unused=unused[item_key]))

                    result_dict[item_key] = sub_list

    return result_dict


def get_insight_sort_string(sorting_insight, *args) -> str:
    """
    Get a string of insight sort parameters
    :param sorting_insight: Insight to be analyzed
    :type sorting_insight: dict
    :return: String of sort parameters
    :rtype: str
    """

    sort_string = ""

    for key in args:

        if key in sorting_insight:
            sort_string += key

    return sort_string


def transform_param(insight_to_analyze):
    """
    Change `param` of `insight` by `func`
    :param insight_to_analyze: Insight to be analyzed
    :type insight_to_analyze: dict
    """

    def transform_param_nested(**kwargs):

        if kwargs["param"] in insight_to_analyze.keys():
            insight[kwargs["param"]] = kwargs["func"](insight[kwargs["param"]])

        return insight

    return transform_param_nested


def recursive_search_parameter(insight_to_search, parameter) -> list:
    """
    Search all parameter in insight
    :param insight_to_search: Insight for search
    :type insight_to_search: dict
    :param parameter: Parameter
    :type parameter: str
    :return: List of found parameters
    :rtype: list
    """

    list_of_results = []

    for key, value in insight_to_search.items():

        if key == parameter:
            list_of_results.append(value)
        elif isinstance(value, dict):
            list_of_results.extend(recursive_search_parameter(value, parameter))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    list_of_results.extend(recursive_search_parameter(item, parameter))

    return list_of_results


if __name__ == "__main__":

    UNUSED_KEYS = {
        "period": None,
        "count": None,
        "total_count": None,
        "page_id": None,
        "entities_affected": {
            "entities": {
                "link": None,
                "status": None,
                "days_in_data": None
            }
        }
    }

    result = []
    list_of_objectives = []
    insights_campaigns = {}

    print(f"All insights before processing: {insights}")

    for i in range(len(insights) - 1):

        insight = insights[i]

        print(f"\tProcess {i}-th insight: {insight}")

        # First task in README.md
        insights[i] = recursive_remove_unused(insight, UNUSED_KEYS)

        print(f"\t\tFirst task result: {insight}")

        # Second task in README.md
        if "entities_affected" in insight and "table_columns" in insight["entities_affected"]:

            table_columns = []

            for table_column in insight["entities_affected"]["table_columns"]:

                if ("unit" in table_column and table_column["unit"] == "EUR") or "unit" not in table_column:
                    table_columns.append(table_column)

            insight["entities_affected"]["table_columns"] = table_columns

        try:

            metrics_sums = []

            for metric_sum in insight["metric_sums"]:

                if ("unit_key" in metric_sum and metric_sum["unit_key"] == "EUR") or "unit_key" not in metric_sum:
                    metrics_sums.append(metric_sum)

        except KeyError as err:
            print(f"Error handled: {err}")
        else:

            insight["metric_sums"] = metrics_sums

        print(f"\t\tSecond task result: {insight}")

        # Third task in README.md
        if "objective" in insight.keys():
            list_of_objectives.append(insight["objective"])

        # Fifth task in README.md
        insights_campaigns[i] = recursive_search_parameter(insight, "campaign_id")

        # Seventh task in README.md
        if "metric_sums" in insight.keys():
            sums = [ms["sum"] for ms in insight["metric_sums"]]
            sum_levels = [ms["sum_level"] for ms in insight["metric_sums"]]
            sum_generals = [ms["sum_general"] for ms in insight["metric_sums"]]

            print(f"\t\tSeventh task result:")

            for metric, metric_val in {"sums": sums, "sum_levels": sum_levels, "sum_generals": sum_generals}.items():
                metrics_sum = sum(metric_val)
                print(f"\t\t\tParam {metric} - sum: {metrics_sum}, avg: {metrics_sum / len(metric_val)}")

        transfer_func = transform_param(insight)

        # Ninth task in README.md
        insight = transfer_func(param="report_name", func=lambda value: value.upper() if value == "device" else value)
        print(f"\t\tNinth task result: {insight}")

        # Tenth task in README.md
        insight = transfer_func(param="page_id", func=lambda value: None if value == "(not set)" else value)
        print(f"\t\tTenth task result: {insight}")

    print(f"\tThird task result: {list_of_objectives}")

    # Fourth task in README.md
    dict_of_objectives = dict(map(lambda o: (o, list_of_objectives[o]), range(len(list_of_objectives))))
    print(f"\tFourth task result: {dict_of_objectives}")

    print(f"\tFifth task result: {insights_campaigns}")

    # Sixth task in README.md
    unique_objectives = set(list_of_objectives)
    print(f"\tSixth task result: {unique_objectives}")

    # Eighth task in README.md
    sorted_insights = sorted(insights, key=lambda ins: get_insight_sort_string(ins, "type", "api", "report_name",
                                                                                    "objective"))
    print(f"\tEighth task result: {sorted_insights}")
