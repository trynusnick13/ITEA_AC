from Serhii_Hidenko.l_2_oop.hw.task_2 import get_class_for_insight
from Serhii_Hidenko.source.hw_start import insights


def insight_builder(insight_dict) -> dict:
    """
    Build a dict of insight instance attributes
    :param insight_dict: Source insight dict
    :type insight_dict: dict
    :return: Dict of insight with attributes from class
    :rtype: dict
    """

    api = insight_dict["api"] if "api" in insight_dict else None

    insight_class = get_class_for_insight(api)

    attributes = [attr for attr in dir(insight_class(**insight)) if not attr.startswith("__")
                  and not attr.endswith("__") and not attr.startswith("_")]

    return {attribute: insight_dict[attribute] for attribute in attributes if attribute in insight_dict}


if __name__ == "__main__":

    for insight in insights:

        try:
            ib = insight_builder(insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(ib)
