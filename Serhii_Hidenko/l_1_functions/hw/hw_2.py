from Serhii_Hidenko.source.hw_start import insights


FORMULAS = {
    1: lambda ins_period, **kwargs: (kwargs["sum"] * kwargs["sum_level"] / kwargs["sum_general"]) / ins_period,
    2: lambda ins_period, **kwargs: (kwargs["sum"] * kwargs["sum_level"]**2 / kwargs["sum_general"]) / ins_period,
    3: lambda ins_period, **kwargs: (kwargs["sum_level"] / kwargs["sum_general"]) / ins_period,
    4: lambda ins_period, **kwargs: (kwargs["sum_level"] * 100) / ins_period
}


if __name__ == "__main__":

    for insight in insights:

        if "period" not in insight:
            continue

        # Set period by formula
        period = 7 if (isinstance(insight["period"], int) and insight["period"] > 4) or insight["period"] is None else \
            insight["period"]

        for metric_sum in insight["metric_sums"]:

            # Get formula from dict
            summary_func = FORMULAS.get(insight["api"], lambda: lambda: 0)

            try:
                metric_sum["summary"] = summary_func(period, **metric_sum)
            except ZeroDivisionError:
                metric_sum["summary"] = 0

            print({
                "period": period,
                "api": insight["api"],
                "sum": metric_sum["sum"],
                "sum_level": metric_sum["sum_level"],
                "sum_general": metric_sum["sum_general"],
                "summary": metric_sum["summary"]
            })

    list_of_entities = []

    for insight in insights:

        if "entities_affected" not in insight:
            continue

        list_of_entities += filter(lambda entity: entity["spend_sum"] > 200, insight["entities_affected"]["entities"])

    print(list_of_entities)
